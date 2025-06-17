from django.shortcuts import render
from django.http import HttpResponse
from tasks.froms import TaskForm,TaskModelForm
from tasks.models import Employee,Task

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