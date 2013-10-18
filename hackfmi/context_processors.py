from django.conf import settings


def constants(request):
    return {
        'MAX_UPLOAD_SIZE': settings.MAX_UPLOAD_SIZE,
        'MAX_UPLOAD_FILES': settings.MAX_UPLOAD_FILES,
    }
