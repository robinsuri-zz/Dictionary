from myproject.models import User


def fetchUserToken(userId):
    user = User.objects.get(userId=userId)
    return user.getUserToken()


def createUser(userId, token):
    user = User(userId=userId, userToken=token)
    user.save()


def deleteUser(userId):
    user = User.objects.get(userId=userId)
    user.delete()
