# Generated by Django 4.2.7 on 2024-01-18 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_passwordreset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycart',
            name='products',
        ),
        migrations.DeleteModel(
            name='products',
        ),
    ]