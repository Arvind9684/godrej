# Generated by Django 4.1.13 on 2024-07-19 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_compliance_comp_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectEnquary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('cityName', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('projectName', models.CharField(max_length=50)),
            ],
        ),
    ]
