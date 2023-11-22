from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import redirect
from datetime import date
from .models import *

# Create your views here.
def index(request):
    return render(request, 'htmlpages/index.html')


@csrf_exempt
def loginpost(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get("password")
        try:
            user = Users.objects.get(username= username, password=password)
            if user:
                request.session['username'] = username
                return JsonResponse({'message': 'Login Credentials correct succesSSSSs'})
        except Users.DoesNotExist:
            return JsonResponse({"error": 'You have provided wrong credentialssssss'})




def welcome_view(request):
    username = request.session.get('username')
    if username:
        usertask = Task.objects.filter(user__username= username)
        context = {'username':username,'usertasks':usertask}
        return render(request, 'htmlpages/welcome.html',context)
    else:
        return JsonResponse({"error": 'SESSION TMEOUTTTTT'})
    

@csrf_exempt
def createtask(request):
    username = request.session.get('username')
    if request.method == 'POST':
        today_date = date.today()
        data = json.loads(request.body)
        task = data.get('task')
        user_instance = Users.objects.get(username=username)
        taskcreation = Task.objects.create(task_name= task,user=user_instance,status=0,date=today_date)
        return JsonResponse({'message': 'TASK CREATED SUCCSEFULLLLLLLY'})
    

@csrf_exempt
def updatetask(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        taskid = data.get('tasksid')
        taskdesc = data.get('taskdesc')
        taskstatus = data.get('taskstatus')

        task_instance = Task.objects.get(id=taskid)
        task_instance.task_name = taskdesc
        task_instance.status = taskstatus
        task_instance.save()

        return JsonResponse({'message': 'TASK UPDATEDDDDD SUCCSEFULLLLLLLY'})
    

@csrf_exempt
def deletetask(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        tasksid = data.get("tasksid")
        task_instance = get_object_or_404(Task, id=tasksid)
        task_instance.delete()
        return JsonResponse({'message': 'TASK DELETEDDDDD SUCCSEFULLLLLLLY'})
    


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        mobile = data.get('phone')
        user = Users.objects.create(username=username,password=password,phone=mobile)
        if user:
            request.session['username'] = username
            return JsonResponse({'message': 'USER CRETAED SUCCSEFULLLLLLLY'})
    else:
        return render(request, 'htmlpages/signup.html')





def logout(request):
    removed_value = request.session.pop('username')
    # print(f"Removed value: {removed_value}")
    return render(request, 'htmlpages/index.html')
        


