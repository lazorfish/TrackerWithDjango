# Generated by Django 2.0.2 on 2018-03-27 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DurationTimeEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DateTimeField()),
                ('project', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectnumber', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=200)),
                ('projectyear', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StartStopTimeEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('project', models.ManyToManyField(to='tracker.Project')),
            ],
        ),
    ]