# Generated by Django 5.1.3 on 2024-12-14 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_users_created_at_remove_users_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='senha',
            new_name='password',
        ),
    ]
