# Generated by Django 3.0.6 on 2020-08-01 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedpage', '0017_auto_20200801_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='electedCount',
            field=models.CharField(blank=True, choices=[('초선', '초선'), ('재선', '재선'), ('3선', '3선'), ('4선', '4선'), ('5선', '5선'), ('6선', '6선'), ('7선', '7선'), ('8선', '8선'), ('9선', '9선'), ('10선', '10선')], max_length=10),
        ),
        migrations.AlterField(
            model_name='politician',
            name='politicalCommittee',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
