# Generated by Django 5.1.2 on 2024-10-19 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='senha',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='usuario',
            new_name='username',
        ),
    ]
