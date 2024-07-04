from django.shortcuts import render,redirect
from Backend.models import category2db,product2db
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Webapp.models import contactinfodb

# Create your views here.
def index_page(request):
    return render(request,"index_page.html")

def add_category(request):
    return render(request,"add_category.html")

def save_category(request):
    if request.method=="POST":
        cna=request.POST.get('cname')
        cdes=request.POST.get('cdescription')
        cimg=request.FILES['cimage']
        obj=category2db(cname=cna,cdescription=cdes,cimage=cimg)
        obj.save()
        return redirect(add_category)

def display_category(request):
    data = category2db.objects.all()
    return render(request,"display_category.html",{'data': data})

def edit_category(request,c_id):
    cat = category2db.objects.filter(id=c_id)
    return render(request, "edit_category.html", {'cat': cat})

def update_category(request,c_id):
    cn=request.POST.get('cname')
    cdes=request.POST.get('cdescription')
    try:
        img=request.FILES['cimage']
        fs=FileSystemStorage()
        file=fs.save(img.name,img)
    except MultiValueDictKeyError:
        file=category2db.objects.get(id=c_id).cimage
    category2db.objects.filter(id=c_id).update(cname=cn,cdescription=cdes,cimage=file)
    return redirect(display_category)

def delete_category(request,c_id):
    data=category2db.objects.filter(id=c_id)
    data.delete()
    return redirect(display_category)

def login_page(request):
    return render(request,"login.html")

def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        ps = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=ps)

            if x is not None:
                login(request,x)
                request.session['username'] = un
                request.session['password'] = ps

                return redirect(index_page)
            else:
                return redirect(login_page)
        else:
            return redirect(login_page)


def logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)

def add_product(request):
    cat = category2db.objects.all()
    return render(request,"add_product.html",{'cat':cat})


def save_product(request):
    if request.method=="POST":
        pcat=request.POST.get('pcat')
        pna=request.POST.get('pname')
        pri=request.POST.get('pprice')
        pdes=request.POST.get('pdescription')
        pimg=request.FILES['pimage']
        obj=product2db(pname=pna,pprice=pri,pdescription=pdes,pimage=pimg,pcategory=pcat)
        obj.save()
        return redirect(add_product)

def display_product(request):
    data=product2db.objects.all()
    return render(request,"display_product.html",{'data':data})

def edit_product(request,pro_id):
    pro = product2db.objects.filter(id=pro_id)
    cat =category2db.objects.all()
    return render(request,"edit_product.html",{'pro':pro},{'cat':cat})

def update_product02(request,pro_id):
    pcat = request.POST.get('pcat')
    pn=request.POST.get('pname')
    pr=request.POST.get('pprice')
    pdes=request.POST.get('pdescription')
    try:
        img=request.FILES['pimage']
        fs=FileSystemStorage()
        file=fs.save(img.name,img)
    except MultiValueDictKeyError:
        file=product2db.objects.get(id=pro_id).pimage
    product2db.objects.filter(id=pro_id).update(pname=pn,pprice=pr,pdescription=pdes,pimage=file,pcategory=pcat)
    return redirect(display_product)

def delete_product(request,pro_id):
    data = product2db.objects.filter(id=pro_id)
    data.delete()
    return redirect(display_product)

def contact_info(request):
    data=contactinfodb.objects.all()
    return render(request,"contact_data.html",{'data':data})
