# Generated by Django 2.0 on 2018-01-03 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='create_time',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='goodsrecord',
            name='create_time',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='indent',
            name='create_time',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='pricefile',
            name='create_time',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='record',
            name='create_time',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='salesrecord',
            name='create_time',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='temprecord',
            name='create_time',
            field=models.DateTimeField(default=''),
        ),
    ]
