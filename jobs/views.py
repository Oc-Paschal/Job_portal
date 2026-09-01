from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job


@login_required
def create_job(request):
    if request.method == 'POST':
        Job.objects.create(
            employer=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            location=request.POST.get('location'),
            salary=request.POST.get('salary'),
            job_type=request.POST.get('job_type'),
            requirements=request.POST.get('requirements'),
            deadline=request.POST.get('deadline'),
        )

        return redirect('job_list')

    return render(request, 'jobs/create_job.html')


def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})