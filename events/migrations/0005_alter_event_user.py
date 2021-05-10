# Generated by Django 3.2 on 2021-05-10 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userprofile_email_address'),
        ('events', '0004_alter_event_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='profiles.userprofile'),
        ),
    ]
