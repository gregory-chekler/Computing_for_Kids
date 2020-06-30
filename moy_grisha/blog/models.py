from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from embed_video.fields import EmbedVideoField


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(default='', upload_to='blog_pics', blank=True, null=True)
	video = EmbedVideoField(default='', blank=True)


	def __str__(self):
		return f'{self.title} Post'

	# def get_absolute_url(self, *args, **kwargs):
	# 	super().save(*args, **kwargs)
	#
	# 	img = Image.open(self.image)
	# 	if img.height > 600 or img.width > 600:
	# 		output_size = (600, 600)
	# 		img.thumbnail(output_size)
	# 		img.save(self.image.name)
	# 	return reverse('post-detail', kwargs={'pk': self.pk})
