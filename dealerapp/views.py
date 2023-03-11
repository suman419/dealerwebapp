from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from .models import *
from .forms import DealerForm
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import User


class DealerListView(View):
    def get(self, request):
        form = DealerForm()
        return render(request, 'index.html', { 'form':form})
    #template_name = 'index.html'
    #model = Dealer
    #context_object_name = 'dealers'

    def post(self, request):
        form = DealerForm(request.POST, request.FILES)
        if form.is_valid():
            dealer_obj =form.save()
            return redirect('/success')
        else:
            form = DealerForm()
        return render(request, 'success.html', {'form':form,})

def success(request):
    last_register_dealer =Dealer.objects.last()
    return render(request,'success.html',{'last_register_dealer':last_register_dealer})

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')


@login_required(login_url='login')
def list_dealer(request):
    user_name =request.user
    name = str(user_name).replace("_sdo","")
    anumandal=name
    list_dealers= Dealer.objects.filter(anumandal__name=anumandal)
    dealer_count= Dealer.objects.filter(anumandal__name=anumandal).count()
    #list_dealers = list_dealers.filter()
    query = request.GET.get("q")
    if query:
        list_dealers = list_dealers.filter(Q(full_name__icontains=query)|Q(block__name__icontains=query)|Q(panchayat__name__icontains=query)).distinct()
    paginator=Paginator(list_dealers,5)
    page_number=request.GET.get('page',1)
    try:
        list_dealers=paginator.page(page_number)
    except PageNotAnInteger:
        list_dealers=paginator.page(1)
    except EmptyPage:
        list_dealers=paginator.page(paginator.num_pages)
    return render(request,'list_dealer.html', {'list_dealers':list_dealers,'dealer_count':dealer_count })

@login_required(login_url='login')
def Dealer_detail(request, pk):
    dealer_detail = Dealer.objects.get(pk=pk)
    return render(request, 'dealer_detail.html', {'dealer_detail':dealer_detail})


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'accounts/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render (request,'accounts/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('dealerlist')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request, "You have successfully logged out.")
    return redirect('logout')

def load_blocks(request):
    anumandal_id = request.GET.get('anumandal')
    blocks = Block.objects.filter(anumandal_id=anumandal_id).order_by('name')
    context = {'blocks': blocks}
    return render(request, 'block_dropdown_list_options.html', context)

def load_panchayats(request):
    block_id = request.GET.get('block')
    panchayats = Panchayat.objects.filter(block_id=block_id).order_by('name')
    context = {'panchayats': panchayats}
    return render(request, 'panchayat_dropdown_list.html', context)
