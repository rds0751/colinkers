"""
Definition of urls for CoLinkers.
"""

from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from CoLinkers.core import views as views_core

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', views_core.home, name='home'),
    url(r'^about/', views_core.about, name='about'),
    url(r'^events/', views_core.events, name='events'),
    url(r'^gallery/', views_core.gallery, name='gallery'),
    url(r'^contact/', views_core.contact, name='contact'),
    url(r'^login/', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'template_name': 'core/logout.html'}, name='logout'),
	url(r'^signup/$', views_core.signup, name='signup'),
    # url(r'^CoLinkers/', include('CoLinkers.CoLinkers.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
