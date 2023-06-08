from django.db import models
from .cohorte import Cohorte


class Student(models.Model):
    name = models.CharField(max_length=50)
    document_type = models.CharField(max_length=30)
    document_number = models.IntegerField(default=0)
    cohorte = models.ForeignKey(Cohorte, null = True, on_delete=models.SET_NULL)
