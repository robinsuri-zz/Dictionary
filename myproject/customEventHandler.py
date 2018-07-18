from flockos import EventHandlerClient


class CustomEventHandler(EventHandlerClient):
    def __init__(self, appSecret, appId):
        EventHandlerClient.__init__(self, appSecret, appId)

    def on_app_install(self, handler):
        self.on_app_install_handler = handler

    def on_app_uninstall(self, handler):
        self.on_app_uninstall_handler = handler