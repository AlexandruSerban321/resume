from django.db import models

class Experience(models.Model):
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    details = models.CharField(max_length=200)

    def __str__(self):
        return self.company


class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    details = models.CharField(max_length=200)

    def __str__(self):
        return self.school


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()

    def __str__(self):
        return self.name

class Strenght(models.Model):
    strenght =  models.CharField(max_length=100)

    def __str__(self):
        return self.strenght