# Generated by Django 4.0.5 on 2022-06-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='', max_length=60)),
                ('Course_Number', models.IntegerField()),
                ('Instructor_Name', models.CharField(default='', max_length=60)),
                ('Duration', models.FloatField()),
            ],
        ),
    ]
