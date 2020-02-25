from main.models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from datetime import datetime

def user(request, uname, pas, em, fname, lname, month, day, year):
    u = User(username = uname, password = make_password(pas), email = em, first_name = fname, last_name = lname)
    u.save()
    up = UserProfile(user = u, description = '', dob = datetime.strptime(str(month_string_to_number(month)) + str("/" + day) + str("/" + year), '%m/%d/%Y').date())
    up.save()

def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
         'may': 5,
         'jun': 6,
         'jul': 7,
         'aug': 8,
         'sep': 9,
         'oct': 10,
         'nov': 11,
         'dec': 12
        }
    s = string.strip()[:3].lower()

    return m[s]
