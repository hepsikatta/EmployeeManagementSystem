from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Employee
from django.db.models import Q

# 1. Login System
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_field_valid() or form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# 2. Admin Dashboard & Search Employee
@login_required
def dashboard(request):
    query = request.GET.get('search', '')
    if query:
        employees = Employee.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) | 
            Q(department__icontains=query)
        )
    else:
        employees = Employee.objects.all()
    return render(request, 'dashboard.html', {'employees': employees, 'query': query})

# 3. Add Employee
@login_required
def add_employee(request):
    if request.method == 'POST':
        Employee.objects.create(
            employee_id=request.POST['employee_id'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            department=request.POST['department'],
            designation=request.POST['designation'],
            joining_date=request.POST['joining_date']
        )
        return redirect('dashboard')
    return render(request, 'add_employee.html')

# 4. Update Employee
@login_required
def update_employee(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        emp.first_name = request.POST['first_name']
        emp.last_name = request.POST['last_name']
        emp.email = request.POST['email']
        emp.department = request.POST['department']
        emp.designation = request.POST['designation']
        emp.save()
        return redirect('dashboard')
    return render(request, 'update_employee.html', {'emp': emp})

# 5. Delete Employee
@login_required
def delete_employee(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        emp.delete()
        return redirect('dashboard')
    return render(request, 'delete_confirm.html', {'emp': emp})