from django.db import models

# Create your models here.

class Teams(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)

    def __str__(self):
        return f"Name : {self.name}, Location : {self.location}"

class Developers(models.Model):
    name = models.CharField(max_length = 50)
    skills = models.CharField(max_length = 200)
    team = models.ForeignKey(Teams, on_delete = models.CASCADE, default = 0)

    def __str__(self):
        return f"Name : {self.name}, Skills : {self.skills}, Team : {self.team}"

