# Generated by Django 3.1.3 on 2020-11-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_framework_tracking', '0010_auto_20200609_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='apirequestlog',
            name='request_city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='apirequestlog',
            name='request_country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
