from django.http import HttpResponse
from django.shortcuts import render, redirect

from myapp.models import admintbl, routestbl, managebustbl


# Create your views here.
def index(request):
    return render(request, 'AdminPanel/index.html')

def dashboard(request):
    sesid=request.session.get('admin')
    if not sesid:
        return redirect('../adminpanel')
    return render(request, 'AdminPanel/dashboard.html')
def index_code(request):
    if request.method == "POST":
        a = request.POST.get('email')
        b = request.POST.get('password')
        data=admintbl.objects.filter(username=a).first()
        if not data:
            return HttpResponse("email Wrong")
        if data.password == b:
            request.session['admin'] = a
            return redirect('../dashboard')
        else:
            return HttpResponse("password Wrong")
    else:
        return redirect('../adminpanel')

def managebus(request):
    sesid=request.session.get('admin')
    if not sesid:
        return redirect('../adminpanel')
    getdata=routestbl.objects.all()
    fetch=managebustbl.objects.all()
    return render(request, 'AdminPanel/managebus.html',{'getshow':getdata,'fetchshow':fetch})

def manage_routes(request):
    sesid=request.session.get('admin')
    if not sesid:
        return redirect('../adminpanel')
    data=routestbl.objects.all()
    return render(request, 'AdminPanel/manage_routes.html',{'show':data})

def managebus_code(request):
    if request.method == "POST":
        a=request.POST.get('busname')
        b=request.POST.get('routeid')
        c=request.POST.get('dtime')
        d=request.POST.get('totalseet')
        managebustbl.objects.create(busname=a,routeid=b,dtime=d,totalseet=d)
        return redirect('../managebus')
    else:
        return redirect('../adminpanel')


def manage_routes_code(request):
    if request.method == "POST":
        a=request.POST.get('source')
        b=request.POST.get('destination')
        c=request.POST.get('distance')
        d=request.POST.get('duration')
        routestbl.objects.create(source=a,destination=b,distance=c,duration=d)
        return redirect('../manage_routes')
    else:
        return redirect('../adminpanel')
def manage_routes_delete(request,id):
    routestbl.objects.filter(id=id).delete()
    return redirect('../manage_routes')

def manage_quotas(request):
    sesid=request.session.get('admin')
    if not sesid:
        return redirect('../adminpanel')
    return render(request, 'AdminPanel/manage_routes.html')

def bookin_view(request):
    sesid=request.session.get('admin')
    if not sesid:
        return redirect('../adminpanel')
    return render(request, 'AdminPanel/bookin_view.html')

