# Generated by Django 2.2 on 2019-05-05 21:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Equipo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6178d248-fb2f-44da-a95d-9a75548935b9'), editable=False, primary_key=True, serialize=False),
        ),
    ]
