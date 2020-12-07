from django.shortcuts import render, redirect
from customer.models import *
from customer.forms import CustomerAccountForm, CustomerLoanForm
from django.db import connection
from main.models import *
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm
from userprofile.forms import ProfileUpdateForm, UserUpdateForm
from userprofile.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def createuser(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        obj = User.objects.latest('id')
        profile = UserProfile.objects.get(user_id=obj)
        profile.role = request.POST['role']
        profile.save()
        if request.POST['role'] == 'клиент':
            return redirect('stafflistuser')
        elif request.POST['role'] == 'курер':
            return redirect('stafflistcourier')
    else:
        form = UserCreationForm()
    return render(request, 'staff/signup.html', {'form': form})

#
# def profile(request, user_id):
#     print("saaslom")
#     if request.method == 'POST':
#         p_form = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=request.user.profile)
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         print(p_form['passport_date_first'])
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             print("salomZOR")
#             redirect('profile', user_id=user_id)
#     else:
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#         u_form = UserUpdateForm(instance=request.user)
#     return render(request, 'main/profile.html', {"u_form": u_form, "p_form": p_form})


def listcourier(request):
    listcouriers = User.objects.filter(userprofile__role__in=['курер'])
    return render(request, 'staff/listcourier.html', {"listcouriers": listcouriers})


def listuser(request):
    listusers = User.objects.filter(userprofile__role__in=['клиент'])
    # listusers = Profile.objects.filter(role='клиент').select_related('user')
    page = request.GET.get('page', 1)
    paginator = Paginator(listusers, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'staff/listuser.html', {"users": users})


def deleteuser(request, user_id):
    get_user = User.objects.get(pk=user_id)
    get_userprofile = UserProfile.objects.get(user_id=user_id)
    get_usercashsum = CustomerAccount.objects.get(user_id=user_id)
    get_userloansum = CustomerLoan.objects.get(user_id=user_id)
    get_user.delete()
    get_userprofile.delete()
    get_usercashsum.delete()
    get_userloansum.delete()
    return redirect('stafflistuser')


def edituser(request, user_id):
    # print("222")
    user = User.objects.get(pk=user_id)
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=profile)
        u_form = UserUpdateForm(request.POST, instance=user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # print("salomZOR")
            redirect('staffediteuser', user_id=user_id)
        else: print(u_form.errors + p_form.errors)
    else:
        p_form = ProfileUpdateForm(instance=profile)
        u_form = UserUpdateForm(instance=user)
        profile = UserProfile.objects.get(user=user)
        user = User.objects.get(pk=user_id)
    return render(request, 'staff/profile.html', {"u_form": u_form, "p_form": p_form, "user": user, "profile": profile})


def listcustomermoney(request):
    customeraccount = CustomerAccount.objects.filter(user__userprofile__role='клиент')
    return render(request, 'staff/listcustomermoney.html', {"customercashsums": customeraccount})


def listcustomerloan(request):
    customerloans = CustomerLoan.objects.filter(user__userprofile__role='клиент')
    return render(request, 'staff/listcustomerloan.html', {"customerloans": customerloans})