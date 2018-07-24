from flockos import chat
from PyDictionary import PyDictionary


def handleWord(word, guid, token):
    meaning = fetchOneMeaning(word)
    if (meaning == None):
        meaning = "Not Found"
    sendMessage(meaning, guid, token)


def fetchOneMeaning(word):
    dictionary = PyDictionary()
    try:
        dictMeaning = dictionary.meaning(word)
    except:
        return None
    return dictMeaning.values()[0][0]


def sendMessage(message, guid, token):
    response = chat.send_message(token=token, to=guid.encode('ascii'), text=message)
