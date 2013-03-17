from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#    url(r'^$', 'abbq.views.home', name='home'),
    url(r'^$', direct_to_template, {'template': 'index.html'}),
    url(r'^about/', direct_to_template, {'template': 'about.html'}),
    url(r'^roster/', direct_to_template, {'template': 'roster.html'}),
    url(r'^contact/', direct_to_template, {'template': 'contact.html'}),
    url(r'^schedule/', direct_to_template, {'template': 'schedule.html'}),
    url(r'^press/', direct_to_template, {'template': 'press.html'}),


# url(r'^abbq/', include('abbq.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
