# Generated by Django 4.1.2 on 2022-10-10 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firsttname', models.CharField(max_length=200)),
                ('lassttname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firsttname', models.CharField(max_length=200)),
                ('lassttname', models.CharField(max_length=200)),
            ],
        ),
    ]