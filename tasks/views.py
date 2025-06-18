from django.shortcuts import render
from django.http import HttpResponse
from tasks.froms import TaskForm,TaskModelForm
from tasks.models import Employee,Task, TaskDetail, Project
from datetime import date
from django.db.models import Q,Count,Max,Min,Avg

# Create your views here.

def manager_dashboard(request):
    return render(request,"dashboard/manager.html")

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


            ''' For Django Form Data '''
            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')

            # task = Task.objects.create(title=title,description=description,due_date=due_date)
            
            # # assign employee to task
            # for emp_id in assigned_to:
            #     employees = Employee.objects.get(id=emp_id)
            #     task.assigned_to.add(employees)

            # return HttpResponse("Task Added Succesfully!!")
        
    context = {"form":form}
    return render(request,'task_form.html',context)

def view_task(request):
    # tasks = Task.objects.all()
    # task_3 = Task.objects.get(id=3)
    # first_task = Task.objects.first()
    # return render(request,"show_task.html",{"tasks":tasks, "task_3":task_3,"first_task":first_task})
    # tasks = Task.objects.filter(status="COMPLETED")
    # tasks = Task.objects.filter(due_date=date.today())
    # tasks = TaskDetail.objects.exclude(priority="L")
    # tasks = Task.objects.filter(title__icontains="c",status="PENDING")
    # tasks = Task.objects.filter(Q(status="PENDING") | Q(status="IN_PROGRESS"))
    # tasks = Task.objects.select_related('details').all()

    task_cnt = Project.objects.annotate(num_task=Count('task'))
    return render(request, 'show_task.html',{"task_cnt":task_cnt})