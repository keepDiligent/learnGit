from django.db import models

# Create your models here
class Article(models.Model):
 title = models.CharField(max_length=50)
 publish_time = models.DateTimeField(auto_now_add=True)
 content = models.TextField()

 class Meta:
 	ordering = ['-publish_time']

 def __unicode__(self):
  return self.title
