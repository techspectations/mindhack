from django.conf.urls import include, url
from django.contrib import admin
from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
from example_app.views import ChatterBotAppView
from example_app.views import myview


urlpatterns = [
    url(r'^$', ChatterBotAppView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/chatterbot/', include(chatterbot_urls, namespace='chatterbot')),
    url(r'^test/',myview ),
    
]

