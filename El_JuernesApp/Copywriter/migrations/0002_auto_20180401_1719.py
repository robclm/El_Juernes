# Generated by Django 2.0.3 on 2018-04-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Copywriter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='priority',
            field=models.CharField(default='', max_length=140),
        ),
    ]