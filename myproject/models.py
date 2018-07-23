from django.db import models


class User(models.Model):
    userId = models.CharField(max_length=20)
    userToken = models.CharField(max_length=100)

    def getUserId(self):
        return self.userId

    def getUserToken(self):
        return self.userToken
