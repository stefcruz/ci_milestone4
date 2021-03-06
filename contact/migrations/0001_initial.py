# Generated by Django 3.2 on 2021-05-29 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_category', models.CharField(choices=[('general_query', 'General Query'), ('event_issue', 'Event issue'), ('profile_issue', 'Profile issue'), ('payment_issue', 'Payment issue')], default='general_query', max_length=100)),
                ('contact_name', models.CharField(max_length=80)),
                ('contact_email', models.CharField(blank=True, max_length=80, null=True)),
                ('message', models.CharField(max_length=1500)),
                ('is_resolved', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
