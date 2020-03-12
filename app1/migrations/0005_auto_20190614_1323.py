# Generated by Django 2.0 on 2019-06-14 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20190613_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, default='无', max_length=68, null=True)),
                ('address', models.CharField(blank=True, default='无', max_length=256, null=True)),
                ('data', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, default='无', max_length=68, null=True)),
                ('address', models.CharField(blank=True, default='无', max_length=256, null=True)),
                ('message', models.TextField(blank=True, default='无', null=True)),
                ('file_name', models.CharField(blank=True, default='无', max_length=128, null=True)),
                ('data', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.RemoveField(
            model_name='loginuser',
            name='time',
        ),
        migrations.AddField(
            model_name='loginuser',
            name='ip',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='address',
            field=models.CharField(blank=True, default='无', max_length=256, null=True),
        ),
    ]
