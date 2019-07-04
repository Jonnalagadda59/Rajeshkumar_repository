# Generated by Django 2.0 on 2019-06-26 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('work_rating', models.BigIntegerField()),
                ('date', models.DateTimeField(max_length=100)),
                ('feedback', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('states', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=1000)),
            ],
        ),
    ]
