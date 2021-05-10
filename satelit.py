import requests
import json
from collections import namedtuple
from datetime import datetime
from datetime import timedelta
import pytz


def customSatelitDecoder(satelitDict):
    return namedtuple('X', satelitDict.keys())(*satelitDict.values())


def customTimeDecoder(timeDict):
    return namedtuple('X', timeDict.keys())(*timeDict.values())


def getSatelitData():
    url_satelit = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url=url_satelit)
    data_satelit = json.loads(response.text, object_hook=customSatelitDecoder)
    return data_satelit


def getTimeLocationData(latitude, longitude):
    url_time = 'https://api.sunrise-sunset.org/json?lat=' + latitude + '&lng=' + longitude + '&formatted=0'
    time_res = requests.get(url=url_time);
    time_data = json.loads(time_res.text, object_hook=customTimeDecoder)
    return time_data




satelit_data = getSatelitData()

print("Souřadnice satelitu: Zeměpisná šířka %f; Zeměpisná délka %f " % (float(satelit_data.iss_position.latitude),  float(satelit_data.iss_position.longitude)))

time_data = getTimeLocationData(satelit_data.iss_position.latitude, satelit_data.iss_position.longitude)

#získání hodnoty východu a západu slunce z dat získaných z rest serveru
sunrise_datetime =  datetime.fromisoformat(time_data.results.sunrise)
valid_sunrise = datetime(sunrise_datetime.year, sunrise_datetime.month, sunrise_datetime.day, sunrise_datetime.hour, sunrise_datetime.minute, sunrise_datetime.second)

sunset_datetime = datetime.fromisoformat(time_data.results.sunset)
valid_sunset = datetime(sunset_datetime.year, sunset_datetime.month, sunset_datetime.day, sunset_datetime.hour, sunset_datetime.minute, sunset_datetime.second)

#získání času z údajů satelit v UTC+0
formated_time = datetime.fromtimestamp(satelit_data.timestamp, pytz.UTC)
current_time = datetime(formated_time.year, formated_time.month, formated_time.day, formated_time.hour,
                        formated_time.minute, formated_time.second)


noc = False

#Pokud je aktuální čas mezi časovým úsekem východu a zápodu slunce je den naopak noc
if (current_time > valid_sunrise and current_time < valid_sunset):
    print("Den")
else:
    print("Noc")
    noc = True

#Výpočet zda je satelit v pozici, kdy je na souřadnicích 60 až 120 minut po západu slunce
#nebo zad je 60 až 120 minut před východem slunce
cur_minute = (current_time.hour * 60) + current_time.minute
valid_sunrise_minute = (valid_sunrise.hour * 60) + valid_sunrise.minute
valid_sunset_minute = (valid_sunset.hour * 60) + valid_sunset.minute

ideal_sunrise = abs(cur_minute - valid_sunrise_minute)
ideal_sunset = abs(cur_minute - valid_sunset_minute)


if (noc == True):
    if (ideal_sunset > 60 and ideal_sunset < 120 or ideal_sunrise > 60 and ideal_sunrise < 120):
        print("Vhodna pozice pro pozorovani")
    else:
        print("Spatna pozice pro pozorovani")
else:
    print("Spatna pozice pro sledovani")
