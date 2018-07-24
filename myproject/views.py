from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from customEventHandler import CustomEventHandler
from myproject import properties

@csrf_exempt
def event(request):
    customEventHandler = CustomEventHandler(properties().getAppSecret(), properties().getAppId())
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
