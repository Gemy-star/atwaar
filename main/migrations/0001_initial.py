# Generated by Django 3.2.4 on 2021-06-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email Address')),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='Phone')),
            ],
        ),
    ]
