# Generated by Django 3.1.2 on 2020-10-22 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20201022_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developers',
            name='team',
        ),
    ]