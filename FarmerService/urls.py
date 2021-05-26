"""FarmerService URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',include('accounts.urls',namespace='accounts')),
    path('admin/', include('admin_dashboard.urls', namespace='admin_dashboard')),
    path('crop/', include(('crop.urls','crop'),namespace='crop')),
    path('agri/', include(('agriculture.urls','agriculture'),namespace='agriculture')),
    path('machine/', include(('machine.urls','machine'),namespace='machine')),
    path('marketprice/', include(('marketprice.urls', 'marketprice'), namespace='marketprice')),
    path('farmer/', include(('farmer.urls', 'farmer'), namespace='farmer')),
    path('profile/', include(('user_profile.urls', 'user_profile'), namespace='user_profile')),
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
