# Generated by Django 3.0.7 on 2020-06-28 05:23

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='blog_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, default=''),
        ),
    ]
