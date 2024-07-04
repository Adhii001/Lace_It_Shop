from django.shortcuts import render,redirect
from Backend.models import category2db,product2db
from Webapp.models import contactinfodb,Registrationdb,cartdb
from django.contrib import messages

# Create your views here.

def home_page(request):
    cat = category2db.objects.all()
    return render(request,"home.html",{'cat':cat})


def contact(request):
    cat = category2db.objects.all()
    return render(request,"contact.html",{'cat':cat})

def products(request):
    cat = category2db.objects.all()
    pro = product2db.objects.all()
    return render(request,"products.html",{'pro':pro,'cat':cat})

def products_filtered(request,cat_name):
    cat = category2db.objects.all()
    data = product2db.objects.filter(pcategory=cat_name)
    return render(request,"products_filtered.html",{'data':data,'cat':cat})

def single_product(request,Pro_id):
    cat = category2db.objects.all()
    data = product2db.objects.get(id=Pro_id)
    return render(request,"single_product.html",{'data':data,'cat':cat})

def category(request):
    return render(request,"category.html")

def save_contact(request):
    if request.method=="POST":
        cna = request.POST.get('name')
        csub = request.POST.get('subject')
        cmail = request.POST.get('email')
        cmes = request.POST.get('message')
        obj=contactinfodb(cname=cna,cmessage=cmes,cemail=cmail,csubject=csub)
        obj.save()
        return redirect(contact)


def LR(request):
    return render(request,"LR.html")

def save_registration(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        pas=req.POST.get('password')
        img=req.FILES['image']
        obj=Registrationdb(Name=na,Email=em,Password=pas,Image=img)
        if Registrationdb.objects.filter(Name=na).exists():
            messages.warning(req,"User already exists...!")
        elif Registrationdb.objects.filter(Email=em).exists():
            messages.warning(req, "Email already exists...!")
        obj.save()
        messages.success(req, "Registration Successful Please Login...!")
        return redirect(LR)


def User_login(req):
    if req.method=="POST":
        na=req.POST.get('name')
        pwd=req.POST.get('password')
        if Registrationdb.objects.filter(Name=na,Password=pwd).exists():
            req.session['Username']=na
            req.session['Password']=pwd
            messages.success(req, "Login Successful..!")
            return redirect(home_page)


        else:
            messages.warning(req, "Incorect Username/Password")
            return redirect(LR)


    else:
        messages.warning(req, "User Not Exist")
        return redirect(LR)



def User_Logout(req):
    del req.session['Username']
    del req.session['Password']
    messages.success(req, "Logout Successful..!")
    return redirect(home_page)


def save_cart(req):
    if req.method=="POST":
        una=req.POST.get('uname')
        pna=req.POST.get('pname')
        pqty=req.POST.get('qty')
        tot=req.POST.get('total1')
        obj=cartdb(User_name=una,Product_name=pna,Quantity=pqty,Total_price=tot)
        obj.save()
        return redirect(home_page)

def cart(req):
    data=cartdb.objects.filter(User_name=req.session['Username'])
    cat = category2db.objects.all()
    Total_Price=0
    shipping_price=0
    for i in data:
        Total_Price=Total_Price+i.Total_price
        if Total_Price>1500:
            shipping_price=0
        else:
            shipping_price=100

    return render(req,"cart.html",{'data':data,'Total_Price':Total_Price,'cat':cat,'shipping_price':shipping_price})