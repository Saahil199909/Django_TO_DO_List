from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    def __str__(self):
        return self.username


class Task(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    status = models.IntegerField()

    def __str__(self):
        # return self.task_name,self.id
         return f"{self.task_name} (ID: {self.id})"
