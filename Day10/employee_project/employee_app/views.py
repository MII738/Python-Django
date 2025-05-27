from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q


def employee_list(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'id')  # default sort by id

    employees = Employee.objects.all()

    if search_query:
        employees = employees.filter(
            Q(name__icontains=search_query) | Q(email__icontains=search_query)
        )

    if sort_by in ['name', '-name', 'email', '-email', 'id', '-id']:
        employees = employees.order_by(sort_by)

    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'employee_app/employee_list.html', context)


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully.")
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_app/employee_form.html', {'form': form})


def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully.")
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_app/employee_form.html', {'form': form})


def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    messages.error(request, "Employee deleted successfully.")
    return redirect('employee_list')
