# Generated by Django 3.1.7 on 2021-11-30 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20211130_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cron',
            name='comments',
            field=models.CharField(max_length=200),
        ),
    ]
