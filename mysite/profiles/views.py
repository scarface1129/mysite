from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import DetailView, View, CreateView
from mmm.models import GymLocation
from menus.models import item
from .models import Profile
from .forms import RegisterForm
from django.http import HttpResponse, HttpResponseRedirect

User = get_user_model()
def activate_user_view(request, code=None, *args, **kwargs):
    if code:
        qs = Profile.objects.filter(activation_key=code)
        if qs.exists() and qs.count() == 1:
            profile = qs.first()
            if not profile.activated:
               user_ = profile.user
               user_.is_active = True
               user_.save()
               profile.activated = True
               profile.activation_key = None
               profile.save()
               print("YOU ARE SO VERY WELCOME ")
               return redirect("/login")
    return redirect("/login")
# class ActivateView(View):
# 	def get(self,request):
# 		return HttpResponse("you can go ahead and paste your activation code here")

class RegisterView(CreateView):
	form_class = RegisterForm
	template_name ='registration/register.html' 
	success_url = '/'

	def dispatch(self, *args, **kwargs):
		# if self.request.user.is_authenticated:
		#  	return redirect('/logout')
		return super(RegisterView, self).dispatch(*args, **kwargs)



class ProfileFollowToggle(LoginRequiredMixin, View):
	def post(self, request, *args, **kwargs):
		username_to_toggle = request.POST.get("username").strip()
		profile_ ,is_following = Profile.objects.toggle_follower(request.user, username_to_toggle)
		print(is_following)
		print(profile_)
		return redirect(f"/profile/{profile_.user.username}/")


class ProfileDetailView(DetailView):
	# queryset=User.objects.filter(is_active=True)
	# print(queryset)

	template_name = "profiles/user.html"
	def get_object(self):
		username = self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact=username, is_active=True)

	def get_context_data(self, *args, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		user = context['user']
		is_following = False
		if user.profile in self.request.user.is_following.all():
			is_following = True
		context['is_following'] = is_following	
		query = self.request.GET.get('q')
		item_exists = item.objects.filter(user= user).exists()
		qs = GymLocation.objects.filter(owner = user).search(query)
		if item_exists and qs.exists():
			context['location'] = qs  
		return context




