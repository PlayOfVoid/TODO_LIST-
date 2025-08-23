from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=1000,blank=True,null=True)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'task'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('create_at',)
