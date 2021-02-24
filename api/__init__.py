import requests
import api.modules.user as user

HEADERS = ""

def getHeaders():
    if HEADERS == "":
        print("NO HEADERS SUPPLIED")
        return {}
    headers = {}

    rows = HEADERS.split("\n")

    headers = {key.strip(): val.strip() for key, val in [val.split(": ", 1) for val in rows]}

    return headers

def getUrl(path, params={}):
    headers = getHeaders()
    reqURL = "https://my.barker.college/api/" + path
    return requests.get(reqURL, headers=getHeaders(), params=params)

def getRaw(path, params={}):
    return getUrl(path, params).text

def getJson(path, params={}):
    return getUrl(path, params).json()

def getAvatarUrl():
    return getRaw("UserDetail/GetUserAvatar")

def getFavouriteList():
    return getJson("Favourite/List")

def getPagedNotification(returnData=0, pageSize=20, page=1):
    return getJson("UserNotifications/GetPaged", {"returnData": returnData, "pageSize": pageSize, "page": page})

def getNotices(perPage=10, page=1):
    return getJson("Notices/GetNotices", {"perPage": perPage, "page": page})

def getTimetable(start, end): #FORMAT THESE
    return getJson("Student/GetTimetable", {"start": start, "end": end})

def getCoCurricularUpcoming(start, end): #FORMAT THESE
    return getJson("Student/GetCoCurricularUpcoming", {"start": start, "end": end})

def getPlannerItems(completed=False):
    return getJson("Todo/GetPlannerItemsByUserId", {"completed": completed})

def getForms():
    return getJson("Todo/GetMyFormsByUserId")

def getSuggested():
    return getJson("Content/GetSuggested")