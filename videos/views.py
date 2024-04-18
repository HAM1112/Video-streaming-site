from django.shortcuts import render , redirect
from videos.models import Video
from django.conf import settings

import os
# Create your views here.

def deleteVideo(request , video_id):
    print(video_id)
    video = Video.objects.get(id=video_id)
    video_path = os.path.join(settings.MEDIA_ROOT, str(video.video_file))
    
    if os.path.exists(video_path):
        os.remove(video_path)
    
    video.delete()
    return redirect('home')