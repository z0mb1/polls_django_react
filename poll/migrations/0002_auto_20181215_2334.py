# Generated by Django 2.1.3 on 2018-12-15 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='description',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='description'),
        ),
    ]