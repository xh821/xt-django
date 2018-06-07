# Generated by Django 2.0.4 on 2018-05-18 13:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cwckd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('djbh', models.CharField(max_length=50)),
                ('fkdw', models.CharField(max_length=30)),
                ('jsr', models.CharField(max_length=20)),
                ('bm', models.CharField(max_length=20)),
                ('fjsm', models.CharField(max_length=200)),
                ('ps1', models.CharField(max_length=200)),
                ('ysje', models.IntegerField()),
                ('yfje', models.IntegerField()),
                ('zhbh', models.CharField(max_length=20)),
                ('zhmc', models.CharField(max_length=20)),
                ('jsfs', models.CharField(max_length=30)),
                ('je', models.IntegerField()),
                ('ps', models.CharField(max_length=100)),
                ('zdr', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='cwrkd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('djbh', models.CharField(max_length=50)),
                ('fkdw', models.CharField(max_length=30)),
                ('jsr', models.CharField(max_length=20)),
                ('bm', models.CharField(max_length=20)),
                ('fjsm', models.CharField(max_length=200)),
                ('ps1', models.CharField(max_length=200)),
                ('ysje', models.IntegerField()),
                ('yfje', models.IntegerField()),
                ('zhbh', models.CharField(max_length=20)),
                ('zhmc', models.CharField(max_length=20)),
                ('jsfs', models.CharField(max_length=30)),
                ('je', models.IntegerField()),
                ('ps', models.CharField(max_length=100)),
                ('zdr', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='jslr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qssj', models.DateTimeField(default=django.utils.timezone.now)),
                ('jssj', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
