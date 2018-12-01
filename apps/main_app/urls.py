from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('home', views.home),

    path('users/<id>', views.user),

    path('trail/<id>/addtrip', views.addtrip),
    path('trail/<id>/addreview', views.addreview),
    path('trail/<id>', views.trail),

    path('process', views.process),
    path('mytrip',views.mytrip),
    path('trip', views.trip),
    path('trip/<id>/edit', views.tripedit),
    path('trip/<id>', views.tripshow),
    path('jointrip/<id>', views.jointrip),
    path('addpic/<id>', views.addpic),

    path('admin', views.admin),
    path('admin/findemergency', views.emergency),
    path('admin/deleteuser', views.deleteuser),

    path('oauth', views.oauth),
    path('oauth/return', views.oauthprocess),

    path('donation', views.donation),
    path('donation/process', views.processdono)
]