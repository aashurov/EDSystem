import random
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from customer.models import *
from staff.models import *
from datetime import date, datetime
