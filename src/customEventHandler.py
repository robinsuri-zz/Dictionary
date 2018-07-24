from flockos import EventHandlerClient

from src import db, utils, properties


class CustomEventHandler(EventHandlerClient):

    def __init__(self, appSecret, appId):
        EventHandlerClient.__init__(self, appSecret, appId)
        self.on_app_install(self.handleInstall)
        self.on_app_uninstall(self.handleUninstall)
        self.on_client_slash_command(self.handleSlashCommand)

    def handleInstall(self, event):
        token = event.token
        userId = event.userId
        db.createUser(userId, token)

    # store info in db

    def handleUninstall(self, event):
        userId = event.userId
        db.deleteUser(userId)

    # remove info from db

    def handleSlashCommand(self, event):
        userId = event.userId
        utils.handleWord(event.text.strip(), userId, properties().getBotToken())
