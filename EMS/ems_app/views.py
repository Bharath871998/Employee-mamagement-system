from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

# Getting the list of all the Employees
def home(request):
    staff = Employee.objects.all()
    return render(request, 'crud/home.html', {"sdata": staff})


# Adding new Employee
def new_emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm()   
    return render(request, 'crud/new_emp.html', {'form': form})


# Editing the existing Employee details
def edit_emp(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            eform = EmployeeForm()
        else:
            my_staff = Employee.objects.get(id = id)
            eform = EmployeeForm(instance=my_staff)
        return render(request, 'crud/edit_emp.html', {'form': eform})
    else:
        if id == 0:
            eform = EmployeeForm(request.POST)
        else:
            staff = Employee.objects.get(id=id)
            ef = EmployeeForm(request.POST, instance = staff)
            if ef.is_valid():
                ef.save()
                return redirect('/')
            else:
                return render(request, 'crud/edit.html', {'form': eform})
    
    
def delete_emp(request,id):
    dform = Employee.objects.get(id=id)
    dform.delete()
    return redirect('/')
