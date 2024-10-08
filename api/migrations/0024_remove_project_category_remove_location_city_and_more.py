# Generated by Django 5.0.7 on 2024-08-14 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_location_latitude_alter_location_longitude_and_more'),
        ('myapp', '0032_remove_amenities_project_delete_callback_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
        migrations.RemoveField(
            model_name='project',
            name='city',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='property_type',
        ),
        migrations.RemoveField(
            model_name='project',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='project',
            name='sub_area',
        ),
        migrations.RemoveField(
            model_name='project',
            name='sub_category',
        ),
        migrations.RemoveField(
            model_name='project',
            name='website',
        ),
        migrations.DeleteModel(
            name='APIKey',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
        migrations.DeleteModel(
            name='Picture',
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
            name='SubCategory',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Website',
        ),
    ]
