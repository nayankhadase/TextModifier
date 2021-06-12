from django.shortcuts import render
from .models import Inquire
from django.contrib import messages
# Create your views here.
def Home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'about.html')

def Contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        query=request.POST.get('query')
        obj=Inquire()
        obj.name=name
        obj.email=email
        obj.mobile=mobile
        obj.query=query
        obj.save()
        messages.success(request,"We Got Your Request..")
        return render(request,'contact.html',{'name':name})
    else:
        return render(request,'contact.html')

def Analize(request):
    query=request.POST.get('query')
    upper=request.POST.get('upper','off')
    punch=request.POST.get('punch','off')
    lower=request.POST.get('lower','off')
    numbers=request.POST.get('numbers','off')
    wordcount=request.POST.get('wordcount','off')
    lettercount=request.POST.get('lettercount','off')
    extraspace=request.POST.get('extraspace','off')
    newline=request.POST.get('newline','off')
    
    punctuation='''<>,./?;:'"}{][\|`~!@#$%^&*)(_+=-*'''
    num="1234567890"
    result=""
    if upper == "on":
        if result == '':
            result=query
        result=result.upper()
        
    if punch == "on":
        if result == '':
            for i in query:
                if i not in punctuation:
                    result+=i
        elif result != '':
            data=''
            for i in result:
                if i not in punctuation:
                    data+=i   
            result=data 

    if lower == "on":
        if result == "":
            result=query
        result=result.lower()

    if numbers=="on":
        if result=="":
            for i in query:
                if i not in num:
                    result+=i
        elif result !="":
            data=""
            for i in result:
                if i not in num:
                    data+=i
            result=data

    
    if lettercount== "on":
        if result=="":
            result=query
        length=len(result)
        count=0
        for i in result:
            if i == " ":
                count+=1
            elif i=="\n":
                count+=2
        lettercount=length-count

    if wordcount =="on":
        if result=="":
            result=query
        # remove newline
        data1=""
        for char in result:
            if char != "\n" and char!="\r":
                data1+=char
            else:
                data1+=" "
        # remove extra spaces
        data2=''
        for index,char in enumerate(data1):
            if not (data1[index-1] == " " and data1[index] == " "):
                data2+=char
        #strap is use to remove white spaces from start and end
        data3=data2.strip()
        count=1 # this is for 1st word
        for index,char in enumerate(data3):
            if data3[index-1] == " " and data3[index]!=" ":
                count+=1
        wordcount=count

    if newline =="on":
        if result=="":
            result=query
        data1=""
        for char in result:
            if char != "\n" and char!="\r":
                data1+=char
            else:
                data1+=" "
        data=''
        for index,char in enumerate(data1):
            if not (data1[index-1] == " " and data1[index] == " "):
                data+=char
        result=data

    if extraspace =="on" and newline =="off":
        if result=="":
            result=query
        result=result.strip()
        data=""
        for index,char in enumerate(result):
            if not (result[index] == " " and result[index+1] == " "):
                data+=char
        result=data

    # if no modification apply
    error=''
    if (upper=="off" and punch=="off" and lower=="off" and numbers=="off" and wordcount=="off" and lettercount=="off" and extraspace=="off" and newline=="off"):
        result=query
        error="You have not choose any text modifier"

    data={'result':result,"length":lettercount,"wordcount":wordcount,'error':error}
    return render(request,'result.html',data)