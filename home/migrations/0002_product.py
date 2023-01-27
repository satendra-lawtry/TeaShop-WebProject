# Generated by Django 4.1 on 2023-01-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pimage', models.ImageField(upload_to='Product_image')),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
