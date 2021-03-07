<<<<<<< HEAD
<<<<<<< HEAD
from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(upload_to="music")
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


from allauth.account.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def retrieve_social_data(request, user, **kwargs):
    """Signal, that gets extra data from sociallogin and put it to profile."""
=======
=======
>>>>>>> parent of edf2cf7... wip
from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(upload_to="music")
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

<<<<<<< HEAD

from allauth.account.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def retrieve_social_data(request, user, **kwargs):
    """Signal, that gets extra data from sociallogin and put it to profile."""
>>>>>>> 3c40d1c92f2fe860cd260a8d8e6510aef9f8ee90
    print(user)
=======
>>>>>>> parent of edf2cf7... wip
