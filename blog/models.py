from django.db import models
from account.models import User

class Article(models.Model):
	author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
	title = models.CharField(max_length=1000)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.title} | {self.author.get_full_name()}"

