# Generated by Django 2.0.4 on 2018-05-18 13:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spmc', models.CharField(max_length=20)),
                ('spbh', models.CharField(max_length=20)),
                ('pp', models.CharField(max_length=20)),
                ('gg', models.CharField(max_length=120)),
                ('xh', models.CharField(max_length=50)),
                ('zl', models.IntegerField()),
                ('scsj', models.DateTimeField(default=django.utils.timezone.now)),
                ('bzq', models.DateTimeField(default=django.utils.timezone.now)),
                ('bxsj', models.CharField(max_length=20)),
                ('ghxx', models.CharField(max_length=200)),
                ('ckcb', models.IntegerField()),
                ('ps', models.CharField(max_length=100)),
                ('dwmc', models.CharField(max_length=100)),
                ('dwdm', models.CharField(max_length=50)),
                ('tm', models.IntegerField()),
                ('lsj', models.IntegerField()),
                ('y1', models.IntegerField()),
                ('y2', models.IntegerField()),
                ('y3', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='addspimg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgf', models.ImageField(upload_to='upload')),
                ('name1', models.CharField(default='前面', max_length=10)),
                ('imgb', models.ImageField(upload_to='upload')),
                ('name2', models.CharField(default='后面', max_length=10)),
                ('imgl', models.ImageField(upload_to='upload')),
                ('name3', models.CharField(default='左面', max_length=10)),
                ('imgr', models.ImageField(upload_to='upload')),
                ('name4', models.CharField(default='右面', max_length=10)),
                ('imgu', models.ImageField(upload_to='upload')),
                ('name5', models.CharField(default='上面', max_length=10)),
                ('imgd', models.ImageField(upload_to='upload')),
                ('name6', models.CharField(default='底面', max_length=10)),
                ('status', models.IntegerField(choices=[(0, '进行中'), (1, '已完成')], default=0, verbose_name='状态')),
            ],
        ),
    ]
