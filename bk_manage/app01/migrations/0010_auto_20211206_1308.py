# Generated by Django 3.1.7 on 2021-12-06 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_auto_20211206_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bkip',
            name='bk_ip',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bkip',
            name='cron',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.cron'),
        ),
    ]
