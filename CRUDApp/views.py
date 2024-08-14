from django.shortcuts import render, HttpResponseRedirect
from .models import Employee
from django.contrib import messages

# Create your views here.

def Home(request):
    if request.method == 'POST':
        empID = request.POST.get('empID')
        empName = request.POST.get('empName')
        empDesg = request.POST.get('empDesg')
        empSlaray = request.POST.get('empSlaray')
        emp = Employee(empID=empID, empName=empName,empDesg=empDesg,empSlaray=empSlaray)
        emp.save()
        messages.success(request, 'Data Submited Successfully!!!')
    return render(request, 'index.html')



def AllEmployee(request):
    emp = Employee.objects.all()
    return render(request, 'employee.html',{'employee':emp})

def EmployeeUpdate(request, id):
    emp = Employee.objects.get(pk=id)
    if request.method == 'POST':
        empID = request.POST.get('empID')
        empName = request.POST.get('empName')
        empDesg = request.POST.get('empDesg')
        empSlaray = request.POST.get('empSlaray')
        emp = Employee(id=id,empID=empID, empName=empName,empDesg=empDesg,empSlaray=empSlaray)
        emp.save()
        messages.success(request, 'Data Updated Successfully!!!')
    return render(request, 'update.html',{'e':emp})

def DeleteEmployee(request, id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return HttpResponseRedirect('/employee/')
