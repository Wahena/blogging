import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    is_active = models.BooleanField()
    
    def __unicode__(self):
        return self.post_title   
        
    
class Image(models.Model):
    post = models.ForeignKey(Post, related_name="images")
    image = models.ImageField(upload_to='Images')
    image_title = models.CharField(max_length=100, blank=True)
