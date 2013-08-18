import json

from django.http import HttpResponse


class JsonResponse(HttpResponse):
    def __init__(self, content, status=None):
        super(JsonResponse, self).__init__(json.dumps(content), status=status,
            mimetype='application/json')


class JsonpResponse(HttpResponse):
    def __init__(self, content, callback, status=None):
        content = '%s(%s);' % (callback, json.dumps(content))
        super(JsonpResponse, self).__init__(content, status=status,
            mimetype='application/javascript')


def json_view(func):
    def view(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        if isinstance(response, HttpResponse):
            return response
        return JsonResponse(response)
    return view


def jsonp_view(func):
    def view(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        if isinstance(response, HttpResponse):
            return response
        return JsonpResponse(response, callback=request.GET.get('callback'))
    return view