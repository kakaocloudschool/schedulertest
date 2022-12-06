from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from django.conf import settings
from .forms import JobForm, JobExecutionForm, SchedulerForm
from .models import DjangoJob,DjangoJobExecution,DjangoJobExecutionManager, Scheduler
from app.models import AppInfo


def scheduler(request, pk):
    qs = Scheduler.objects.all()
    if qs:
        qs = qs.filter(app_name__app_name__exact=pk)
    return render(request, "app/schedule_list.html", {"scheduler": qs})

@login_required
def schedule_list(request, pk):
    qs = Scheduler.objects.all()
    if qs:
        qs = qs.filter(app_name__app_name__exact=pk)
    return render(request, "app/schedule_list.html", {"schedule_list": qs})


@login_required
def new_schedule(request):
    if request.method == "POST":
        form = SchedulerForm(request.POST, request.FILES)
        if form.is_valid():
            scheduler = Scheduler()
            scheduler.cluster_name = form.cleaned_data["cluster_name"]
            scheduler.kubeconfig = form.cleaned_data["kubeconfig"]
            scheduler.bearer_token = form.cleaned_data["bearer_token"]
            scheduler.user_id = request.user.id
            # scheduler, result_code, msg = chk_and_register_cluster(scheduler)
            if result_code == -1:
                messages.error(request, msg)
            else:
                messages.success(request, "클러스터 생성 성공.")
                cluster.save()
                return redirect("scheduler")
    else:
        form = SchedulerForm()
    return render(request, "app/new_schedule.html", {"form": form})

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


    return render(request, "schedule_list.html", {"schedule_history": qs})

