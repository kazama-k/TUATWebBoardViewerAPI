# Generated by Django 2.0.3 on 2018-06-08 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180321_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='administrator',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='attach_name',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='attach_url',
            field=models.URLField(blank=True, max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='publisher',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=4096),
        ),
    ]
