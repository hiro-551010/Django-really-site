# Generated by Django 3.1.7 on 2021-03-23 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mysite.user')),
                ('username', models.CharField(default='匿名ユーザー', max_length=30)),
                ('zipcode', models.CharField(default='', max_length=8)),
                ('prefecture', models.CharField(default='', max_length=6)),
                ('city', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
