# Generated by Django 4.0.5 on 2022-10-31 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=255)),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phoneno', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=255)),
                ('type', models.CharField(default='C', max_length=2)),
            ],
        ),
    ]
