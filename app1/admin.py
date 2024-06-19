from django.contrib import admin

from app1.models import Course, Member, Student, Project

class MemberAdmin(admin.ModelAdmin):
    list_display = ("course_name", "course_code", "course_credits",)

admin.site.register(Course, MemberAdmin)

class MyAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone", "joined_date",)

admin.site.register(Member, MyAdmin)

class MyStudent(admin.ModelAdmin):
    list_display = ("student_usn", "student_name", "student_sem")
    
admin.site.register(Student, MyStudent)

class MyProject(admin.ModelAdmin):
    list_display = ("student", "ptopic", "planguage", "pduration")

admin.site.register(Project, MyProject)

