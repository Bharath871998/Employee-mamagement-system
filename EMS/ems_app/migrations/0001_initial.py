# Generated by Django 4.0.2 on 2023-10-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F')], max_length=20)),
                ('joining_date', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=20)),
                ('education', models.CharField(max_length=100)),
            ],
        ),
    ]
