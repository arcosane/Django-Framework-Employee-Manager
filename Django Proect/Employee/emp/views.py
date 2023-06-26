from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp, Testimonial
from .forms import FeedbackForm, EmpForm


# Create your views here.

def emp_home(request):
    emps = Emp.objects.all()
    
    return render(request, "home.html",{
        'emps':emps
    })

def add_emp(request):
    if request.method == "POST":
        
        #fetch data
        
        emp_name= request.POST.get("emp_name")
        emp_id= request.POST.get("emp_id")
        emp_phone= request.POST.get("emp_phone")
        emp_address= request.POST.get("emp_address")
        emp_working= request.POST.get("emp_working")
        emp_department= request.POST.get("emp_department")
        
        #create model
        
        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.working = emp_working
        e.department = emp_department
        if emp_working == None:
            e.working = False
        else:
            e.working = True
        
        #save object
        
        e.save()
        
        #prepare msg
        
        return redirect("/emp/home/")
    form = EmpForm()
    return render(request, "add_emp.html",{'form':form})

def delete_emp(request,emp_id):
    emp = Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp = Emp.objects.get(pk=emp_id)
    return render(request,"update.html",{
        'emp':emp
    })
    
def do_update_emp(request,emp_id):
    
    if request.method == "POST":
        emp_name= request.POST.get("emp_name")
        emp_id_new= request.POST.get("emp_id")
        emp_phone= request.POST.get("emp_phone")
        emp_address= request.POST.get("emp_address")
        emp_working= request.POST.get("emp_working")
        emp_department= request.POST.get("emp_department")
        
        e = Emp.objects.get(pk=emp_id)
        e.name = emp_name
        e.emp_id = emp_id_new
        e.phone = emp_phone
        e.address = emp_address
        e.working = emp_working
        e.department = emp_department
        if emp_working == None:
            e.working = False
        else:
            e.working = True
            
        e.save()

    return redirect("/emp/home/")

def testimonials(request):
    test = Testimonial.objects.all
    return render(request,"testimonials.html",{
        'test':test
    })
    
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return redirect("/emp/home/")
        else:
            return render(request,"feedback.html",{'form':form})
    else:
        form = FeedbackForm()
        return render(request,"feedback.html",{'form':form})