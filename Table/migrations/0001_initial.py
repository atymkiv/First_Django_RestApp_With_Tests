# Generated by Django 2.1.2 on 2018-10-30 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('midName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('rate', models.FloatField()),
            ],
        ),
    ]
