from django.shortcuts import render , redirect
from videos.models import Video
from django.conf import settings
from django.contrib.auth.models import User
import os
from videos.forms import VideoForm
# Create your views here.

def deleteVideo(request , video_id):
    print(video_id)
    video = Video.objects.get(id=video_id)
    video_path = os.path.join(settings.MEDIA_ROOT, str(video.video_file))
    
    if os.path.exists(video_path):
        os.remove(video_path)
    
    video.delete()
    return redirect('home')


def allVideos(request):
    
    if request.method == "POST":
        selected = request.POST['selected']
        search = request.POST['search']
        user = request.POST['user']
        
        # if category is all give all category 
        if user == "All":
            # serach empty then get all games
            if search == '':
                videos = Video.objects.all()
            
            else : #search with keyword
                videos = Video.objects.filter(name__istartswith=search)
        else:
            if search == '':
                videos = Video.objects.filter(user=user)
            else :
                videos = Video.objects.filter(name__istartswith=search , user=user)
        
        # sorting based on the given option
        if selected == 'latest':
            videos = videos.order_by('-id')
        elif selected == 'oldest':
            videos = videos.order_by('id')
        
            
        #  passing all categories for the select/option
        users = User.objects.order_by('username')
        form = VideoForm()
        context = {
            'form' : form,
            'videos' : videos,
            'selected' : selected,
            'search' : search,
            'users' : users,
            'c_selected' : user,
            'search' : search,
        }
        
        return render(request , 'index.html' , context )
    
    return redirect('home')