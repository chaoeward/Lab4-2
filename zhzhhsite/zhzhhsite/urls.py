from django.conf.urls import patterns, include, url
from books.views import Show,Delete,Search,Add1,Add,Delete2,Add2,Add3,Delete1,Inform

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zhzhhsite.views.home', name='home'),
    # url(r'^zhzhhsite/', include('zhzhhsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^home/$',Show),
    (r'^delete/$',Delete),
    (r'^search/$',Search),
    (r'^add1/$',Add1),
    (r'^add/$',Add),
    (r'^delete2/$',Delete2),
    (r'^add2/$',Add2),
    (r'^add3/$',Add3),
    (r'^delete1/$',Delete1),
    (r'^inform/$',Inform),
)
