import os
import dj_database_url
from pickle import FALSE
from .common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ['35.182.169.92','.vercel.app', '127.0.0.1']
DATABASES = {}
}
print('prod.py')
