# Generated by Django 5.0.6 on 2024-06-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=40)),
                ('course_name', models.CharField(max_length=255)),
                ('course_credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_usn', models.IntegerField()),
                ('student_name', models.CharField(max_length=255)),
                ('student_sem', models.IntegerField()),
                ('enrolment', models.ManyToManyField(to='app1.course')),
            ],
        ),
    ]
