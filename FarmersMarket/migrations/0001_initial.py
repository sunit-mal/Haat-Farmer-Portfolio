# Generated by Django 4.1.2 on 2023-04-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productImg', models.ImageField(upload_to='Media')),
                ('userName', models.CharField(max_length=20)),
            ],
        ),
    ]
