# Generated by Django 4.2.7 on 2023-12-20 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_mycart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycart',
            name='quality',
        ),
    ]
