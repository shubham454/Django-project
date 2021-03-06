# Generated by Django 2.2.2 on 2020-08-13 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=64)),
                ('tz', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='app.Member')),
            ],
        ),
    ]
