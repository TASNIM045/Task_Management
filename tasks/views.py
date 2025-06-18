from django.shortcuts import render
from django.http import HttpResponse
from tasks.froms import TaskForm,TaskModelForm
from tasks.models import Employee,Task, TaskDetail, Project
from datetime import date
from django.db.models import Q,Count,Max,Min,Avg

# Create your views here.

def manager_dashboard(request):
    tasks = Task.objects.all()
    total_task = tasks.count()
    completed_task = Task.objects.filter(status="COMPLETED").count()
    in_progress_task = Task.objects.filter(status="IN_PROGRESS").count()
    pending_task = Task.objects.filter(status="PENDING").count()

    context = {
        'tasks' : tasks,
        'total_task' : total_task,
        'completed_task' : completed_task,
        'in_progress_task' : in_progress_task,
        'pending_task' : pending_task
    }
    return render(request,"dashboard/manager.html",context)

def user_dashboard(request):
    return render(request,"dashboard/user.html")

def test(request):
    context = {
        "name":["alu","potol"],
        "age":45,
    }
    return render(request,'test.html',context)

def create_task(request):
    employees = Employee.objects.all()
    form = TaskModelForm()

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            ''' For ModelForm Data '''
            form.save()
            return render(request,'task_form.html',{'form':form,'massage':'Task Added Succesfully!!'})
        
    context = {"form":form}
    return render(request,'task_form.html',context)

def view_task(request):
    task_cnt = Project.objects.annotate(num_task=Count('task'))
    return render(request, 'show_task.html',{"task_cnt":task_cnt})