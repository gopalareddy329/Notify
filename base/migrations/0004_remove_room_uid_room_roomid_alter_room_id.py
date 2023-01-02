# Generated by Django 4.1.2 on 2022-12-27 12:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_broadcaste_options_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='uid',
        ),
        migrations.AddField(
            model_name='room',
            name='roomid',
            field=models.CharField(default=uuid.uuid4, max_length=50),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]