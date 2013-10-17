import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    blog_text = models.CharField(max_length = 400)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.blog_text
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently?'
    
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    comment_text = models.CharField(max_length = 200)
    likes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.comment_text
