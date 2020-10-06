from django import forms
from .validators import validate_ability
from .models import GymLocation

class GymLocationCreateForm(forms.ModelForm):
	#email         = forms.EmailField()
	#ability        = forms.CharField(required=False, validators=[validate_ability])
	class Meta:
		model = GymLocation 
		fields = [
			
			'name',
			'location',
			'ability',
			'slug',
			'images',
			
		]
	# def clean_name(self):
	# 	name = self.cleaned_data.get("name")
	# 	if name == "hello":
	# 		raise forms.ValidationError("NOT A VALID NAME")
	# 	return name


	
	
