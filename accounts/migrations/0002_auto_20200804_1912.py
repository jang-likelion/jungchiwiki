# Generated by Django 3.0.8 on 2020-08-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', '남성'), ('F', '여성')], max_length=1),
        ),
    ]
