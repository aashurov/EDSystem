from django.shortcuts import render, redirect


# Create your views here.
def staff(request):
    return render(request, 'staff/dashboard.html')