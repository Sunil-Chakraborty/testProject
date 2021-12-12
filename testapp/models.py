from django.db import models
from ckeditor.fields import RichTextField

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField('publication', blank=True)
    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
    
class Student(models.Model):  
    username = models.CharField(max_length=20)  
    first_name = models.CharField("person's first name",max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField("Mobile No.",max_length=10)
    bio = RichTextField("Students history",max_length=500, blank=True)
    tot_marks=models.IntegerField(default=0)  
    email = models.EmailField()  
  
    
    def __str__(self):
        return self.username
    
    
class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.TextField()
        
    
        
    
    