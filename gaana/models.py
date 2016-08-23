from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Artist(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name



class Song(models.Model):
    artist = models.ForeignKey(Artist)
    track = models.CharField(max_length=128, blank=True)
    album = models.CharField(max_length=128, blank=True)
    release_year = models.DateTimeField()
    release_label = models.CharField(max_length=128)
    genre = models.CharField(max_length=128, blank=True)


    # def get_year(self):
    #     return self.release_year.year

    def __unicode__(self):
        return self.release_label



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_image', blank=True)

    def __unicode__(self):
        return self.user.username