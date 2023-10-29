from django.shortcuts import render,redirect
from nouapp.models import Student, Login
from django.views.decorators.cache import cache_control
from . models import Sturesponse,Question,Answer
from django.contrib import messages
from datetime import date
from adminapp.models import Material

# cache := all values(session,cookies) on client browser is stored in cache

# Create your views here.

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def studenthome(req):
    try:
        if req.session['rollno']!=None:
            rollno=req.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(req,'studenthome.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
def studentlogout(req):
    try:
        del req.session['rollno']
    except KeyError:
        return redirect('nouapp:login')
    return redirect('nouapp:login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def response(req):
    try:
        if req.session['rollno']!=None:
            rollno=req.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if req.method=="POST":
                responsetype=req.POST['responsetype']
                subject=req.POST['subject']
                responsetext=req.POST['responsetext']
                responsedate=date.today()
                rollno=stu.rollno
                name=stu.name
                program=stu.program
                branch=stu.branch
                year=stu.year
                contactno=stu.contactno
                emailaddress=stu.emailaddress
                print(subject)
                print(contactno)
                sr=Sturesponse(rollno=rollno,name=name,program=program,branch=branch,year=year,contactno=contactno,emailaddress=emailaddress,responsetype=responsetype,subject=subject,responsetext=responsetext,responsedate=responsedate)
                sr.save()
                messages.success(req,"SUCCESS")
            
            return render(req,'response.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def changepassword(req):
    try:
        if req.session['rollno']!=None:
            rollno=req.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if req.method=='POST':
                oldpassword=req.POST['oldpassword']
                newpassword=req.POST['newpassword']
                confirmpassword=req.POST['confirmpassword']
                if newpassword!=confirmpassword:
                    messages.error(req,'ConfirmPassword and NewPassword does not match')
                    return render(req,'changepassword.html',locals())
                try:
                    obj=Login.objects.get(userid=rollno,password=oldpassword)
                    Login.objects.filter(userid=rollno).update(password=newpassword)
                    return redirect('studentapp:studentlogout')
                except:
                    messages.error(req,'Old Password is not matched')
                    return render(req,'changepassword.html',locals())
            return render(req,'changepassword.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def postquestion(req):
    try:
        if req.session['rollno']!=None:
            rollno=req.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            if req.method=='POST':
                question=req.POST['question']
                postedby=stu.name
                posteddate=date.today()
                Question(question=question,postedby=postedby,posteddate=posteddate).save()
            ques=Question.objects.all()    
            return render(req,'postquestion.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def postanswer(req,qid):
    try:
        if req.session['rollno']!=None:
            rollno=req.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            qid=qid
            return render(req,'postanswer.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def postans(req):
    try:
        if req.session['rollno']!=None:
            rollno=req.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            qid=req.POST['qid']
            answer=req.POST['answer']
            answeredby=stu.name
            posteddate=date.today()
            Answer(answer=answer,answeredby=answeredby,posteddate=posteddate,qid=qid).save()
            return redirect('studentapp:postquestion')
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewanswer(req,qid):
    try:
        if req.session['rollno']!=None:
            rollno=req.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            ans=Answer.objects.filter(qid=qid)
            return render(req,'viewanswer.html',locals())
    except KeyError:
        return redirect('nouapp:login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewprofile(req):
    try:
        if req.session['rollno']!=None:
            rollno=req.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(req,'viewprofile.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def studenthome(req):
    try:
        if req.session['rollno']!=None:
            rollno=req.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            return render(req,'studenthome.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewsmat(req):
    try:
        if req.session['rollno']!=None:
            rollno=req.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            program=stu.program
            branch=stu.branch
            year=stu.year
            mat=Material.objects.filter(program=program,branch=branch,year=year,materialtype='smat')
            return render(req,'viewsmat.html',locals())
    except KeyError:
        return redirect('nouapp:login')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def viewassign(req):
    try:
        if req.session['rollno']!=None:
            rollno=req.session['rollno']
            stu=Student.objects.get(rollno=rollno)
            program=stu.program
            branch=stu.branch
            year=stu.year
            mat=Material.objects.filter(program=program,branch=branch,year=year,materialtype='assign')
            return render(req,'viewassign.html',locals())
    except KeyError:
        return redirect('nouapp:login')