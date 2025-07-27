from django.shortcuts import render,redirect
from.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')



def login(request):
    useremail = request.POST.get('useremail')
    userpassword  = request.POST.get('userpassword')
    if useremail == 'admin@gmail.com' and userpassword  =='admin':
        request.session['adminemail'] = useremail
        request.session['admin'] ='admin'
        return render(request,'index.html',{'status': 'Admin Login Success'})

    elif userdetailss.objects.filter(useremail=useremail,userpassword =userpassword ).exists():
        userdetails=userdetailss.objects.get(useremail=request.POST['useremail'],userpassword =userpassword )
        if userdetails.userpassword  == request.POST['userpassword']:
            request.session['uid'] = userdetails.id
            request.session['uname'] = userdetails.username
            request.session['uemail'] = useremail
            request.session['user'] = 'user'
        return render(request,'index.html', {'status': 'User Login Success'})

    else:
            return render(request, 'login.html', {'status': 'Failed'})
        
    return render(request,'login.html')
  
def register(request):
    if request.method == "POST":
        userphoto = request.FILES["userphoto"]
        username = request.POST.get("username")
        useremail = request.POST.get("useremail")
        userphone = request.POST.get("userphone")
        userpassword = request.POST.get("userpassword") 
        userage = request.POST.get("userage")
        data=userdetailss(userphoto=userphoto,username=username,useremail=useremail,userphone=userphone,userpassword=userpassword,userage=userage)
        data.save()
    return render(request,'register.html')

def service(request):
    return render(request,'service_section.html')

def blog(request):
    return render(request,'blog_details.html')

def contact(request):
    return render(request,'contact_us.html')

def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)
def bookappointment(request):
    if request.method == "POST":
        username = request.POST.get("username")
        useremail = request.POST.get("useremail")
        doctorname = request.POST.get("doctorname")
        userphone = request.POST.get("userphone") 
        data=userdetailss(doctorname=doctorname,username=username,useremail=useremail,userphone=userphone,)
        data.save()
        return redirect(index)
    return render(request,'bookappointment.html')




