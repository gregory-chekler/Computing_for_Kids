# Generated by Django 3.0.4 on 2020-03-24 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200324_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='blog_pics'),
        ),
    ]
