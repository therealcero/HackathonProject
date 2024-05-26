from django.db import models

class Community(models.Model):
    group_name = models.CharField(max_length=300, unique=True)
    group_icon = models.CharField(max_length=300)
    group_admin = models.CharField(max_length=300)

    
class GroupMember(models.Model):
    groupname = models.CharField(max_length=300)
    username = models.CharField(max_length=300)

class Chats(models.Model):
    groupname = models.CharField(max_length=300, unique=False)
    username = models.CharField(max_length=300, unique=False)
    text = models.CharField(max_length=1000, unique=False, null=False)

class Roadmap(models.Model):
    topic = models.CharField(max_length=300, unique=False)
    link = models.CharField(max_length=300, unique=False)

class Videos(models.Model):
    topic = models.CharField(max_length=300, unique=False)
    embededlink = models.CharField(max_length=800, unique=False)

class Books(models.Model):
    topic = models.CharField(max_length=300, unique=False)
    author = models.CharField(max_length=300, unique=False)
    link = models.CharField(max_length=300, unique=False)

class Course(models.Model):
    topic = models.CharField(max_length=300, unique=False)
    author = models.CharField(max_length=300, unique=False)
    link = models.CharField(max_length=300, unique=False)
