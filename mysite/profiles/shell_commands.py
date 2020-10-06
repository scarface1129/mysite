from django.contrib.auth import get_user_model

User = get_user_model


random_ = User.objects.last()
#my followers
random_.profile.folloers.all()
#following
random_.is_following.all()

