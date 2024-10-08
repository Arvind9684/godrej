# Generated by Django 4.1.13 on 2024-07-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_projectenquary'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('price', models.BigIntegerField()),
                ('locality', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=25)),
                ('topology', models.CharField(max_length=50)),
                ('aboutus', models.CharField(max_length=1000)),
                ('langt', models.CharField(max_length=50, null=True)),
                ('lat', models.CharField(max_length=50, null=True)),
                ('location', models.CharField(max_length=250)),
                ('project_type', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('posassion_date', models.DateField(auto_now=True)),
                ('neighbourhood', models.CharField(max_length=50)),
                ('master_plan', models.FileField(upload_to='master_plans/')),
                ('unit_plan', models.FileField(upload_to='unit_plans/')),
                ('amenties', models.CharField(max_length=500)),
                ('image', models.FileField(upload_to='project_image/')),
                ('image2', models.FileField(null=True, upload_to='project_image2/')),
                ('image3', models.FileField(null=True, upload_to='project_image3/')),
                ('image4', models.FileField(null=True, upload_to='project_image4/')),
            ],
        ),
    ]
