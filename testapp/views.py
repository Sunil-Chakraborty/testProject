from django.shortcuts import render,redirect
from .models import Student,Article,Publication 
from .forms import  StudentForm 

def students(request):
    students = Student.objects.all()
    context={'students': students}
    return render(request,'testapp/Scrollable-student.html',context)

def articles(request):
    articles = Article.objects.all()    
    context={'articles': articles}
    return render(request,'testapp/articles.html',context)

def add_student(request):  
    student = StudentForm()
    if request.method == 'POST':
        student = StudentForm(request.POST)
        if student.is_valid():
            student.save()
            return redirect('students')         
    return render(request,"testapp/student_frm.html",{'form':student})


def viewStudent(request,pk):  
    students = Student.objects.get(id=pk)
    form=StudentForm(instance=students)
    
    context = {'form':form} 
    return render(request,'testapp/view_form.html', context)


def updateStudent(request,pk):  
    students = Student.objects.get(id=pk)
    form=StudentForm(instance=students)
               
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=students)                
        if form.is_valid():              
            form.save()  
            return redirect('students')
        
    context = {'form':form} 
    
    return render(request,'testapp/edit2_form.html', context)

def deleteStudent(request,pk):
      
    students = Student.objects.get(id=pk)
                       
    if request.method == 'POST':
        students.delete()
        return redirect('students')
        
    context = {'obj':students} 
    
    return render(request,'testapp/delete_template.html', context)