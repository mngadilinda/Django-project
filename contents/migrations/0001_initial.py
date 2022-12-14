# Generated by Django 4.1.2 on 2022-10-09 10:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('overview', models.TextField(blank=True)),
                ('lesson_id', models.AutoField(primary_key=True, serialize=False)),
                ('textual_lesson', ckeditor.fields.RichTextField(blank=True)),
                ('less_images', models.FileField(upload_to='lesson/images')),
                ('less_video', models.FileField(upload_to='leeson/videos/')),
                ('less_notes', models.FileField(upload_to='lesson/notes/')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('module_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('program_id', models.AutoField(primary_key=True, serialize=False)),
                ('program_img', models.FileField(upload_to='program/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Tests_Exams',
            fields=[
                ('title', models.CharField(max_length=300)),
                ('overview', ckeditor.fields.RichTextField(blank=True)),
                ('test_ex_id', models.AutoField(primary_key=True, serialize=False)),
                ('lessons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.lesson')),
                ('modules', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.module')),
                ('programs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.program')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='contents.program'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='contents.module'),
        ),
    ]
