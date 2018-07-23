from flockos import EventHandlerClient

from myproject import db


class CustomEventHandler(EventHandlerClient):

    def __init__(self, appSecret, appId):
        EventHandlerClient.__init__(self, appSecret, appId)
        self.on_app_install(self.handleInstall)
        self.on_app_uninstall(self.handleUninstall)

    def handleInstall(self, event):
        token = event.token
        userId = event.userId
        db.createUser(userId, token)

    # store info in db

    def handleUninstall(self, event):
        userId = event.userId
        db.deleteUser(userId)
    # remove info from db
