from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment_text = models.TextField()
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    post =""
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} commented '{self.comment_text}'"
    
