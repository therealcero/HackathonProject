# Generated by Django 5.0.6 on 2024-05-26 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_books_course_roadmap_videos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='embededlink',
            field=models.CharField(max_length=800),
        ),
    ]
