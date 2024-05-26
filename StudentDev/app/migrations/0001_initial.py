# Generated by Django 5.0.6 on 2024-05-25 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=300, unique=True)),
                ('group_icon', models.CharField(max_length=300)),
                ('group_admin', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=300)),
            ],
        ),
    ]
