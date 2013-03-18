from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#    url(r'^$', 'abbq.views.home', name='home'),
    url(r'^$', TemplateView.as_view(template_name= 'index.html')),
    url(r'^about/', TemplateView.as_view(template_name= 'about.html')),
    url(r'^roster/', TemplateView.as_view(template_name= 'roster.html')),
    url(r'^contact/', TemplateView.as_view(template_name= 'contact.html')),
    url(r'^schedule/', TemplateView.as_view(template_name= 'schedule.html')),
    url(r'^press/', TemplateView.as_view(template_name= 'press.html')),


# url(r'^abbq/', include('abbq.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
