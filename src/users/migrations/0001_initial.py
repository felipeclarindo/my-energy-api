# Generated by Django 5.1.3 on 2024-11-16 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=11)),
                ('login', models.CharField(max_length=70)),
                ('senha', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=125)),
            ],
        ),
    ]
