from django.forms import ModelForm

from pragmatic.profileapp.models import Profile



class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']