# Generated by Django 2.2.6 on 2019-12-23 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dogowner',
        ),
    ]
