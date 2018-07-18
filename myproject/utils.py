from flockos import chat
from PyDictionary import PyDictionary

dictionary = PyDictionary()

def handleWord(word, guid, token):
    meaning = fetchOneMeaning(word)
    if (meaning == None):
        meaning = "Not Found"
    sendMessage(meaning, guid, token)


def fetchOneMeaning(word):
    try:
        dictMeaning = dictionary.meaning(word)
    except:
        return None
    return dictMeaning.values()[0][0]


def sendMessage(message, guid, token):
    chat.send_message(token=token, to=guid, text=message)
