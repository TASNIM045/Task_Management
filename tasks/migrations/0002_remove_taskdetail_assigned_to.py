# Generated by Django 5.2.1 on 2025-06-20 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskdetail',
            name='assigned_to',
        ),
    ]
