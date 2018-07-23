from flockos import EventHandlerClient


class CustomEventHandler(EventHandlerClient):

    def __init__(self, appSecret, appId):
        EventHandlerClient.__init__(self, appSecret, appId)
        self.on_app_install(self.handleInstall)
        self.on_app_uninstall(self.handleUninstall)

    def handleInstall(self, event):
        token = event.token
        userId = event.userId

    # store info in db
    
    def handleUninstall(self, event):
        userId = event.userId
    # remove info from db
