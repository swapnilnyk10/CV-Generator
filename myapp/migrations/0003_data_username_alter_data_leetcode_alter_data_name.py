# Generated by Django 4.0.5 on 2022-06-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_data_leetcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='username',
            field=models.CharField(default='X', max_length=20),
        ),
        migrations.AlterField(
            model_name='data',
            name='leetcode',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='data',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
