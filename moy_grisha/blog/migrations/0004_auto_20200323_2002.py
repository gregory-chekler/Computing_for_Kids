# Generated by Django 3.0.4 on 2020-03-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200323_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='', upload_to='blog_pics'),
        ),
    ]