from flockos import EventHandlerClient


class CustomEventHandler(EventHandlerClient):

    def __init__(self, appSecret, appId):
        EventHandlerClient.__init__(self, appSecret, appId)
        self.on_app_install(self.handleInstall)
        self.on_app_uninstall_handler(self.handleUninstall)

    def handleInstall(self, request):
        print("Install")

    # store info in db

    def handleUninstall(self, request):
        print("Uninstall")
    # remove info from db
