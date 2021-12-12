from django.urls import path
from .import views

urlpatterns = [    
    path('',views.students, name='students'),
    path('add-student/',views.add_student, name='add-student'),
    path('view-student/<str:pk>', views.viewStudent, name='view-student'), 
    path('update-student/<str:pk>', views.updateStudent, name='update-student'),
    path('delete-student/<str:pk>', views.deleteStudent, name='delete-student'),             
    path('articles/',views.articles, name='articles'),       
]
