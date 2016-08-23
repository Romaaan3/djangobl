from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
# Create your views here.
from .models import Post

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully created new post!", extra_tags="some-class")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, pk=None):
	instance = get_object_or_404(Post, id = pk)
	context = {
		"title": instance.title, 
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
		"title": "List"
	}		
	return render(request, "post_list.html", context)

def post_update(request, pk=None):
	instance = get_object_or_404(Post, id = pk)
	form = PostForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully updated post!")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title, 
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)

def post_delete(request, pk=None):
	instance = get_object_or_404(Post, id=pk)
	instance.delete()
	messages.success(request, "Successfully deleted!")
	return redirect("posts:list")
	