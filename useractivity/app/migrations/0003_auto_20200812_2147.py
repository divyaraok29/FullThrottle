# Generated by Django 3.1 on 2020-08-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200812_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.CharField(default='CF5A4F893', help_text='User Id - Primary Key', max_length=9, primary_key=True, serialize=False),
        ),
    ]
