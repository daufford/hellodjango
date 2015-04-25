from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #three arguments for url:  regex, view, kwargs, name
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls"))  #if in the polls directory, look at the poll specific URL list
]
