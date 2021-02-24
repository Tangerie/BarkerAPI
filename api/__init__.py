import requests
import api.modules.user as user

def getHeaders():
    headers = {}

    rows = """Host: my.barker.college
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11.2; rv:86.0) Gecko/20100101 Firefox/86.0
    Accept: application/json, text/plain, */*
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Referer: https://my.barker.college/overview
    Cookie: _ga_6549QH9MTM=GS1.1.1612296084.3.0.1612296084.0; _ga=GA1.2.1263843688.1612076477; ARRAffinity=75a5ecf066e1ab991b7b9f4759cea9c7adab263f0998dab8b5215eb30fe435dd; ARRAffinitySameSite=75a5ecf066e1ab991b7b9f4759cea9c7adab263f0998dab8b5215eb30fe435dd; .AspNetCore.Cookies=CfDJ8NmzZsN12gBJpLgsGReX77aEq05VqtWXAZE9mhA3j6IZmoaIL4d3zJmk4kxWl3FHYttz_XKyRqaOH3tR5TGJRUS-G2trT3vD4Irn4nOmIhcz8At-IVWE4xSWuw_sgR1ZIETJYb9DVYdB1VgQosY7qZHCKxPNYq0QAVRhY2-y-tjTgAcD8pWEVmw3UBimjzTdDhV7WSejowEh-veF7gIc4e0AVpUeWuKHsAXsHoC5MX7ih-U9jgG0OZtKdHbGeMvgWBYPsCuGd6p_gjl7a3tLPQxELL7n_AkQoVrEq1uEmS7A-QSJ2MV6silo9HW9iw23v80tr1TMoeYNXMdvBm-3v5L2LWgmoxHGj5lDFMqJ8Ibj9T4ZtHSg2NDgCXuw8pfqd-elOsDxk6tUFt9VNeMCcqwpb-6lh0hO8bP11uJ_qg7AuUcqpB5tag3rXrr5ezErx0NPJJt_jehtkE1qaC5QJVoxKfLrCyMd1-zM18FAp52JmU3lBuMHiSfQWdpYKnVxTU0iuVZ2mTcuaoUfuLcjIxJfoIxbXytGNh-sRaPZsy0OESA0ndRPPPMh-8h2rvxYTr7TSdR-b9a95mRpJKUD5pfDa4Mhf4j_Hwid_Ag41v8ljw5NWtcAPS3knDkrzhIpQIx8zy210-yEzDP7E0UCscpJGZ99zS5QmVEJoao3T6_sShTf5_ZBi1zFJZhsBLUeXHlr7ndBuIrRkEjN9N2bw768P3K_KUAihgC0Fjvntr794CF6td9V6tD_EPm03pm6Rx2sQUtIxQiwtU-KMDyzr5c4DTj-Ue7ZMNdyPwjhn17-hKwDAtAo7YiEGavbnNcsGGuExwTU-zd42mipi9445RhC0_TTw3YMp3AJeCKpzoyEcoo2-v9VC98JPRHG_NguAWBv1wRo_vDf9UeTeyP0eU6r1zP_bo5Jx3drQKNBYzVf1ehJcIj-GHT_ZAvLPOJ0EIIY82F7ZpLEmD5tLc-qklJJbCTzpjDfFULacKIrgzx6YdJB4tJsHVX-5ZewJwPSBQx2X9T3Z4OJ4Z2Tzt7-h6zgLrDoRcMvdH6mlU0c9z678mkuD03OjeuuJ6DhkD0KBsehWq9T8avS6Xy8VG-0IkilsSyNiSKlRsijongh5zpdjQimRd98OHX86Ututlme3J33w6ALdBEQo1OiQ8-b1BDGNvwQHZqLp1IvQSobUWmoHjPWBH8CX-6Oph0YLfOlnuFY_j00cEO5F47IwTzJR14UHlJkD67mmJBmvezGHMvoFDzhIHyVZ-C8wtrFNgn4UTmmduzPFDKUflnMqBCpfCnKsbcTxupuu89e5szCQXoBKcMXtAxvFDwjOZUdMLRxxYQqFq5HrBICkps2GxcD12aGlN69-HkPP7zqUSPQb-_Nzdv_1NE8lhzf8EYgz8Xz-b--J08OmKJS9Vf7WIW_TdtBM7u6ZayOwVIxlSQmH2qpPF-wXwPJE6DSgnbPKxnnzdXmhCtx6gAgYYvZQDaf98iNBtXTLTMhQQRnqjplb_h5nlkqzy80uHdIUnfsOVH0Y7CmVYiCV08kebIcdmG-OSiEhlTlXR6ki5CeL0R561j71IVQUR1h1CP-lXkgJgzQzJkZxVKrbHxpERUzLDx8eMo8u83aVhLfAkap0Nt9sEQZhYkepav0ynoQD98gjSCR_jWMpgMGOFbNMNlQ0tpmu1p-c6a2taN0Yod15zCDxjxfiyj83iKBbvCelwukXrCCEAJsfwT_2tzlSK6QQnvULi1UxkaG31eKx6VsqkkHLTVcoS47twV7Si0TB_FyvcW_R4fFVsiqVFgAGhBJLKoV8NONN8TzJnqhk5Z-S1M6fT4bdg3WW4c-_Z9AaEBMZWECyNl3FTTt5sdpxFO68U1RtDE1EYZypWwjosOMYqi4rhyQmRrCBzH2vnVrneSBOLhOtyBk_4NVbn0yWlzRAybhVRaBEUJdtCdos-QK9oNetwKCdn3IEHvZC2-CgClblxci_COb8oFoGvGy3viaq76tX7S3r-MdZoyc-1KfYsWSRs1Sotx7bOHF5TX3Bb9WnlNEoGZFrJpVfQTI_MzGsoqSjlNikGdVTxnidwtULeOvqJUrs-_NKqTpzzhZIUYRQ6MQRS8w0HN4-C_jDmVAPr3uJIVMRnIL5iX-NdlYLoBm9gDZuWXo6eCVN0cbSxzHQVkw42BBd7C-0IHI8G5A-dSF1_T33e1nmpBmaLD-xUpFT7FbeSJs3f2RxjfJnaKH-04bu_dkHqQ7dbhOROkSlMkcEin_ZC_gCo9kfaRma-Ho-HZorblPoOnUBLrNFA2xSV0bhn3kuOsynRaphTc6FGBZnjbjZDnht2IE7C-rEOfTnHUiiACKospNEaTv3UXtfxGSTMuQW13LBZL_sZenu44_xij-NA-3ZS-5wi459VPPUxDXIZAv00knYZoX-KJrCTH6XxpD0O6E8fvGdlt1dpOyUcKy-O9la2SPYjorpPsS9i1AkmG6_krSIbdbTpsQNfKZfQfR-MleAaHB173mu5mPsvZxksyaKM1j7-yWAW-0v2vdmiCOmZZDTfRxVzcLCAw2wtDJHlIGklkLZBzVYelzOgLV0uIr-m6iUbZ02bGywOlohd-RumThphEJS8bsoSQ5dNM_W4e3aDRmDjfDuljVoAaQkdDjXYwMfAv4Svcb4hrwJA83Bj41K1XD_dT59Gr17Y3IHEmbHD0jZR8AsgIEn4AXxPA3bfnf8hPc3FWEQZwjueW2RmDXwS5RMoOpudvmVSP9JpYNewhpJj4a-rVRmvMDaXaS1W1HceJi4XoZTl1KT7s1Xfzkpjk4P1x04HunF_2AIopWlEyfgJry3gbpIe9c3WbzbH2zk97Sig-IVdOiDwnV36oYZeP1rG3CYkdVBO5blhdOxgF7dqPxK7reWLzYdSqiDmGFG1lBzruHDGyFscKboLRLqTzQV-pOpgPzGuZVptIiy7xdQqErn1uab665VI-tmueDVUdVR3vpt6w30vUQJmvJwGIW7z6FrNkTvCCir4gGVIA7NBQV5UGUlX519bgONLVXM_LOJF34alh7Cz8-baz3yCMms7AkCMiDIu7kzgEJo6plBhJbYHv_EMIe9o45GUwYy0G5CTnCqerbCMv7z6kKPkxPTWPjbA6OjyRHOKVemtUTY_8PQ7JIfTT9WIunakpQu_e1qTaZOFLS5ygae0YCFWqpoIBNoiO2h1rb5wueZqNNSunBxNwMzSs
    Sec-GPC: 1
    Cache-Control: max-age=0
    TE: Trailers""".split("\n")

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