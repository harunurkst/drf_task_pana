from django.db import models


class Divisions(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField()

    def __str__(self):
        return self.name


class Districts(models.Model):
    name = models.CharField(max_length=150)
    division = models.ForeignKey(Divisions)

    def __str__(self):
        return self.name


class Thana(models.Model):
    name = models.CharField(max_length=150)
    districts = models.ForeignKey(Districts)

    def __str__(self):
        return self.name