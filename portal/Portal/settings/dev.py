from .common import *


DEBUG = True
SECRET_KEY = 'django-insecure-*m64rwzj!wgb%ejjtxc9n+p@^squ$95gtvjs-$npg%rd*nl*k_'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heavyard',
        'USER': 'admin',
        'PASSWORD': 'Softyard@12#',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
print('dev.py')
