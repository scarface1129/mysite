from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
        )


 def validate_email(value):
	email = self.cleaned_data.get("email")
	if ".edu" in email:
		raise forms.ValidationError("NOT A VALID Email Address")
	return email

ABILITY = ["Wonderful","Good","Excellent","Cool"]

def validate_ability(value):
	if value not in ABILITY:
		raise ValidationError("your are not even serious ")
