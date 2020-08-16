from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView ,DetailView ,CreateView, UpdateView ,DeleteView
from django.urls import reverse_lazy,reverse
from .models import Post,Category
from .forms import PostForm ,EditForm
from django.http import HttpResponseRedirect


def LikeView(request,pk):
	post=get_object_or_404(Post,id=request.POST.get('post_id'))
	liked=False

	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked=False
	else:
		post.likes.add(request.user)
		liked=True
	return HttpResponseRedirect(reverse('detail',args=[str(pk)]))


def CatergoryView(request,cats):
	category_posts=Post.objects.filter(category=cats.replace('-',' '))
	return render(request,'course/catergorie.html',{'cats':cats.title().replace('-',' '),'category_posts':category_posts})

class AddCategeroyView(CreateView):
	model=Category
	#form_class=PostForm
	template_name='course/add_categeroy.html'
	fields=('__all__')


class AddPostView(CreateView):
	model=Post
	form_class=PostForm
	template_name='course/create_post.html'
	#fields='__all__'

class UpdatePostView(UpdateView):
	model=Post
	form_class=EditForm
	template_name='course/update_post.html'
	#fields=['title','image','body']

class DeletePostView(DeleteView):
	model=Post
	template_name='course/delete_post.html'
	success_url=reverse_lazy('blog-home')





class BlogHome(ListView):
	model=Post
	template_name='course/blog-home.html'
	#ordering=['-id']
	ordering=['-post_date']

	def get_context_data(self,*args, **kwargs):
		cat_menu=Category.objects.all()
		context=super(BlogHome,self).get_context_data(*args, **kwargs)
		context['cat_menu']=cat_menu
		return context

class BlogDetail(DetailView):
	model=Post
	template_name='course/detail.html'

	def get_context_data(self,*args, **kwargs):
		cat_menu=Category.objects.all()
		stuff=get_object_or_404(Post,id=self.kwargs['pk'])
		total_likes=stuff.total_likes()
		context=super(BlogDetail,self).get_context_data(*args, **kwargs)

		liked=False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked=True

		context['cat_menu']=cat_menu
		context['total_likes']=total_likes
		context['liked']=liked
		return context

def index(request):
	return render(request,'course/index.html',{})


def about(request):
	return render(request,'course/about.html',{})	

def courses(request):
	return render(request,'course/courses.html',{})		


def course_details(request):
	return render(request,'course/course-details.html',{})		

	
def contacts(request):
	return render(request,'course/contacts.html',{})