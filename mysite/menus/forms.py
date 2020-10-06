from django import forms
from .models import item
from django.db import models
from django.forms import ModelForm
from mmm.models import GymLocation


class ItemForm(forms.ModelForm):
	class Meta:
		model = item
		fields=[
			'gym',
            'name',
            'content',
            'excludes',
            'public',		
            'nickname',

		]
	def __init__(self, user, *args, **kwargs):
		#print(kwargs.pop('instance'))
		print(kwargs)
		print(user)
		super(ItemForm, self).__init__(*args, **kwargs)
		self.fields['gym'].queryset = GymLocation.objects.filter(owner = user)
