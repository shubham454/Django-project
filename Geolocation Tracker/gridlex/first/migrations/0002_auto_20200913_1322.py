# Generated by Django 2.2.2 on 2020-09-13 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='latitude',
            field=models.FloatField(blank=True, default=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='places',
            name='longitude',
            field=models.FloatField(blank=True, default=87),
            preserve_default=False,
        ),
    ]
