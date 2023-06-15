from django.db import models
from django.urls import reverse
from .cohorte import Cohorte


class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)

    DOCUMENT_TYPE_CHOICE = (
        ("CC","Cedula de Ciudadania"),
        ("PPT","Permiso de Protección Temporal"),
        ("CE", "Cedula de Extranjeria"),
        ("TI","Tarjeta de Identidad")
    )
    document_type = models.CharField(max_length=3, choices=DOCUMENT_TYPE_CHOICE, default="CC")
    document_number = models.IntegerField(default=0)
    cohorte = models.ForeignKey(Cohorte, null = True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.fname + " " + self.lname
    
    def get_absolute_url(self):
        return reverse("student-detail", args=[str(self.id)])
    
    