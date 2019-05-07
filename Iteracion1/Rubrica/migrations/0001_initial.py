# Generated by Django 2.2 on 2019-05-05 21:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubrica',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rúbrica', models.FileField(upload_to=None)),
                ('duración_Mínima', models.TimeField(default=datetime.datetime(2019, 5, 5, 21, 45, 6, 138169, tzinfo=utc))),
                ('duración_Máxima', models.TimeField(default=datetime.datetime(2019, 5, 5, 21, 45, 6, 138251, tzinfo=utc))),
            ],
        ),
    ]
