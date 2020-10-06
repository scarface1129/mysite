from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from .validators import validate_ability
from .utils import unique_slug_generator
from django.urls import reverse
from django.db.models import Q


User = settings.AUTH_USER_MODEL
class GymLocationQuerySet(models.query.QuerySet):
	
	def search(self, query):
		if query:
			query=query.strip()
			return self.filter(
				Q(name__icontains=query)|
				Q(location__icontains=query)|
				Q(ability__icontains=query)|
				Q(item__content__icontains=query)|
				Q(item__nickname__icontains=query)

				).distinct()
		else:
			return self
				

class GymLocationManager(models.Manager):
	
	def get_queryset(self):
		return GymLocationQuerySet(self.model, using=self._db)
	
	def search(self, query):
		return self.get_queryset().search(query)


class GymLocation(models.Model):
	owner              = models.ForeignKey(User,on_delete=models.CASCADE)
	name               = models.CharField(max_length=120)
	location           = models.CharField(max_length=120, null=True, blank=True)
	ability            = models.CharField(max_length=120, null=True, blank=True, validators=[validate_ability] )
	timestamp          = models.DateTimeField( auto_now_add= True)
	images             = models.FileField(upload_to= 'post_image',blank=True, null=True)
	updated            = models.DateTimeField(auto_now= True)
	slug               = models.SlugField(null=True, blank=True)
	objects            = GymLocationManager()
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['-updated', '-timestamp']

	def get_absolute_url(self):
		#return f"/Gym/{self.slug}"
		scar = reverse("mmm:detail", kwargs= {'slug':self.slug})
		return scar
	@property
	def title(self):
		return self.name
	
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	print("saving....")
	if instance.ability:
		instance.ability=instance.ability.capitalize()
	else:
		 instance.ability=instance.ability  
#	# if not instance.slug:
	# 	#instance.name = "Another new  title"
	instance.slug = unique_slug_generator(instance)


# def rl_post_save_receiver(sender, instance, created,  *args, **kwargs):
# 	print("saved")
# 	print(instance.timestamp)
# 	if not instance.slug:
# 		#instance.name = "Another new  title"
# 		instance.slug = unique_slug_generator(instance)
# 		instance.save()



pre_save.connect(rl_pre_save_receiver, sender=GymLocation)

#post_save.connect(rl_post_save_receiver, sender=GymLocation)

