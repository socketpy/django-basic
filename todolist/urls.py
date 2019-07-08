from django.conf.urls import url
from django.urls import path

#import 'views.py' from crrently directory (import from same directory)
from . import views


urlpatterns = [

    # running function called 'index' in views.py file
    path('', views.index, name='index'),
    path('count/', views.count, name='count'),
    path('eggs/', views.eggs, name='EggS'),
    path('about/', views.about, name='about')
]

