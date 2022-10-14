#Tool Created by Kevin Deep
#modules required
import argparse
import requests, json
import sys
from sys import argv
import os

#arguments and parser

parser = argparse.ArgumentParser()



args = parser.parse_args()

#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner of script
print (lgreen+bold+"""

▀█▀ ░█▀▀█ ── ░█▀▀▀ ▀▄░▄▀ ▀▀█▀▀ ░█▀▀█ ░█▀▀▀ ░█▀▄▀█ ░█▀▀▀ 
░█─ ░█▄▄█ ▀▀ ░█▀▀▀ ─░█── ─░█── ░█▄▄▀ ░█▀▀▀ ░█░█░█ ░█▀▀▀ 
▄█▄ ░█─── ── ░█▄▄▄ ▄▀░▀▄ ─░█── ░█─░█ ░█▄▄▄ ░█──░█ ░█▄▄▄
                                             Kevin Deep
"""+lgreen+bold)
print (lgreen+bold+" <===[[Tool Created By Kevin Deep]]===> \n"+lgreen+bold)




api = "https://ip-api.io/json/"

try:
        ip = input("\033[0;32mLocate The IP Address: \033[0;32m" )
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold
        b = lgreen+bold
        print("")
        print (a, "[Address IP]      >"  , data['ip'])
        print (a, "[Country Name]    >"  , data['country_name'])
        print (b, "[Region Name]     >"  , data['region_name'])
        print (b, "[City]            >"  , data['city'])
        print (b, "[Country Capital] >"  , data['countryCapital'])
        print (b, "[Country Code]    >"  , data['country_code'])
        print("")
        print (a, "[Time Zone]       >"  , data['time_zone'])
        print (a, "[Calling Code]    >"  , data['callingCode'])
        print (a, "[Currency]        >"  , data['currency'])
        print (a, "[CurrencySymbol]  >", data['currencySymbol'])
        print("")
        print (a, "[Organization]    >"  , data['organisation'])
        print (a, "[Latitude]        >"  , data['latitude'])
        print (b, "[Longitude]       >"  , data['longitude'])
        print (a, "[Zip code]        >"  , data['zip_code'])
        print ("")
        print (a, "[Suspicious IP]   >"  , data['suspiciousFactors'])
        print (" "+lgreen+bold)

except KeyboardInterrupt:
        print ('Terminating, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" check your internet connection!"+clear)
sys.exit(1)
