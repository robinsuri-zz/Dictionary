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
    statusCode = {'status': 200}

    def start_response(status, headers):
        if (status == '200 OK'):
            statusCode['status'] = 200
        else:
            statusCode['status'] = 500

    environ = request.environ
    customEventHandler.handle(environ, start_response)
    status = statusCode['status']
    return HttpResponse(content='', status=status, content_type='application/json')
