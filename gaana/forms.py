from django import forms
from django.contrib.auth.models import User
from gaana.models import UserProfile
from gaana.models import Playlist


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    def clean_password(self):
        if self.data['password'] != self.data['confirm_password']:
            raise forms.ValidationError("Passwords are not the same")
        return self.data['password']

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        widgets = {
            'password': forms.PasswordInput(),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', )



class PlaylistForm(forms.ModelForm):
    name = forms.CharField(max_length=128)

    class Meta:
        model = Playlist
        fields = ('name', )


# class PlaylistForm(forms.Form):
#     playlist_name = forms.CharField(label='Create Playlist', max_length=100)