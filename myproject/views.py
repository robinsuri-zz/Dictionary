from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from customEventHandler import CustomEventHandler

appSecret = "8f221431-7a5a-42a6-bc19-42713e40d155"
appId = "0951f74a-4e6a-4884-803c-b434453371ff"


def hello(request):
    return HttpResponse('hello')


@csrf_exempt
def event(request):
    customEventHandler = CustomEventHandler(appSecret, appId)
    httpResponse = HttpResponse(content='', status=500, content_type='application/json')

    def start_response(status, headers):
        global httpResponse
        if (status == '200 OK'):
            print("Inside start_response")
            httpResponse = HttpResponse(content='', status=200, content_type='application/json')
        else:
            httpResponse = HttpResponse(content='', status=500, content_type='application/json')

    environ = request.environ
    customEventHandler.handle(environ, start_response)
    return httpResponse
