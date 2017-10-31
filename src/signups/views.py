from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from beacon_landing.urls import UserSerializer

from .models import SignUp
from .forms import SignUpForm

# Create your views here.
def home(request):
	form = SignUpForm(request.POST or None) # sends to server

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'Thank you for joining')
		return HttpResponseRedirect('/thank-you')
	return render_to_response("signup.html",
								locals(),
								context_instance=RequestContext(request))


def thankyou(request):
	form = SignUpForm(request.POST or None) # sends to server
	return render_to_response("thankyou.html",
							locals(),
							context_instance=RequestContext(request))

def aboutus(request):
	# form = SignUpForm(request.POST or None) # sends to server
	return render(request, "aboutus.html", {})


def profile(request):
	# form = SignUpForm(request.POST or None) # sends to server
	if request.user.is_authenticated():
		context = {
			"queryset": SignUp.objects.all()
		}
	return render(request, "profile.html", context)

def quests(request):
	return render_to_response("Quests.html", {'quest':'placeholder'},context_instance=RequestContext(request))

@api_view(['POST'])
def register_user(request):
  s = UserSerializer(data=request.DATA, context={'request': request})
  if s.is_valid():
    User.objects.create_user(s.init_data['email'], s.init_data['username'], s.init_data['password'])
    return Response(s.data, status=status.HTTP_201_CREATED)
  else:
    return Response(s._errors, status=status.HTTP_400_BAD_REQUEST)
