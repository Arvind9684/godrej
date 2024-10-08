# Generated by Django 5.0.7 on 2024-07-20 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_projecttable_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='schedulOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('schedule_data', models.CharField(max_length=30)),
                ('schedule_time', models.CharField(max_length=15)),
                ('projectName', models.CharField(max_length=50)),
            ],
        ),
    ]
