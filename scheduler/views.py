from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

from django.conf import settings
from .forms import JobForm, JobExecutionForm
from .models import DjangoJob,DjangoJobExecution,DjangoJobExecutionManager
from app.models import AppInfo
from datetime import datetime


def scheduler(request, pk):
    #     if request.method == "POST":
    #         form = SchedulerForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             scheduler = Scheduler()
    #
    #             current_time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")  # 현재시간을 datetime으로 변환
    #             day_limit = (current_time + timedelta(days)).date()  # 현재시간에 기간 날짜수를 더하기
    #
    #             scheduler.user_id = request.user.id
    #             # scheduler, result_code, msg = chk_and_register_cluster(scheduler)
    #             if result_code == -1:
    #                 messages.error(request, msg)
    #             else:
    #                 messages.success(request, "클러스터 생성 성공.")
    #                 cluster.save()
    #                 return redirect("scheduler")
    #     else:
    #         form = SchedulerForm()
    return render(request, "test2.html")



@login_required
def schedule_list(request, pk):
    qs = DjangoJob.objects.all()
    print(qs)
    print(pk)
    if qs:
        qs = qs.filter(app_name__app_name__exact=pk)
    return render(request, "app/schedule_list.html", {"schedule_list": qs, "pk": pk})


@login_required
def new_schedule(request, pk):
    appinfo = get_object_or_404(AppInfo, pk=pk)
    print(pk)
    if request.method == 'POST':
        print(request.method)
        # form = SchedulerForm(request.POST)
        form = JobForm(request.POST, appinfo)
        form.app_name = pk

        if form.is_valid():
            print("1")
            # scheduler = Scheduler()
            job = DjangoJob()
            # scheduler.schedule_dt = form.cleaned_data["schedule_dt"]
            # scheduler.deploy_type = form.cleaned_data["deploy_type"]
            # scheduler.user_id = request.user.id
            #
            # scheduler.save()
            # return redirect("schedule_list")
            print(form.cleaned_data["next_run_time"])
            job.next_run_time = form.cleaned_data["next_run_time"]
            job.deploy_type = form.cleaned_data["deploy_type"]
            job.save()

            redirect("scheduler")

    else:
        print(request.method)
        # form = SchedulerForm()
        form = JobForm()
    return render(request, "app/new_schedule.html", {"form": form})







