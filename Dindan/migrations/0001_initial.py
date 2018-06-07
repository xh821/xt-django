# Generated by Django 2.0.4 on 2018-05-19 01:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='zjdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('djbh', models.CharField(max_length=20)),
                ('dhsj', models.DateTimeField(default=django.utils.timezone.now)),
                ('dhdw', models.CharField(max_length=40)),
                ('spbh', models.CharField(max_length=50)),
                ('spmc', models.CharField(max_length=30)),
                ('sl', models.IntegerField()),
                ('dj', models.IntegerField()),
                ('je', models.IntegerField()),
                ('zdr', models.CharField(max_length=20)),
                ('sh', models.IntegerField(choices=[(1, '已审核'), (0, '未审核')], default=0, verbose_name='审核状态')),
            ],
        ),
    ]
