"""icobapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin

class TextFieldView(SingleObjectMixin, View):

    def get(self, request, *args, **kwargs):
        content = "93FC0841CE4F9FA5654829F8469A1B5051A339F58C2D4902017670FEA7730849\ncomodoca.com\nf9121db688f3e83"
        response = HttpResponse(content, content_type='text/plain; charset=utf8')
        response['Content-Disposition'] = 'attachment; filename="49E8AE83E3D85A8C03AFA06A3BADAFB6.txt"'
        return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainapp/', include('mainapp.urls')),
    path('auth/', obtain_auth_token),
    path('.well-known/pki-validation/49E8AE83E3D85A8C03AFA06A3BADAFB6.txt', TextFieldView.as_view())
]
