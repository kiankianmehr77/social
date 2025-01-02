from django.shortcuts import render, redirect
from .models import Post
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class PostDetailView(View):
    def get(self, request,post_id, post_slug):
        post = Post.objects.get(pk=post_id, slug = post_slug)
        return render(request, 'post/detail.html', {'post':post})


class PostDeleteView(LoginRequiredMixin,View):

    def get(self,request, post_id):
        post = Post.objects.get(pk = post_id)
        if post.user.id == request.user.id:
            post.delete()
            messages.success(request, 'post deleted succesfully', 'success')
        else:
            messages.error(request, 'you cant delete this post', 'danger')

        return redirect('home:home')