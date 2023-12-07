from django.forms import ModelForm
from .models import *
 
class CreateInForum(ModelForm):
    class Meta:
        model= Forum
        fields = "__all__"
 
class CreateInDiscussion(ModelForm):
    class Meta:
        model= Comment
        fields = "__all__"