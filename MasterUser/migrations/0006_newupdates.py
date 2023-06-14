# Generated by Django 4.1.7 on 2023-05-25 19:33

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterUser', '0005_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewUpdates',
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
    ]
