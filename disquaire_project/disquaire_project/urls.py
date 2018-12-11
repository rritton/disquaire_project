"""
Definition of urls for disquaire_project.
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from store import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', disquaire_project.views.home, name='home'),
    # url(r'^disquaire_project/', include('disquaire_project.disquaire_project.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', views.index),
    url(r'^store/', include('store.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

#if settings.DEBUG:
 #   import debug_toolbar
  #  urlpatterns = [
   #     url(r'^__debug__/', include(debug_toolbar.urls))
    #] + urlpatterns
