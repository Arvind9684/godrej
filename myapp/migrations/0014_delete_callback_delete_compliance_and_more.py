# Generated by Django 5.0.7 on 2024-07-24 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_demoproject'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Callback',
        ),
        migrations.DeleteModel(
            name='compliance',
        ),
        migrations.RemoveField(
            model_name='demoproject',
            name='project_ptr',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='projectEnquary',
        ),
        migrations.DeleteModel(
            name='projectTable',
        ),
        migrations.DeleteModel(
            name='schedulOn',
        ),
        migrations.DeleteModel(
            name='shareholderPattern',
        ),
        migrations.DeleteModel(
            name='demoProject',
        ),
    ]
