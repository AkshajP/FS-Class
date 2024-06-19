from django import forms
class htmlForms(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=255)
    available = forms.BooleanField()

    # firstname = forms.CharField(max_length=255)
    # lastname = forms.CharField(max_length=255)
    # phone = forms.IntegerField()
    # joined_date = forms.DateField()
    
    # course_code = forms.CharField(max_length=40)
    # course_name = forms.CharField(max_length=255)
    # course_credits = forms.IntegerField()
    
    # student_usn = forms.IntegerField()
    # student_name = forms.CharField(max_length=255)
    # student_sem = forms.IntegerField()
    # enrolment = forms.ModelMultipleChoiceField(queryset=None)