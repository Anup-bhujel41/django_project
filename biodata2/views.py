from django.shortcuts import redirect, render
from biodata2.models import Feedback, Product
from portfolio.models import Biodata


# # Create your views here.
# def landing_page(request):
#     return render(request, "land.html")

# def form1(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         number = request.POST.get("number")
#         feedback = request.POST.get("feedback")

#         Product.objects.create(
#             name = name,
#             email = email,
#             number = number,
#             feedback = feedback

#         )
#         return redirect("biodata")
#     return render(request, "land.html")


# def form2(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         address = request.POST.get("address")
#         age = request.POST.get("age")
#         email = request.POST.get("email")
#         company = request.POST.get("company")

#         Biodata.objects.create(
#             name = name,
#             address = address,
#             age = age,
#             email = email,
#             company = company
#         )
#         return redirect("test")
#     return render(request, landing_page)
    

def landing_page(request):
    form_type = request.POST.get("form_type")
    if form_type == "feedback":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        feedback_text = request.POST.get("feedback")

        Feedback.objects.create(
            name = name,
            email = email,
            number = number,
            feedback = feedback_text

        )
        return redirect("/api/v1/biodata")
    
    if form_type == "signup":
        name = request.POST.get("name")
        address = request.POST.get("address")
        age = request.POST.get("age")
        email = request.POST.get("email")
        company = request.POST.get("company")
# 
        Biodata.objects.create(
            name = name,
            address = address,
            age = age,
            email = email,
            company = company
        )
        return redirect("/test")
    return render(request, "land.html")

