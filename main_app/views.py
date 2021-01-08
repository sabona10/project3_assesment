from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm

# Create your views here.

def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets,'widget_form':widget_form})

def create_widget(request):
    # widgets = Widget.objects.all()
    return redirect('index')

def delete_widget(request, widget_id):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widgets})