import os
from django.contrib import messages
from pytube import Youtube
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    if request.method == 'GET':
        search = request.GET.get('src')
        if search:
            prof = Profile.objects.filter(name__icontains = search)
        elif search == "None":
            return redirect('home')
        else:
           prof = Profile.objects.all() 
    return render(request, 'index.html',locals())
# delete 
def delete(request,id):
    prof =Profile.objects.get(id=id)
    if prof.image != 'defProf.jpg':
        os.remove(prof.image.path)
    prof.delete()
    messages.warning(request, "Account Deleted.")
    return redirect('index')
# create
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        birth_date = request.POST.get('birth_date')
        image = request.FILES.get('image')
        blood = request.POST.get('blood')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')
        address = request.POST.get('address')
        if Profile.objects.filter(name=name).exists():
            messages.warning(request, "Another account exists this name.")
        elif Profile.objects.filter(email=email).exists():
            messages.warning(request, "Another account exists this email.")
        else:   
            if image:
                prof = Profile.objects.create(name=name, email=email, phone=phone, age=age, birth_date=birth_date, image=image, blood=blood, gender=gender, religion=religion, address=address)
                prof.save()
                messages.success(request, "account created")
                return redirect('index')
            else:
                prof = Profile.objects.create(name=name, email=email, phone=phone, age=age, birth_date=birth_date, blood=blood, gender=gender, religion=religion, address=address)
                prof.save()
                messages.success(request, "account created")
                return redirect('index')
    return render(request,'create.html')
# update profile
def update(request, id):
    prof = Profile.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        birth_date = request.POST.get('birth_date')
        image = request.FILES.get('image')
        blood = request.POST.get('blood')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')
        address = request.POST.get('address')
        if image:
            if image != 'defProf.jpg':
                os.remove(prof.image.path)
                prof.image = image
            prof.name = name
            prof.email = email
            prof.phone = phone
            prof.age = age
            prof.birth_date = birth_date
            prof.blood=blood
            prof.gender = gender
            prof.religion = religion
            prof.address = address
            prof.save()
            messages.success(request, "account updated")
            redirect(request, 'index')
        else:
            messages.success(request, "Got an error")
    return render(request,'update.html', locals())
# single profile details
def profileDetails(request, id):
    prof = Profile.objects.get(id=id)
    return render(request, 'profileDetails.html', locals())
# calculator
result = []
def cal(request):
    if request.method =='POST':     
        if request.POST.get('1'):  
            result.append('1')       
            output = ''.join(result) 
            print(output)

        elif request.POST.get('2'):
            result.append('2')
            output = ''.join(result)
            print(output)
        elif request.POST.get('3'):
            result.append('3')
            output = ''.join(result)
            print(output)
        elif request.POST.get('4'):
            result.append('4')
            output = ''.join(result)
            print(output)
        elif request.POST.get('5'):
            result.append('5')
            output = ''.join(result)
            print(output)
            
        elif request.POST.get('6'):
            result.append('6')
            output = ''.join(result)
            print(output)
        elif request.POST.get('7'):
            result.append('7')
            output = ''.join(result)
            print(output)
        elif request.POST.get('8'):
            result.append('8')
            output = ''.join(result)
            print(output)
        elif request.POST.get('9'):
            result.append('9')
            output = ''.join(result)
            print(output)
        elif request.POST.get('+'):
            result.append('+')
            output = ''.join(result)
            print(output)
        elif request.POST.get('-'):
            result.append('-')
            output = ''.join(result)
            print(output)
        elif request.POST.get('*'):
            qa=result.append('*')
            output = ''.join(result)
            print(output)
        elif request.POST.get('/'):
            result.append('/')
            output = ''.join(result)
            print(output)
        elif request.POST.get('0'):
            result.append('0')
            output = ''.join(result)
            if output=="3240" :
                output='Secret code'
            print(output)
        elif request.POST.get('C'):
            result.clear()

        elif request.POST.get('='): 
            try:                    
                r = ''.join(result)    
                output=eval(r)          
                print(output)
                result.clear()       
            except:
                output='00'
                result.clear()    
    return render(request,'cal.html',locals(),)
# Converter
def converter(request):
    return render(request, 'imageToPdf.html')
# Downloader
def downloader(request):
    return render (request,"downloader.html")