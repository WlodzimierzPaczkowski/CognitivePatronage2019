# Generated by Django 2.1.5 on 2019-01-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dblearning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worked', models.FloatField()),
                ('salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='dbpred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worked', models.FloatField()),
                ('salary', models.FloatField()),
            ],
        ),
    ]
