# Generated by Django 3.1 on 2020-08-13 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200813_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.CharField(default='22F590E10', help_text='User Id - Primary Key', max_length=9, primary_key=True, serialize=False),
        ),
    ]