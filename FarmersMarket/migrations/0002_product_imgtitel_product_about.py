# Generated by Django 4.1.2 on 2023-04-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarmersMarket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ImgTitel',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='about',
            field=models.CharField(default='', max_length=150),
        ),
    ]
