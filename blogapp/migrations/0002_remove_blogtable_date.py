# Generated by Django 4.0.1 on 2022-01-24 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogtable',
            name='date',
        ),
    ]
