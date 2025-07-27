from django.shortcuts import render
from mediplus .  models import userdetailss

# Create your views here.

def viewprofile(request):
    u_id=request.session['uid']
    data=userdetailss.objects.get(pk=u_id)
    return render(request,'viewprofile.html',{'res':data})
    