import requests


def getLatestCountryDataByName(name):
    url = "https://covid-19-data.p.rapidapi.com/country"

    querystring = {"name":name}

    headers = {
        'x-rapidapi-key': "c64477f5cemshc55c6ce39045df2p1e9929jsn5f773e90b280",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    confirmed = (response.text).split(",")[2][12:]
    recovered =(response.text).split(",")[3][12:]
    critical =(response.text).split(",")[4][11:]
    deaths = (response.text).split(",")[5][9:]

    return confirmed,recovered,critical,deaths


def getLatestCountryData():
    url = "https://covid-19-data.p.rapidapi.com/totals"

    headers = {
        'x-rapidapi-key': "c64477f5cemshc55c6ce39045df2p1e9929jsn5f773e90b280",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    confirmed = (response.text).split(",")[0][14:]
    recovered =(response.text).split(",")[1][12:]
    critical =(response.text).split(",")[2][11:]
    deaths = (response.text).split(",")[3][9:]
    
    return confirmed,recovered,critical,deaths