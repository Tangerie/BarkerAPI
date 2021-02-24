import api

def getDetails():
    return api.getJson("UserDetail/GetUserDetails")

def getName():
    return getDetails()["userName"]

def getGroups():
    return getDetails()["userGroups"]

def getId():
    return getDetails()["userId"]