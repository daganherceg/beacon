from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages

from .models import User
from .forms import UserProfileRegistrationForm

# Navbar Sign in
def home(request):
	form = UserProfileRegistrationForm(request.POST or None) # sends to server

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'Thank you for joining')
		return HttpResponseRedirect('/thank-you')
	return render_to_response("signup.html", 
								locals(), 
								context_instance=RequestContext(request))


def thankyou(request):
	form = UserProfileRegistrationForm(request.POST or None) # sends to server
	return render_to_response("thankyou.html", 
							locals(), 
							context_instance=RequestContext(request))

def aboutus(request):
	# form = UserProfileRegistrationForm(request.POST or None) # sends to server
	return render(request, "aboutus.html", {})


def profile(request):
	# form = UserProfileRegistrationForm(request.POST or None) # sends to server
	if request.user.is_authenticated():
		context = {
			"queryset": User.objects.all()
		}
	return render(request, "profile.html", context)

@api_view(['POST'])
def register_user(request):
  s = UserSerializer(data=request.DATA, context={'request': request})
  if s.is_valid():
    User.objects.create_user(s.init_data['email'], s.init_data['username'], s.init_data['password'])
    return Response(s.data, status=status.HTTP_201_CREATED)
  else:
    return Response(s._errors, status=status.HTTP_400_BAD_REQUEST)
