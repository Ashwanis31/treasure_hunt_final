# Generated by Django 3.0.2 on 2020-01-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=20)),
                ('puzz', models.IntegerField()),
                ('attemp', models.IntegerField()),
                ('leader', models.CharField(max_length=100)),
            ],
        ),
    ]
