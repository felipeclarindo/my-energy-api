# Generated by Django 5.1.3 on 2024-12-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
