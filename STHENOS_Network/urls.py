from django.urls import include, path
from . import views


urlpatterns = [   
    path("", views.network, name="network"),   
    path("profile/<str:username>", views.profile_view, name="profile"),     
    path("like", views.like, name="like"),
    path("profile/like", views.like, name="like"),
    path("following", views.following, name="following"),
    path("follow", views.follow, name="follow"),
    path("edit", views.edit, name="edit"),
    path("archive", views.archive, name="archive"),
    
    path("emails", views.compose, name="compose"),


    path("<str:mailbox>", views.mailbox, name="mailbox"),  #always in last because it will override whats after because of his flexibility
]
