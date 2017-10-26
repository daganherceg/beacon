"""beacon_landing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.models import User
from signups.models import SignUp
from rest_framework import routers, serializers, viewsets

class SignUpSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = SignUp
    fields = ('first_name', 'last_name', 'email', 'timestamp', 'updated')

class SignUpsViewSet(viewsets.ModelViewSet):
  queryset = SignUp.objects.all()
  serializer_class = SignUpSerializer

router = routers.DefaultRouter()
router.register(r'signups', SignUpsViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
  url(r'^$', 'signups.views.home', name='home'),
	url(r'^thank-you', 'signups.views.thankyou', name='thankyou'),
	url(r'^about-us', 'signups.views.aboutus', name='aboutus'),
  url(r'^profile', 'signups.views.profile', name='profile'),
  url(r'^admin/', admin.site.urls),
  url(r'^accounts/', include('registration.backends.default.urls')),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
