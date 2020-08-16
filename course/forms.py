from django import forms
from .models import Post ,Category

choices=Category.objects.all().values_list('name','name')
choices_list=[]
for item in choices:
	choices_list.append(item)
	
class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('title','author','image','body')

		widgets={
		'title':forms.TextInput(attrs={'class':'form-control'}),
		#'author':forms.TextInput(attrs={'class':'form-control','value:':'','id':'name_id','type':'hidden'}),
		#'author':forms.Select(attrs={'class':'form-control'}),
		'author':forms.TextInput(attrs={'class':'form-control','value:':'','id':'name_id','type':'hidden'}),
		#'category':forms.Select(choices=choices_list,attrs={'class':'form-control'}),
		'body':forms.Textarea(attrs={'class':'form-control'}),
		}

	
class EditForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('title','image','body')

		widgets={
		'title':forms.TextInput(attrs={'class':'form-control'}),
		'body':forms.Textarea(attrs={'class':'form-control'}),
		
		}		