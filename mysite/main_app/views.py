from django.shortcuts import render, redirect
from .forms import WidgetForm
from .models import Widget
from django.views.generic.edit import DeleteView

# Create your views here.


def index(request):
    widget_form = WidgetForm()
    form = WidgetForm(request.POST)
    widgets = Widget.objects.all()
    if form.is_valid():
        widget = form.save(commit=False)
        # widget_id = request.user.id
        widget.save()
        return redirect('index')

    return render(request, 'index.html', {'widget_form': widget_form, 'widgets': widgets})


class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'
