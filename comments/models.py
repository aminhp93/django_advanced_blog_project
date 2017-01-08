from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


from posts.models import Post
# Create your models here.

class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	# post = models.ForeignKey(Post)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return str(self.user.username)