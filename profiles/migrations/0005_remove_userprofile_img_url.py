# Generated by Django 3.2 on 2021-05-12 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userprofile_email_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='img_url',
        ),
    ]
