from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Video

def validate_video_file(value):
    import os
    from django.core.exceptions import ValidationError
    from django.utils.translation import gettext_lazy as _

    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Unsupported file extension. Only .mp4, .avi, .mkv, .mov, and .wmv are allowed.'))

class VideoForm(forms.ModelForm):
    video_file = forms.FileField(validators=[validate_video_file])
    
    class Meta:
        model = Video
        fields = ['name', 'video_file']
