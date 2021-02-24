import requests, api

with open("headers.txt", "r", encoding="utf8") as fp:
    api.HEADERS = fp.read()

print(api.user.getId())
