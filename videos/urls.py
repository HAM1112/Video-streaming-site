from django.urls import path
from . import views


urlpatterns = [
    path('delete/<int:video_id>' , views.deleteVideo , name='delete-video'),
    path('allvideos/' , views.allVideos , name='all-videos'),
]
