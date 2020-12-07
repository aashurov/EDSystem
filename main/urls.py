from django.urls import path
from userprofile.userprofile import *
from customer.customer import *
from staff.staff import *
from courier.courier import *

urlpatterns = [
    path('', index, name='index'),
    path('login/',  ulogin, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('profile/<int:user_id>', profile, name='profile'),
    path('profile/password', password, name='password'),

    path('customer/', customer, name='customer'),
    path('courier/', courier, name='courier'),
    path('staff/', staff, name='staff'),
]
