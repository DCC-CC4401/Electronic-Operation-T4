# Generated by Django 2.2 on 2019-05-05 21:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Rubrica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubrica',
            name='duración_Máxima',
            field=models.TimeField(default=datetime.datetime(2019, 5, 5, 21, 56, 17, 612038, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rubrica',
            name='duración_Mínima',
            field=models.TimeField(default=datetime.datetime(2019, 5, 5, 21, 56, 17, 612020, tzinfo=utc)),
        ),
    ]
