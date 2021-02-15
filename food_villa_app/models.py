from django.db import models

# Create your models here.
class Topic(models.Model):
	'''a topic the user is searching about'''
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		'''return a string representation of the model'''
		return self.text

# Create items model here
class Item(models.Model):
	'''Items user are searching or adding'''
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)
	text = models.TextField()
	
	class Meta:
		verbose_name_plural = 'items'
		
	def __str__(self):
		'''Return a string represation of the model'''
		return f'{self.text[:50]}...'
