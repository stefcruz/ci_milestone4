# Generated by Django 3.2 on 2021-05-10 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210503_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email_address',
            field=models.EmailField(max_length=60),
        ),
    ]
