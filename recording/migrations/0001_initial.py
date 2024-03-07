# Generated by Django 4.2.7 on 2024-03-07 16:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('participant', models.CharField(max_length=128)),
                ('host', models.CharField(max_length=128)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('expiration', models.DateTimeField()),
            ],
        ),
    ]
