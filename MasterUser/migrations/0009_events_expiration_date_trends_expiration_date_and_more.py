# Generated by Django 4.1.7 on 2023-05-30 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterUser', '0008_events_trends'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='expiration_date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='trends',
            name='expiration_date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='expiration_date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='newupdates',
            name='expiration_date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='studentnoticeboard',
            name='expiration_date',
            field=models.CharField(default='', max_length=100),
        ),
    ]
