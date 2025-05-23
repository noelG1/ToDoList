from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField(null=True,blank=True)
    isCompleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering= ['isCompleted']

  