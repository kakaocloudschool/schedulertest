from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from django.conf import settings
from .forms import JobForm, JobExecutionForm
from .models import DjangoJob,DjangoJobExecution,DjangoJobExecutionManager
from app.models import AppInfo


def jobadd(request, pk):
    job = DjangoJob()
    appinfo = get_object_or_404(AppInfo, pk=pk)

    if request.method=='POST':

        form = JobForm(request.POST,appinfo)
        if form.is_valid():
            job.id = form.cleaned_data["id"]

            job.next_run_time=form.cleaned_data["next_run_time"]
            #appinfo = AppInfo.objects.get(app_name=appinfo.app_name)
            print(appinfo.app_name)

            job.save()

            redirect("schedulejob")
    else:
        print("get")
        form = JobForm()


    return render(request, "jobadd.html", {"form": form})




#def history_app(request, q):
#    qs = AppDeployHistory.objects.all()
#    # q = request.GET.get("q", "")
#    if qs:
#        qs = qs.filter(app_name__app_name__exact=q)
#    return render(request, "app/deploy_history.html", {"deploy_history": qs})

@login_required
def schedule_history(request):
    qs = DjangoJob.objects.all()
    # q = request.GET.get("q", "")
    #if qs:
    #    qs = qs.filter(app_name__app_name__exact=q)


    return render(request, "scheduler.html", {"schedule_history": qs})

