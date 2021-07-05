from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
from django.contrib.auth import logout
from myapp1.models import Patient,Donor


# Create your views here.
def homepage(request):
    #return HttpResponse('<h1>HOMEPAGE</h1>')
    return render(request,'BloodBankProj1/homepage.html')

def newuser(request):
    return render(request,'BloodBankProj1/newuser.html')

def newuser_detail(request):
    if request.method == "POST":
        username1 = request.POST["u_name"]
        password1 = request.POST["u_password"]
        user = auth.authenticate(username=username1, password=password1)
        if user is None:
            obj = User.objects.create_user(username=username1, password=password1)
            obj.save()
            return render(request,'BloodBankProj1/homepage.html')
        else:
            return HttpResponse(" username or password already exist ")
    else:
        return HttpResponse(" request is of type GET ")
def loginForm(request):
    return render(request, 'BloodBankProj1/login_detail_form.html')

def login1(request):
    if request.method == "POST":
        username1 = request.POST["name"]
        password1 = request.POST["password"]
        obj=auth.authenticate(username=username1,password=password1)
        if obj is not None:
            return render(request, 'BloodBankProj1/homepage.html', {"user":obj})
        else:
            return render(request,'BloodBankProj1/homepage.html')
    else:
        return HttpResponse("request method is of type GET")

def d_register_form(request):
    return render(request, 'BloodBankProj1/d_regform.html')

def p_register_form(request):
    return render(request, 'BloodBankProj1/p_regform.html')

def d_registration(request):
    if request.method=="POST":
        name1=request.POST["name"]
        age1 = request.POST["age"]
        ph_no1 = request.POST["phone_no"]
        bgp1 = request.POST["group"]
        email1=request.POST["email"]
        unit_req1=request.POST["unit"]
        date_t='2020-10-25 14:30:59'
        user=Donor(d_name1=name1,d_group_blood1=bgp1,d_unit1=unit_req1,d_age1=age1,d_phone_no1=ph_no1,d_email1=email1,d_date1=date_t)
        user.save()
        return render(request, 'BloodBankProj1/homepage.html')
    else:
        return HttpResponse('method type is get')

def p_registration(request):
    if request.method == "POST":
        name1 = request.POST["name"]
        age1 = request.POST["age"]
        ph_no1 = request.POST["phone_no"]
        bgp1 = request.POST["group"]
        email1=request.POST["email"]
        unit_req1=request.POST["unit"]
        date_t='2020-10-25 14:30:59'
        user=Patient(p_name=name1,p_group_blood=bgp1,p_unit=unit_req1,p_age=age1,p_phone_no=ph_no1,p_email=email1,p_date=date_t)
        user.save()
        return render(request, 'BloodBankProj1/homepage.html')
    else:
        return HttpResponse('method type is get')
def historyForm(request):
    return render(request, 'BloodBankProj1/detail1_form.html')

def mydetails(request):
    if request.method == "POST":
        email_id = request.POST["email"]
        ph_no = request.POST["phone"]
        typ=request.POST["TYPE"]
        print(typ)
        if typ=="D":
            qset1 = Donor.objects.filter(d_email1=email_id,d_phone_no1=ph_no)
            print(qset1)
            return render(request, 'BloodBankProj1/my_details.html',{"qset":qset1,"tp":typ})
        else:
            qset1 = Patient.objects.filter(p_email=email_id, p_phone_no=ph_no)
            return render(request, 'BloodBankProj1/p_details.html', {"qset": qset1,"tp":typ})
    else:
        return HttpResponse("request method is of type GET")

def logout1(request):
    logout(request)
    return render(request, 'BloodBankProj1/homepage.html')



