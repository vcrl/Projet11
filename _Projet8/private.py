import os

KEY = '84-d)vu-dnzpeddj2f18#_e!v&5=v$$3012(shh7m9aad0iac)'#os.environ.get("DJANGO_KEY")
DB = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',#os.environ.get("DB_ENGINE"),
        'NAME': 'projet_8',#os.environ.get("DB_NAME"),
        'USER': 'postgres',#os.environ.get("DB_USER"),
        'PASSWORD' : '123',#os.environ.get("DB_PASSWORD"),
        'HOST': 'localhost',#os.environ.get("DB_HOST"),
        'PORT': '5432'#os.environ.get("DB_PORT") 
    }
}