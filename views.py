from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
from registro.models import Consulta
from datetime import date, timedelta, datetime


from .models import Consulta

# Create your views here.
def index(request):
    #if request.user.is_authenticated:
    return render(request, 'index.html')
    #else:
    #    return HttpResponse('LOGA CARAI')


def CalendarioView(request):
    
    hoje = date.today()
    primeiro_dia = date(hoje.year, hoje.month, 1)
    ultimo_dia = date(hoje.year, hoje.month + 1, 1) - timedelta(days=1)
    
    dias_do_mes = [primeiro_dia + timedelta(days=i) for i in range((ultimo_dia - primeiro_dia).days + 1)]

    consultas = Consulta.objects.filter(data__month=hoje.month, data__year=hoje.year)
    
    consultas_por_dia = {}

    for dia in dias_do_mes:
        consultas_por_dia[dia] = consultas.filter(data=dia)  
    
    semanas = []
    semana = []
    for dia in dias_do_mes:
        semana.append(dia)
        if dia.weekday() == 6:  # Domingo, fim da semana
            semanas.append(semana)
            semana = []
    num_branco = 7 - len(semanas[0])
    for i in range(num_branco):
        semanas[0].insert(0,'')
    if semana:  # Adiciona a última semana
        semanas.append(semana)

    context = {
        'semanas': semanas,
        'consultas_por_dia': consultas_por_dia,
        
    }
    return render(request, 'calendario.html', context)



def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        

        user = User.objects.filter(username=username).first()
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse('DEU MANO')


def LoginView(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return render(request, 'index.html')
        else:
            return HttpResponse('DEU MERDA MANO')
        
def LogoutView(request):
    logout(request)
    return redirect('index') 