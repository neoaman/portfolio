# Generated by Django 3.1.7 on 2021-04-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket_Credential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(max_length=50)),
                ('client_access_key', models.CharField(max_length=50)),
                ('client_access_secret', models.CharField(max_length=50)),
                ('bucket', models.CharField(max_length=50)),
                ('folder', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MongoCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(max_length=50)),
                ('uri', models.CharField(max_length=200)),
                ('db', models.CharField(max_length=50)),
                ('collection', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
