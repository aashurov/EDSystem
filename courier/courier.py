from django.shortcuts import render


# Create your views here.
def courier(request):
    return render(request, 'courier/dashboard.html')