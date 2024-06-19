from django.shortcuts import render
from htmlform.forms import htmlForms

def home_view(request):
    form = htmlForms()
    return render(request, "form.html", {"form": form})

# Create your views here.
