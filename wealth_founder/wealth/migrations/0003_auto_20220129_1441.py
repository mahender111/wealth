# Generated by Django 3.1 on 2022-01-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wealth', '0002_auto_20220129_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_superuser',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
