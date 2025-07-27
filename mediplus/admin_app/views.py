from django.shortcuts import render,redirect
from.models import *
from mediplus.models import userdetailss

# Create your views here.
def docadmin(request):
    if request.method == "POST":
        doctorphoto = request.FILES["doctorphoto"]
        doctorname = request.POST.get("doctorname")
        doctoremail = request.POST.get("doctoremail")
        doctorphone = request.POST.get("doctorphone") 
        doctorspecification = request.POST.get("doctorspecification") 
        doctorfees = request.POST.get("doctorfees") 
        data=doctordetails( doctorphoto=doctorphoto,doctorname=doctorname,doctoremail=doctoremail,doctorphone=doctorphone,doctorspecification=doctorspecification,doctorfees=doctorfees)
        data.save()
    return render(request,'doctor_details.html')


def viewusers(request):
    data=userdetailss.objects.all()
    return render(request,'viewusers.html',{'res':data})


def viewdoctors(request):
    data=doctordetails.objects.all()
    return render(request,'viewdoctors.html',{'res':data})


def ddelete(request,id):
    data=userdetailss.objects.get(pk=id)
    data.delete()
    return redirect(viewusers)

def udelete(request,id):
    data=doctordetails.objects.get(pk=id)
    data.delete()
    return redirect(viewdoctors)

def uupdate(request,id):
    data=doctordetails.objects.get(pk=id)
    return render(request,'update_doctors.html',{'res':data})

def uupdates(request,id):
     if request.method == "POST":
        doctorphoto = request.FILES["doctorphoto"]
        doctorname = request.POST.get("doctorname")
        doctoremail = request.POST.get("doctoremail")
        doctorphone = request.POST.get("doctorphone") 
        doctorspecification = request.POST.get("doctorspecification") 
        doctorfees = request.POST.get("doctorfees") 
        data=doctordetails(doctorphoto=doctorphoto,doctorname=doctorname,doctoremail=doctoremail,doctorphone=doctorphone,doctorspecification=doctorspecification,doctorfees=doctorfees,id=id)
        data.save()
        return redirect(viewdoctors)
     return render(request,"update_doctors.html")
 
    






    

    
