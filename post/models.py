from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.slug
    
    def get_absolute_url(self):
        return reverse('post:post_detail', args=[self.id, self.slug])
    

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    is_reply = models.BooleanField(default=False)
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='reply_comments', null=True, blank=True)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.body)<=30:
            return f'{self.user} - {self.body}'
        return f'{self.user} - {self.body[30]}'