from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post
# Create your views here.
def post_list_view(request):
    qs = Post.objects.all()
    random = Post.objects.all().order_by("?")
    context = {
    "object_list": qs,
    "random_list": random
    }
    return render(request,"posts/list.html", context)

def post_detail_view(request, id=None):
    #obj = Post.objects.get(id=id)
    obj = get_object_or_404(Post, id=id)
    context = {
    "object": obj
    }
    return render(request,"posts/detail.html", context)

def post_search_view(request):
    #print(request.GET)
    request_params = request.GET
    query = request_params.get('q')
    qs = Post.objects.none()
    if query:
     qs = Post.objects.filter(
                              Q(title__icontains=query) |
                              Q(content__icontains=query)
                              )
    context = {
    "object_list": qs
    }
    return render(request,"posts/list.html", context)
