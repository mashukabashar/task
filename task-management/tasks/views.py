from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Welcome to the task management system")

# def contact(request):
#     return HttpResponse("<h1 style='color:red; text-align:center'>Welcome to the contact page</h1>")

# def show_task(request):
#     return HttpResponse("<h1 style='color:red; text-align:center'>Welcome to the task page</h1>")

# def show_specific_task(request, id):
#     return HttpResponse("<h1 style='color:red; text-align:center'>Welcome to the specific task page</h1>")
# print("id",id)
# print("id type",type(id))


def manager_dashboard(request):
    return render(request,"dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request,"dashboard/user-dashboard.html")

def test(request):
    context={
        "names":["Diya","Moni","Mashuka"],
        "age":23
    }
    return render(request,"test.html",context)
