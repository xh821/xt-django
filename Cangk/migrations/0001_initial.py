# Generated by Django 2.0.4 on 2018-05-18 13:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ckID', models.IntegerField()),
                ('ckname', models.CharField(max_length=30)),
                ('ckperson', models.CharField(max_length=10)),
                ('dz', models.CharField(max_length=200)),
                ('ps1', models.CharField(max_length=100)),
                ('person', models.CharField(max_length=10)),
                ('tel', models.IntegerField()),
                ('ps2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ckd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('djbh', models.IntegerField()),
                ('mddw', models.CharField(max_length=150)),
                ('jsr', models.CharField(max_length=10)),
                ('bm', models.CharField(max_length=20)),
                ('ckck', models.CharField(max_length=100)),
                ('ps1', models.CharField(max_length=100)),
                ('spid', models.IntegerField()),
                ('spname', models.CharField(max_length=50)),
                ('danwei', models.CharField(max_length=10)),
                ('ck', models.CharField(max_length=100)),
                ('num', models.IntegerField()),
                ('ckdj', models.IntegerField()),
                ('ckje', models.IntegerField()),
                ('ps2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='kffp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('di', models.IntegerField()),
                ('spbh', models.IntegerField()),
                ('spmc', models.CharField(max_length=20)),
                ('ck', models.IntegerField(choices=[(1, 'Chengdu'), (2, 'Deyang'), (3, 'Mianyang'), (4, 'Xian')], default=1)),
                ('sl', models.IntegerField()),
                ('je', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='rkd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lzsj', models.DateTimeField(default=django.utils.timezone.now)),
                ('djbh', models.CharField(max_length=30)),
                ('ghdw', models.CharField(max_length=20)),
                ('jsr', models.CharField(max_length=20)),
                ('bm', models.CharField(max_length=100)),
                ('rkck', models.CharField(max_length=20)),
                ('ps1', models.CharField(max_length=50)),
                ('spbh', models.CharField(max_length=100)),
                ('spmc', models.CharField(max_length=100)),
                ('dw', models.CharField(max_length=10)),
                ('sl', models.IntegerField()),
                ('rkdj', models.IntegerField()),
                ('rkje', models.IntegerField()),
                ('ps2', models.CharField(max_length=100)),
            ],
        ),
    ]