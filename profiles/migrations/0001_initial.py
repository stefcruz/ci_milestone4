# Generated by Django 3.2 on 2021-04-22 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email_address', models.CharField(blank=True, max_length=40, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('creation_date', models.CharField(blank=True, max_length=80, null=True)),
                ('is_superuser', models.CharField(blank=True, max_length=80, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]