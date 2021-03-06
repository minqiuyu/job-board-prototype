# Generated by Django 3.2.3 on 2021-05-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('contactPhone', models.CharField(max_length=13, verbose_name='Contact Phone')),
                ('contactEmail', models.EmailField(max_length=20, verbose_name='Contact Email')),
                ('description', models.CharField(max_length=750, verbose_name='Description')),
                ('posterName', models.CharField(max_length=25, verbose_name='Poster Name')),
                ('postingDate', models.DateField(auto_now_add=True, verbose_name='Posting Date')),
            ],
        ),
    ]
