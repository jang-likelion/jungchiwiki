# Generated by Django 3.0.6 on 2020-07-30 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedpage', '0002_auto_20200726_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
