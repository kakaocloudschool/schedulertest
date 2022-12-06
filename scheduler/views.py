from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from django.conf import settings
from .forms import JobForm, JobExecutionForm
from .models import DjangoJob,DjangoJobExecution,DjangoJobExecutionManager
from app.models import AppInfo


def jobadd(request, pk):
    #job = DjangoJob()
    job = get_object_or_404(AppInfo, pk=pk)
    if request.method=='POST':
        print("i'm here")
        form = JobForm(request.POST)
        if form.is_valid():
            job.id = form.cleaned_data["id"]
            job.app_name=form.cleaned_data["app_name"]
            job.next_run_time=form.cleaned_data["next_run_time"]
            #appinfo = AppInfo.objects.get(app_name=appinfo.app_name)
            print(job)
            print(1)
            job.save()

            redirect("schedulejob")
    else:
        print("hello")
        form = JobForm()


    return render(request, "jobadd.html", {"form": form})



def schedule(request):

    form = JobExecutionForm()

    return render(request, "schedulejob.html", {"form": form})

