from django.db import models
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse


# Create your models here.
class Book(models.Model):
    #Title
    title = models.CharField(max_length=50, blank = False)
    #Author
    author = models.CharField(max_length=50)
    #ISBN
    isbn = models.CharField(max_length=50)
    #Course
    course = models.CharField(max_length=50)
    #Professor
    professor = models.CharField(max_length=50)
    #Condition
    condition = models.CharField(max_length=50)
    #Price
    price = models.CharField(max_length=50)

    booker = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.title+" "+self.author+" "+self.isbn+" "+self.course+" "+self.professor
        
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk':self.pk})
    def to_dict(self):
        return {'id': self.id}

