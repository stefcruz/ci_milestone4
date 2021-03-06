# Generated by Django 3.2 on 2021-05-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_events_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_category',
            field=models.CharField(choices=[('Arts', 'Arts'), ('Food & Drinks', 'Food & Drinks'), ('Fitness & Sports', 'Fitness & Sports'), ('Kids', 'Kids'), ('Services', 'Services'), ('Other', 'Other')], default='Arts', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(null=True),
        ),
    ]
