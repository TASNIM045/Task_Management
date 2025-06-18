from django.shortcuts import render
from django.http import HttpResponse
from tasks.froms import TaskForm,TaskModelForm
from tasks.models import Employee,Task, TaskDetail, Project
from datetime import date
from django.db.models import Q,Count,Max,Min,Avg

# Create your views here.

def manager_dashboard(request):
    type = request.GET.get('type', 'all')
    counts = Task.objects.aggregate(
        total = Count('id'),
        completed=Count('id', filter=Q(status='COMPLETED')),
        in_progress_task = Count('id',filter=Q(status='IN_PROGRESS')),
        pending = Count('id',filter=Q(status='PENDING'))
    )

    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')
    if type == 'completed':
        tasks = base_query.filter(status='COMPLETED')
    elif type == 'in-progress':
        tasks = base_query.filter(status='IN_PROGRESS')
    elif type == 'pending':
        tasks = base_query.filter(status='PENDING')
    elif type == 'all':
        tasks = base_query.all()

    context = {
        'tasks' : tasks,
        'counts' : counts
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