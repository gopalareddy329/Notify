# Generated by Django 4.1.2 on 2022-12-27 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_alter_broadcaste_options_alter_broadcaste_sent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='broadcaste',
            options={'ordering': ['-broadcaste']},
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('uid', models.UUIDField(unique=True, verbose_name=uuid.uuid4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('participents', models.ManyToManyField(blank=True, related_name='participents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
