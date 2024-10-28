# Generated by Django 4.2.7 on 2023-12-04 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_delete_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='imges/products')),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('features', models.CharField(max_length=1000)),
                ('discount', models.IntegerField()),
                ('category', models.CharField(choices=[('f', 'fashion & beauty'), ('k', 'kids & Babies clotheS'), ('m', 'men & woman clothes'), ('u', 'underwire clothes'), ('a', 'all items')], default='l', max_length=100)),
            ],
        ),
    ]