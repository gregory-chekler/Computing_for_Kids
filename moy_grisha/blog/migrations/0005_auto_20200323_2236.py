# Generated by Django 3.0.4 on 2020-03-23 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200323_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='picture',
            new_name='image',
        ),
    ]