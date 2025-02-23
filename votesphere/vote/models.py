from django.db import models
from django.contrib.auth.models import User

class ElectionOfficer(models.Model):
    id_number = models.CharField(max_length=20, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    fullname = models.CharField(max_length=100)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return self.fullname

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Vote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One user can vote once
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} voted for {self.candidate.name}"
