# Generated by Django 3.2 on 2021-05-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_category',
            field=models.CharField(choices=[('arts', 'Arts'), ('food-and-drinks', 'Food & Drinks'), ('fitness-and-sports', 'Fitness & Sports'), ('kids', 'Kids'), ('services', 'Services'), ('other', 'Other')], default='Arts', max_length=100),
        ),
    ]
