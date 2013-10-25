import datetime, markdown
from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    is_active = models.BooleanField()
    
    def __unicode__(self):
        return self.post_title
        
    @property
    def post_html(self):
        return markdown.markdown(self.post_text)
        
    class Meta:
        ordering = ['pub_date']


class Image(models.Model):
    post = models.ForeignKey(Post, related_name="images")
    image = models.ImageField(upload_to='Images')
    image_title = models.CharField(max_length=100, blank=True)
