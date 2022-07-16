# Generated by Django 4.0.6 on 2022-07-15 15:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Undergraduate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_code', models.IntegerField(help_text='학번', unique=True)),
                ('name', models.CharField(help_text='이름', max_length=16)),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='^[0-9]{3}[0-9]{4}[0-9]{4}$')])),
            ],
            options={
                'ordering': ['student_code'],
            },
        ),
    ]