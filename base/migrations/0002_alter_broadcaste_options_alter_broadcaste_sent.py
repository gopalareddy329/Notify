# Generated by Django 4.1.2 on 2022-12-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='broadcaste',
            options={'ordering': ['broadcaste']},
        ),
        migrations.AlterField(
            model_name='broadcaste',
            name='sent',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]