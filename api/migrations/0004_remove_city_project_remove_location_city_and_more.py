# Generated by Django 5.0.7 on 2024-07-23 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_power_backup_rate_project_power_breakup_rate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='project',
        ),
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='project',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='project',
        ),
        migrations.RemoveField(
            model_name='propertytype',
            name='project',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='project',
        ),
        migrations.RemoveField(
            model_name='subarea',
            name='project',
        ),
        migrations.RemoveField(
            model_name='website',
            name='project',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
        migrations.DeleteModel(
            name='PropertyType',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.DeleteModel(
            name='SubArea',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Website',
        ),
    ]
