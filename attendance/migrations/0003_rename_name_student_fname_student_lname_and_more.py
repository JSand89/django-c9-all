# Generated by Django 4.2.2 on 2023-06-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_cohorte_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='student',
            name='lname',
            field=models.CharField(default='Doe', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='document_type',
            field=models.CharField(choices=[('CC', 'Cedula de Ciudadania'), ('PPT', 'Permiso de Protección Temporal'), ('CE', 'Cedula de Extranjeria'), ('TI', 'Tarjeta de Identidad')], default='CC', max_length=3),
        ),
    ]
