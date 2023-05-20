# Generated by Django 4.2 on 2023-05-03 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0001_initial'),
        ('courses', '0007_remove_course_eleve'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Enseignant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prof.enseignant'),
        ),
        migrations.AlterField(
            model_name='course',
            name='tag',
            field=models.ManyToManyField(to='courses.tag'),
        ),
    ]
