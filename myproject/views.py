from django.http import HttpResponse
from customEventHandler import CustomEventHandler
appSecret ="8f221431-7a5a-42a6-bc19-42713e40d155"
appId ="0951f74a-4e6a-4884-803c-b434453371ff"
def hello(request):
    return HttpResponse('hello')
def event(request, response) :
    customEventHandler = CustomEventHandler(appSecret, appId)
    customEventHandler.handle(request, response)

