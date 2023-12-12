from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            redirect("add_post")
            post_form.save()
    else:
        post_form = forms.PostForm()
    return render(request,'add_post.html',{"form":post_form})
