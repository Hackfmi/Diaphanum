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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "example@gmail.com"
EMAIL_HOST_PASSWORD = "examplepassword"
EMAIL_USE_TLS = True

# Change to true to enable Django Debug Toolbar
USE_DEBUG_TOOLBAR = False
