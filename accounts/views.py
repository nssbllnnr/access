from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
# from .forms import CreateUserForm
# Create your views here.
# def registerPage(request):
#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()


#     template = 'accounts/register.html'
#     context = {'form':form}
#     return render(request,template,context)
# def loginPage(request):
#     context = {}
#     return render(request, 'accounts/login.html', context)
def home(request):
    employees = Employees.objects.all()
    total_employees = employees.count()
    teachers = employees.filter(status='Teacher').count()
    students = employees.filter(status='Student').count()
    context = {'employees':employees,'total_employees':total_employees,'teachers':teachers,'students':students}
    return render(request, 'accounts/dashboard.html',context)

def all(request):
    pass

def customer(request, id):
    customer = Employees.objects.get(id=id)
    # orders = customer.order_set.all()
    # order_count = orders.count()
    context = {'customer':customer}
    return render(request, 'accounts/customer.html',context)
 