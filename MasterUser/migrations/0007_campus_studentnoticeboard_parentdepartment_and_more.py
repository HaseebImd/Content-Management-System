# Generated by Django 4.1.7 on 2023-05-29 18:19

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterUser', '0006_newupdates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campusName', models.CharField(max_length=200, unique=True)),
                ('createdat', models.DateTimeField(auto_now_add=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(auto_now=True, db_column='updatedAt', null=True)),
            ],
            options={
                'verbose_name_plural': 'Campus',
            },
        ),
        migrations.CreateModel(
            name='StudentNoticeBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsTitle', models.CharField(max_length=200)),
                ('newsContent', tinymce.models.HTMLField()),
                ('newsActive', models.BooleanField(default=True)),
                ('titleImage', models.ImageField(upload_to='upload/newupdates/')),
                ('createdat', models.DateTimeField(auto_now_add=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(auto_now=True, db_column='updatedAt', null=True)),
                ('expiration_date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'NewsUpdates',
            },
        ),
        migrations.CreateModel(
            name='ParentDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentName', models.CharField(max_length=200, unique=True)),
                ('departmentShortName', models.CharField(max_length=200, unique=True)),
                ('createdat', models.DateTimeField(auto_now_add=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(auto_now=True, db_column='updatedAt', null=True)),
                ('campusId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterUser.campus')),
            ],
            options={
                'verbose_name_plural': 'ParentDepartment',
            },
        ),
        migrations.CreateModel(
            name='ChildDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentName', models.CharField(max_length=200, unique=True)),
                ('departmentShortName', models.CharField(max_length=200, unique=True)),
                ('createdat', models.DateTimeField(auto_now_add=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(auto_now=True, db_column='updatedAt', null=True)),
                ('parentDepartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterUser.parentdepartment')),
            ],
            options={
                'verbose_name_plural': 'ChildDepartment',
            },
        ),
    ]
