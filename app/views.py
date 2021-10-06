from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,FormView,ListView
# Create your views here.
from django.forms import *

from app.forms import NameForm,StudentForm
from app.models import *

class Cbv_TemplateView(TemplateView):
    template_name='template1.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        #context['name']='Harshad'
        #context['age']=26
        context['form']=NameForm()
        return context
    
    def post(self,request):
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))

class Cbv_FormView(FormView):
    template_name='tempform.html'
    form_class=NameForm

    def form_valid(self,form):
        return HttpResponse(str(form.cleaned_data))

class StudentView(FormView):
    template_name='student.html'
    form_class=StudentForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('data is inserted Successfully')

class StudentList(ListView):
    model=Student
    
    #queryset=Student.objects.filter(name='BBB')
    context_object_name='students'
    ordering=['name']