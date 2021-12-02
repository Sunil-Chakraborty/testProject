from django.contrib import admin
from .models import Publication, Article, Student,Person,Group,Membership
from django.db import models
from django.forms import CheckboxSelectMultiple,Textarea,TextInput


# Checkbox for many-to-many fields

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},       
    }

admin.site.register(Article,ArticleAdmin)
    

class StudentAdmin(admin.ModelAdmin):    
    list_display = ('username','mobile')

    
admin.site.register(Student,StudentAdmin) 

admin.site.register(Publication)

admin.site.register(Person)
admin.site.register(Group)


class MembershipAdmin(admin.ModelAdmin):
    list_display = ['person', 'group', 'date_joined', 'invite_reason']
    
    
admin.site.register(Membership,MembershipAdmin)

