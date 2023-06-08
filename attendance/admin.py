from django.contrib import admin

# Register your models here.

from .models.cohorte import Cohorte
from .models.students import Student


admin.site.register(Cohorte)
admin.site.register(Student)