# Generated by Django 3.1 on 2020-08-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveller',
            name='createddate',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traveller',
            name='logindate',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='traveller',
            name='password',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
