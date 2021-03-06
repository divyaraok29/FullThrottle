# Generated by Django 3.1 on 2020-08-12 13:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeZone',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Timezone Id - Primary Key', primary_key=True, serialize=False)),
                ('time_zone', models.CharField(help_text='Time Zone', max_length=20)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='User Id - Primary Key', primary_key=True, serialize=False)),
                ('first_name', models.CharField(help_text='First name of the user', max_length=20)),
                ('last_name', models.CharField(help_text='Last name of the user', max_length=20)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('activity_id', models.UUIDField(default=uuid.uuid4, help_text='Activity Id - Primary Key', primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(blank=True, help_text='Start time of the activity', null=True)),
                ('end_time', models.DateTimeField(blank=True, help_text='End time of the activity', null=True)),
                ('user_id', models.ForeignKey(help_text='User Id from the Users model', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.users')),
            ],
            options={
                'ordering': ['-start_time', '-end_time'],
            },
        ),
    ]
