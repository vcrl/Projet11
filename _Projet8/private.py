import os

KEY = os.environ.get("DJANGO_KEY")
DB = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'projet_8',
        'USER': 'postgres',
        'PASSWORD' : '123',
        'HOST': 'localhost',
        'PORT': '5432' 
    }
}