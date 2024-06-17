from django.db import models

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
    student_usn = models.IntegerField()  
    student_name = models.CharField(max_length=255)
    student_sem = models.IntegerField()
    enrolment = models.ManyToManyField(Course)
    
    def __str__(self) -> str:
        return f"Student: {self.student_usn} - {self.student_name} - {self.student_sem} - {self.enrolment}"