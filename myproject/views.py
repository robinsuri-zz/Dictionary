from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from customEventHandler import CustomEventHandler

appSecret = "8f221431-7a5a-42a6-bc19-42713e40d155"
appId = "0951f74a-4e6a-4884-803c-b434453371ff"


def hello(request):
    return HttpResponse('hello')


@csrf_exempt
def event(request, **kwargs):
    print("Inside event")
    customEventHandler = CustomEventHandler(appSecret, appId)
    customEventHandler.handle(request)
