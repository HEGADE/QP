from django.db import models
from datetime import datetime

# Create your models here.

class Question_papers(models.Model):
    provider=models.CharField(max_length=20)
    college = models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    subject= models.CharField(max_length=100)
    examination=models.CharField(max_length=100)
    paper = models.FileField(upload_to='preqps')
    
    def __str__(self):
        return  self.college + ' , ' + self.course +' , '+self.year + ' - '+ self.subject 


class Provider(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    level = models.CharField(max_length=100)
    board=models.CharField(max_length=100)
    claass = models.CharField(max_length=100)
    sem = models.CharField(max_length=100)
    sub= models.CharField(max_length=100)
    papertitle=models.CharField(max_length=100)
    doc = models.FileField(upload_to='provider')
    provide_date=models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return  self.name + ' , ' + self.level +' , '+self.board + ' - '+ self.sub    


class Issues(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    phone=models.DecimalField(max_digits=10 ,decimal_places=0)
    issues=models.TextField()
    isuue_date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return   ' Issues from ' + self.name +' - '+self.email 
