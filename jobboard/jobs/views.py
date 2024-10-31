from django.shortcuts import render, redirect
from .models import Job

def add_job(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        description = request.POST.get('description')
        salary = request.POST.get('salary')
        salary_type = request.POST.get('salary_type')
        prerequisites = request.POST.get('prerequisites')
        
        job = Job(
            title=title,
            description=description,
            salary=salary,
            salary_type=salary_type,
            prerequisites=prerequisites
        )
        job.save()
        
        return redirect('job_list')
    
    return render(request, 'jobs/form.html')

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/index.html', {'jobs': jobs})