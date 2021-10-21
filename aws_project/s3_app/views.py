from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ObjectForm
from .models import s3Object

import boto3

s3 = boto3.resource(
    service_name='s3',
    region_name='us-west-2',
    aws_access_key_id='AKIAXF2CYLXHERZWCBUW',
    aws_secret_access_key='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'
)

class Home(TemplateView):
    template_name = 'home.html'

@login_required
def list_objects(request):
    if request.user.is_superuser:
        objects = s3Object.objects.all()
    else:
        objects = s3Object.objects.filter(author_id = request.user.id)
    return render(request, 'list_objects.html', {
        'storage': objects
    })

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = ObjectForm(request.POST, request.FILES)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.author = request.user
            form.save()
            messages.success(request, f'File Uploaded Successfully !')
            return redirect('list_objects')
    else:
        form = ObjectForm()
    return render(request, 'upload_file.html', {
        'form': form
    })

@login_required
def update_file(request, pk):
    file_object = s3Object.objects.get(id=pk)
    form = ObjectForm(instance=file_object)
    if request.method == "POST":
        form = ObjectForm(request.POST, request.FILES, instance=file_object)
        if form.is_valid():
            form.save()
            messages.success(request, f'File Updated Successfully !')
            return redirect('list_objects')
    else:
        form = ObjectForm()
    return render(request, 'update_file.html', {
        'form': form
    })


@login_required
def delete_file(request, pk):
    if request.method == 'POST':
        file_object = s3Object.objects.get(pk=pk)
        file_object.delete()
        messages.success(request, f'File Deleted Successfully !')
    return redirect('list_objects')


@login_required
def list_buckets(request):
    my_buckets = s3.buckets.all()
    return render(request, 'list_buckets.html', {'my_buckets': my_buckets})


