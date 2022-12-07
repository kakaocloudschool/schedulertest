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
    return render(request, "index.html")



@login_required
def schedule_list(request, pk):
    qs = DjangoJob.objects.all()
    if qs:
        qs = qs.filter(app_name__app_name__exact=pk)
    return render(request, "app/schedule_list.html", {"schedule_list": qs, "pk": pk})


def str_to_date(test):
    # print(test)

    if test.rfind('오후') == -1:
        test_str = test.replace('오전', '')
        test_date = test_str.replace('. ', )
        test_slice = test_date.replace('- ', ' ')
        test_join = ":".join((test_slice, '00'))
        if len(test_join) < 19:
            test_list = test_join.split()
            test_join = " 0".join(test_list)
    else:
        test_str = test.replace('오후', '')
        test_date = test_str.replace('. ', '-')
        test_slice = test_date.replace('- ', ' ')
        test_join = ":".join((test_slice, '00'))
        index1 = test_join.find(' ')
        if len(test_join) < 19:
            hour = int(test_join[index1+1:index1+2])
            hour += 12
            test_list = test_join[:index1+1]
            test_list2 = test_join[index1+2:]
            test_join = test_list + str(hour) + test_list2
        else:
            hour = int(test_join[index1+1:index1+3])
            hour += 12
            test_list = test_join[:index1+1]
            test_list2 = test_join[index1+3:]
            test_join = test_list + str(hour) + test_list2

    return test_join

@login_required
def new_schedule(request, pk):
    appinfo = get_object_or_404(AppInfo, pk=pk)
    print(pk)
    if request.method == 'POST':
        print(request.method)
        # form = SchedulerForm(request.POST)
        form = JobForm(request.POST, appinfo)
        form.app_name = pk
        # form = JobForm(request.POST)
        value = request.POST['next_run_time']
        date_value = str_to_date(value)

        print(form.next_run_time)
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

            return render(request, "app/schedule_list.html", {"pk": pk})
    else:
        print(request.method)
        # form = SchedulerForm()
        form = JobForm()
    return render(request, "app/new_schedule.html", {"form": form})







