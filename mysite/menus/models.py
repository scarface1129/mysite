from django.db import models
from django.conf import settings
from mmm.models import GymLocation
from django.urls import reverse


# Create your models here.
User = settings.AUTH_USER_MODEL
class item(models.Model):
	user           = models.ForeignKey(User, on_delete=models.CASCADE)
	gym            = models.ForeignKey(GymLocation, on_delete=models.CASCADE)
	name           = models.CharField(max_length=120)
	content        = models.TextField(help_text="separate each item by a comma")
	excludes       = models.TextField(blank=True, null=True, help_text="separate each item by a comma")
	public         = models.BooleanField(default=True)
	timestamp     = models.DateTimeField( auto_now_add= True)
	updated       = models.DateTimeField(auto_now= True)
	nickname      = models.CharField(max_length=120,null=True)


	class Meta:
		ordering=[ '-updated', '-timestamp' ]
	def get_absolute_url(self):
		#return f"/Gym/{self.slug}"
		return reverse("menus:detail", kwargs= {'pk':self.pk})

	def __str__(self):
		return self.name.capitalize()


	def get_content(self):
		return self.content.split(',')


	def get_excludes(self):
		return self.excludes.split(',')