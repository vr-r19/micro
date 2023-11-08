from django.db import models

class Header(models.Model):
    logo = models.ImageField(upload_to='header/')
    login_link = models.URLField()
    menu_image = models.ImageField(upload_to='header/')

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    read_more=models.URLField()
    image = models.ImageField(upload_to='about/')

class Mic(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='mics/')

class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=255)

class Contact(models.Model):
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    facebook = models.URLField()
    social_twitter = models.URLField()
    social_instagram = models.URLField()
