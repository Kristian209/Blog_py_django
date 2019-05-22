from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
    "title": "Home"
    }
    return render(request, "home.html", context)

def about(request):
    title = "About"
    context = {
    "title": title,
    }
    return render(request, "about.html", context)
