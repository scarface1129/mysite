from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.urls import reverse
from .utils import code_generator
from django.core.mail import send_mail
from .tasks import sleepy
import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail



User = settings.AUTH_USER_MODEL
class ProfileManager(models.Manager):
	def toggle_follower(self, request_user, username_to_toggle):
		profile_ = Profile.objects.get(user__username__iexact = username_to_toggle)
		user = request_user
		is_following = False
		if user in profile_.followers.all():
			profile_.followers.remove(user)
		else:
			profile_.followers.add(user)
			is_following = True
			evm = profile_.activation_key
			print(evm)
		return profile_, is_following	


class Profile(models.Model):
	user               = models.OneToOneField(User, on_delete=models.CASCADE)
	followers          = models.ManyToManyField(User, related_name = 'is_following', blank=True)
	#following  		   = models.ManyToManyField(User, related_name = 'following', blank=True)
	activation_key     = models.CharField(max_length=120, blank=True, null=True)
	activated          = models.BooleanField(default=False)
	timestamp          = models.DateTimeField( auto_now_add= True)
	updated            = models.DateTimeField(auto_now= True)
	objects            = ProfileManager()


	def __str__(self): 
		return self.user.username
	def get_url(self):
		#return f"/Gym/{self.slug}"
		return reverse("profiles:detail", kwargs= {'username':self.username})

	def send_activation_email(self):
		print("Activation")
		if self.activated:
			pass
		else:
			self.activation_key = code_generator()#'somekey'
			self.save()
			#path_=reverse()
			path_ = reverse("activate", kwargs={"code":self.activation_key})
			subject = 'Activate Account'
			from_email = 'agboemmanuel002@gmail.com'
			message = f'Activate your account here: {path_}'
			recipient_list = [self.user.email]
			html_message = f'<p>Activate your account here: {path_}</p>'
			print(html_message)
			sent_mail= send_mail(
					subject,
					from_email,
					message,
					recipient_list,
					fail_silently=False,
					html_message=html_message)
			
			sleepy(10)
			return sent_mail
			# message = Mail(
			#     from_email='agboemmanuel002@gmail.com',
			#     to_emails='ruthozioma1997@gmail.com',
			#     subject='activate Account',
			#     html_content=f'<strong>Activate your account here:{path_}</strong>')
			# try:
			#     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
			#     response = sg.send(message)
			#     print(response.status_code)
			#     print(response.body)
			#     print(response.headers)
			# except Exception as e:
			#     print(e)

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	if created:
		profile, is_created = Profile.objects.get_or_create(user=instance)
		default_user_profile = Profile.objects.get_or_create(user_id=2)[0]
		default_user_profile.followers.add(instance)
		#default_user_profile.remove(instance)
		#default_user_profile.save()
		profile.followers.add(default_user_profile.user)
		profile.followers.add(2)


post_save.connect(post_save_user_receiver, sender=User)


