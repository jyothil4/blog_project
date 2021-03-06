from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',related_name='blog_post')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date= timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments')
    name = models.ForeignKey('auth.User',related_name='blog_comment')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('-created_date',)

    def get_absolute_url(self):
        return reverse('post_detail')

    def __str__(self):
        return self.text
