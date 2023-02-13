from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from django.shortcuts import render, redirect
from .register_form import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")

        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name='registration/register.html', context={"register_form":form})


@login_required
def index(request):

    user = request.user
    context = {
        'tasks': user.task_set.all()
    }
    return render(request, 'tasks/tasks.html', context=context)


def detail(request, task_id):
    try:
        context ={
            'task': Task.objects.get(id=task_id)
        }

    except Task.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'tasks/one_task.html', context=context)


