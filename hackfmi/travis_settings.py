import sys

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'testdb',
        'USER':     'postgres',
        'PASSWORD': '',
        'HOST':     'localhost',
        'PORT':     '',
    }
}

SOUTH_TESTS_MIGRATE = False  # To disable migrations and use syncdb instead
SKIP_SOUTH_TESTS = True  # To disable South's own unit tests
USE_DEBUG_TOOLBAR = False

if len(sys.argv) > 1 and 'test' in sys.argv[1]:
    AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)
