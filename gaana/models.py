from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


class Artist(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name



class Song(models.Model):
    artist = models.ManyToManyField(Artist)
    track = models.CharField(max_length=128, blank=True)
    album = models.CharField(max_length=128, blank=True)
    release_year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.datetime.now().year)])
    release_label = models.CharField(max_length=128)
    genre = models.CharField(max_length=128, blank=True)


    def __unicode__(self):
        return self.release_label


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_image', blank=True)

    def __unicode__(self):
        return self.user.username


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True)
    song = models.ForeignKey(Song, null=True)

    def __unicode__(self):
        return self.name


class Like(models.Model):
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User)
    song = models.ForeignKey(Song)

    def __unicode__(self):
        return self.likes