from django.db import models
from django.urls import reverse
from datetime import datetime , date
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class 	Category(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name 

    def get_absolute_url(self):
    	return reverse('blog-home')     


class Post(models.Model):
	title=models.CharField(max_length=255)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	image=models.ImageField(upload_to='images/')
	#body=models.TextField()
	body=RichTextField(blank=True,null=True)
	post_date=models.DateField(auto_now_add=True)
	category=models.CharField(max_length=200,default='Speaking')
	likes=models.ManyToManyField(User,related_name='blog_posts')

	def total_likes(self):
		return self.likes.count()




	def __str__(self):
		return self.title

	def get_absolute_url(self):
		#return reverse('detail',args=(str(self.id)))
		return reverse('blog-home') 	

