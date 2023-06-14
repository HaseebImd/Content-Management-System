# Generated by Django 4.1.7 on 2023-05-25 18:52

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterUser', '0004_remove_menu_menulink_delete_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobTitle', models.CharField(max_length=200)),
                ('jobDescription', tinymce.models.HTMLField()),
                ('jobActive', models.BooleanField(default=True)),
                ('createdat', models.DateTimeField(auto_now_add=True, db_column='createdAt', null=True)),
                ('updatedat', models.DateTimeField(auto_now=True, db_column='updatedAt', null=True)),
                ('expiration_date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]
