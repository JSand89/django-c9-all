from django.db import models


class Cohorte(models.Model):
    name = models.CharField(max_length=50)
    group_director = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    number_students_initial = models.IntegerField(default=0)
    number = models.IntegerField(default=9)

    def __str__(self):
        return " El Nombre de la Cohorte es: " + self.name + ". El numero de cohorte es: " + str(self.number)