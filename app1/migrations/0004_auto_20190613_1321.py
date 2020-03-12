# Generated by Django 2.0 on 2019-06-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20190607_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('data', models.DateTimeField(auto_now=True)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UploadFile',
        ),
    ]