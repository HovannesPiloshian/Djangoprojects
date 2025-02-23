# Generated by Django 5.0.7 on 2024-07-17 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30, verbose_name='Electronic brand')),
                ('name', models.CharField(max_length=40, verbose_name='Electronic name')),
                ('price', models.PositiveIntegerField(verbose_name='Electronic price')),
                ('discount_price', models.PositiveIntegerField(verbose_name='Electronic discount price')),
                ('description', models.TextField(verbose_name='Electronic description')),
                ('image', models.ImageField(upload_to='products', verbose_name='Electronic image')),
                ('date', models.DateTimeField(auto_now=True)),
                ('color', models.CharField(choices=[('red', 'red'), ('blue', 'blue'), ('black', 'black'), ('white', 'white')], max_length=60)),
            ],
        ),
    ]
