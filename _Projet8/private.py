import os

KEY = os.environ.get("DJANGO_KEY")#'84-d)vu-dnzpeddj2f18#_e!v&5=v$$3012(shh7m9aad0iac)'
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