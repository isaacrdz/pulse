from django.shortcuts import render_to_response,get_object_or_404, render
from django.template.context import RequestContext
from models import *
from forms import * 
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def home(request):
    categorias = Categoria.objects.all()
    enlaces = Enlace.objects.order_by("-votos").all()
    template = "index.html"
    return render(request, template,{"categorias" : categorias, "enlaces":enlaces, "request":request})

def categoria(request,id_categoria):
    categorias = Categoria.objects.all()
    cat = get_object_or_404(Categoria,pk = id_categoria)
    #cat = Categoria.objects.get(pk = id_categoria)
    enlaces = Enlace.objects.filter(categoria = cat)
    template = "index.html"
    return render(request, template,locals())

@login_required
def minus(request,enlace_id):
    enlace = get_object_or_404(Enlace,pk=enlace_id)
    enlace.votos = enlace.votos - 1
    enlace.save()
    return HttpResponseRedirect("/")

@login_required
def plus(request,enlace_id):
    enlace = get_object_or_404(Enlace,pk=enlace_id)
    enlace.votos = enlace.votos + 1
    enlace.save()
    return HttpResponseRedirect("/")

@login_required
def add(request):
    if request.POST:
        form = EnlaceForm(request.POST)
        if form.is_valid():
            enlace = form.save(commit = False)
            enlace.usuario = request.user
            enlace.save()
            return HttpResponseRedirect("/")
    else:
        form = EnlaceForm()
    template = "form.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

from django.views.generic import ListView, DetailView

class EnlaceListView(ListView):
    model = Enlace
    context_object_name = 'enlaces'
    def get_template_names(self):
        return 'index.html'

class EnlaceDetailView(DetailView):
    model = Enlace
    def get_template_names(self):
        return 'index.html'

from rest_framework import viewsets
from .serializers import EnlaceSerializer, UserSerializer
from django.contrib.auth.models import User

class EnlaceViewSet(viewsets.ModelViewSet):
    queryset = Enlace.objects.all()
    serializer_class = EnlaceSerializer
    paginate_by = 10
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer