# Generated by Django 2.2 on 2019-05-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiante', '0003_auto_20190502_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='Nombre',
            field=models.CharField(default='algo', max_length=50),
        ),
    ]
