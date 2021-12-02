from django import forms 
from .models import Student 
 
# class StudentForm(forms.Form):  
#     firstname = forms.CharField(label="Enter first name",max_length=50)  
#     lastname  = forms.CharField(label="Enter last name", max_length = 100)

  
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        # fields = "__all__"
        fields = ['username','first_name','last_name','email','mobile','bio','tot_marks']        