from django.shortcuts import render


# Create your views here.
def filter_view(request):
    return render(
        request,
        "filters_app/filter.html",
        {"message": "a message to capitalize on every word"},
    )
