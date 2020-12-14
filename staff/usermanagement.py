from django.shortcuts import render, redirect
from userprofile.forms import *
from userprofile.models import *


def createuser(request):
    form = UserForm(request.POST)
    if form.is_valid():
        form.save()
        obj = User.objects.latest('id')
        profile = UserProfile.objects.get(user_id=obj)
        profile.role = request.POST['role']
        profile.phone_number = request.POST['username']
        profile.save()
        if request.POST['role'] == 'клиент':
            return redirect('stafflistuser')
        elif request.POST['role'] == 'курер':
            return redirect('stafflistcourier')
    else:
        form = UserForm()
    return render(request, 'staff/signup.html', {'form': form})


def listcourier(request):
    listcouriers = User.objects.filter(userprofile__role__in=['курер'])
    return render(request, 'staff/listcourier.html', {"listcouriers": listcouriers})


def listuser(request):
    listusers = User.objects.filter(userprofile__role__in=['клиент'])
    return render(request, 'staff/listuser.html', {"listusers": listusers})


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
    user = User.objects.get(pk=user_id)
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        p_form = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=profile)
        u_form = UserUpdateForm(request.POST, instance=user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            redirect('staffediteuser', user_id=user_id)
        else:
            print(u_form.errors + p_form.errors)
    else:
        p_form = ProfileUpdateForm(instance=profile)
        u_form = UserUpdateForm(instance=user)
        profile = UserProfile.objects.get(user=user)
        user = User.objects.get(pk=user_id)
    return render(request, 'staff/profile.html', {"u_form": u_form, "p_form": p_form, "user": user, "profile": profile})


def listcustomermoney(request):
    customeraccount = CustomerAccount.objects.filter(user__userprofile__role='клиент').exclude(usd=0).order_by('-usd')
    return render(request, 'staff/listcustomermoney.html', {"customercashsums": customeraccount})


def listcustomerloan(request):
    customerloans = CustomerLoan.objects.filter(user__userprofile__role='клиент').exclude(usd=0).order_by('-usd')
    return render(request, 'staff/listcustomerloan.html', {"customerloans": customerloans})
