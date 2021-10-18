from django.shortcuts import render, redirect
from .models import Names
from .forms import NamesForm
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import get_object_or_404


def index(request):
    error = ''
    coincidence = ''
    shipment = True
    names = Names.objects.order_by('name')
    if request.method == 'POST':
        form = NamesForm(request.POST)
        if form.is_valid():
            for el in names:
                if str(request.POST['name']) == str(el):
                    shipment = False
                    coincidence = el
            if shipment:
                form.save()
                shipment = True
                names = Names.objects.order_by('-id')
                return redirect('/' + str(names[0].id))
            if not shipment:
                return redirect('/' + str(coincidence.id))
        else:
            error = 'Форма была неверно заполнена'

    form = NamesForm

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/index.html', data)


class NewsDetailView(DetailView):
    model = Names
    template_name = 'main/office.html'
    context_object_name = 'personal'
