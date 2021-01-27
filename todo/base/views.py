from django.shortcuts import render

# Create your views here.
tasks = []

def viewtasks(request):
    template_name = 'base/view.html'
    return render(request,template_name,context)
