from django.shortcuts import render, redirect
from .models import Biodata

# Create your views here.
def landing_page(request):
    return render(request, "landing.html")

def form(request):
    if request.method == "POST":

        # Get data from form
        name = request.POST.get("name")
        address = request.POST.get("address")
        age = request.POST.get("age")
        email = request.POST.get("email")
        company = request.POST.get("company")
        
        # Save to database
        Biodata.objects.create(
            name=name,
            address=address,    
            age=age,
            email=email,
            company=company
        )
        
        # Redirect to the same page
        return redirect("test")

    # If GET request, show the form
    return render(request, "form.html")

def form2(request):
    print("form2 was called")
    if request.method == "POST":

        # Get data from form
        name = request.POST.get("name")
        address = request.POST.get("address")
        age = request.POST.get("age")
        email = request.POST.get("email")
        company = request.POST.get("company")
        
        # Save to database
        Biodata.objects.create(
            name=name,
            address=address,    
            age=age,
            email=email,
            company=company
        )
        
        # Redirect to the same page
        return redirect("test")
