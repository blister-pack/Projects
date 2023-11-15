from django.shortcuts import render

# Create your views here.


def page_view(request):
    return render(request, "pages/page.html")


def otherpage_view(request):
    return render(request, "pages/otherpage.html")
