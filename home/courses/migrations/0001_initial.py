# Generated by Django 4.2 on 2023-05-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('datecreation', models.DateTimeField(auto_now=True)),
                ('avis', models.IntegerField(null=True)),
                ('cover', models.ImageField(null=True, upload_to='CourseCovers/img/%y/')),
                ('video', models.FileField(null=True, upload_to='CourseVideos/lecons/%y')),
                ('tag', models.ManyToManyField(null=True, to='courses.tag')),
            ],
        ),
    ]
