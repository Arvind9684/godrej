# Generated by Django 5.0.7 on 2024-07-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_amenities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenities',
            name='image',
            field=models.ImageField(upload_to='amenities/'),
        ),
    ]
