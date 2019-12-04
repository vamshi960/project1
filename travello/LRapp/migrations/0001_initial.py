# Generated by Django 2.1.1 on 2019-11-01 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password1', models.CharField(max_length=24)),
                ('password2', models.CharField(max_length=24)),
            ],
        ),
    ]
