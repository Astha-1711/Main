from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class Advocate(models.Model):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=100)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.username

