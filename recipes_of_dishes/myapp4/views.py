import logging

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import UserForm, ManyFieldsForm, ManyFieldsFormWidget
from .models import User
from .forms import ImageForm


logger = logging.getLogger(__name__)

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Get {name=}, {email=}, {age=}.')
        
    else:
        form = UserForm()
    return render(request, 'myapp4/user_form.html', {'form': form})

def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            logger.info(f'Get {form.cleaned_data=}')
    else:
        form = ManyFieldsForm()
    return render(request, 'myapp4/many_fields_form.html', {'form': form})
# Create your views here.

def many_fields_form_widget(request):
    if request.method == 'POST':
        form = ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            logger.info(f'Get {form.cleaned_data=}')
    else:
        form = ManyFieldsFormWidget()
    return render(request, 'myapp4/many_fields_form_widget.html', {'form': form})
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Error in data'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Get {name=}, {email=}, {age=}')
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'User is saved'
    else:
        form = UserForm()
        message = 'Fill form'
    return render(request, 'myapp4/user_form.html', {'form': form, 'message': message})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp4/upload_image.html', {'form': form})