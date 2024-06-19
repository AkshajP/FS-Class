from django.db import models
from django.forms import ModelForm

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null  = True)
    joined_date = models.DateField(null = True)


class Course(models.Model):
    course_code = models.CharField(max_length=40)
    course_name = models.CharField(max_length=255)
    course_credits = models.IntegerField()

    def __str__(self) -> str:
        return f"Course: {self.course_code} - {self.course_name} - {self.course_credits}"

class Student(models.Model):
    student_usn = models.CharField(max_length=10)
    student_name = models.CharField(max_length=255)
    student_sem = models.IntegerField()
    enrolment = models.ManyToManyField(Course)
    
    def __str__(self) -> str:
        courses = ", ".join([course.course_name for course in self.enrolment.all()])
        return f"Student: {self.student_usn} - {self.student_name} - {self.student_sem} - {courses}"

class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ptopic = models.CharField(max_length=255)
    planguage = models.CharField(max_length=255)
    pduration = models.IntegerField()

    def __str__(self):
        return f"Project: {self.student} - {self.ptopic} - {self.planguage} - {self.pduration}"

class ProjectRegistration(ModelForm):
    required_css_class = 'required' 
    class Meta:
        model = Project
        fields = ['student', 'ptopic', 'planguage', 'pduration']