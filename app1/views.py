from django.shortcuts import render
from django.template import loader, Template, context
from django.http import HttpResponse

from .models import Member
from app1.models import Student, Course

def testing(request):
    mydata = Member.objects.all()
    template = loader.get_template('model.html')
    context = {
        'members': mydata,
    }
    return HttpResponse(template.render(context, request))

def details_of_employees(request,id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {'mymember': mymember,}
    return HttpResponse(template.render(context, request))

def reg(request):
    if request.method == 'POST':
        sid = request.POST.get('sname')
        cid = request.POST.get('cname')
        student = Student.objects.get(id=sid)
        course = Course.objects.get(id=cid)
        res = student.enrolment.filter(id=cid)
        if res:
            return HttpResponse("Already Enrolled")
        student.enrolment.add(course)
        return HttpResponse("Enrolled Successfully")
    else:
        students = Student.objects.all()
        courses = Course.objects.all()
        return render(request, "t2.html", {"students":students, "courses": courses})