from django.db import models
from django.conf import settings

class Video(models.Model):
    name = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='uploaded/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


    