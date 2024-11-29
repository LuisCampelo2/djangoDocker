from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect,get_object_or_404
from home.forms import * # Certifique-se de que o formulário esteja importado corretamente.
from django.contrib import messages,auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def cadastrar_user(request):
    form_action = reverse('home:cadastro')

    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados do formulário no banco.
            # Você pode redirecionar ou enviar uma mensagem de sucesso aqui.
            return redirect('home:index')  # Exemplo de redirecionamento após o cadastro.

    else:
        form = RegisterUser()  # Cria um formulário vazio para exibir no método GET.

    context = {
        'form': form,
        'form_action': form_action
    }

    return render(request, 'home/pages/cadastro.html', context)

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('home:index')


    return render(
        request,
        'home/pages/login.html',
        {
            'form': form
        }
    )

@login_required(login_url='home:login')
def logout_view(request):
    auth.logout(request)
    return redirect('home:login')

@login_required(login_url='home:login')
def update_view(request):
    form = RegisterUpdateForm(instance=request.user)

    form_action=reverse('home:update_view')

    context={
        'form': form,
        'form_action': form_action
    }

    if request.method != 'POST':
        return render(
            request,
            'home/pages/update.html',
            context
        )

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'home/pages/update.html',
            context
        )

    form.save()
    return redirect('home:update')

#views

def index(request):
    return render(request,'home/pages/index.html')


@login_required(login_url='home:login')
def meu_perfil(request): 
    return render(request,'home/pages/perfil.html')
