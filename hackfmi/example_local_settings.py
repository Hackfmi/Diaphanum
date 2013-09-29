DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'viki',
        'USER': 'Viki',
        'PASSWORD': 'test',
        'HOST': '',
        'PORT': '5432',
    }
}

# Change to true to enable Django Debug Toolbar
USE_DEBUG_TOOLBAR = False