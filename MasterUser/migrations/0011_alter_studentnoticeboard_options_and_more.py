# Generated by Django 4.1.7 on 2023-05-30 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MasterUser', '0010_alter_events_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentnoticeboard',
            options={'verbose_name_plural': 'StudentNoticeBoard'},
        ),
        migrations.RenameField(
            model_name='studentnoticeboard',
            old_name='newsContent',
            new_name='contents',
        ),
        migrations.RemoveField(
            model_name='studentnoticeboard',
            name='newsActive',
        ),
        migrations.RemoveField(
            model_name='studentnoticeboard',
            name='newsTitle',
        ),
        migrations.RemoveField(
            model_name='studentnoticeboard',
            name='titleImage',
        ),
    ]
