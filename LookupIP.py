import requests
import re
import time

# you can set own ipgeolocation.io API key here
_API_KEY = 'fd3e249173714f2ca84690d65bc07405'
_PREFIX = '{~}'
_LOGO = '''
 .                   \                       _ .___ 
 /       __.    __.  |   , ,   . \,___,      | /   \\
 |     .'   \ .'   \ |  /  |   | |    \      | |,_-'
 |     |    | |    | |-<   |   | |    |      | |    
 /---/  `._.'  `._.' /  \_ `._/| |`---'      / /    
                                 \                  
'''

def lookup(_ip):
    try:
        if _ip == '':
            response = requests.get("https://api.ipgeolocation.io/ipgeo?apiKey={0}".format(_API_KEY))
        else:
            response = requests.get("https://api.ipgeolocation.io/ipgeo?apiKey={0}&ip={1}".format(_API_KEY, _ip))
       
        json = response.json()

        print('\n{~} Parsing response ...', end='')

        if response.status_code == 200:
            return ('\n\n{0} Information:\n IP:                 {1}\n City:               {2}\n District:           {3}\n State:              {4}\n Postal code:        {5}\n Country:            {6}\n Continent:          {7}\n Languages:          {8}\n ISP:                {9}\n Organization:       {10}\n Latitude:           {11}\n Longitude:          {12}\n {13} Time:\n  Current time:      {14}\n  Time offset:       {15}\n  Name:              {16}\n {17} Currency:\n  Name:              {18}\n  Code:              {19}\n  Symbol:            {20}'.format(
                _PREFIX, json['ip'], json['city'], json['district'], json['state_prov'], json['zipcode'], json['country_name'], json['continent_name'], json['languages'], json['isp'], json['organization'], json['latitude'], json['longitude'], _PREFIX, json['time_zone']['current_time'], json['time_zone']['offset'], json['time_zone']['name'], _PREFIX, json['currency']['name'], json['currency']['code'], json['currency']['symbol']))
        elif response.status_code == 401:
            return ('\n\n{0} Unknown error:\n Status: {1}\n Data: {2}'.format(_PREFIX, response.status_code, json))
        elif response.status_code == 403:
            return ('\n\n{0} Invalid IP address:\n Status: {1}\n Data: {2}'.format(_PREFIX, response.status_code, json))
        elif response.status_code == 404:
            return ('\n\n{0} IP address not found:\n Status: {1}\n Data: {2}'.format(_PREFIX, response.status_code, json))
        elif response.status_code == 423:
            return ('\n\n{0} IP address not yet officially assigned:\n Status: {1}\n Data: {2}'.format(_PREFIX, response.status_code, json))
        else:
            return ('\n\n{0} API usage limit has reached:\n Status: {1}\n Data: {2}'.format(_PREFIX, response.status_code, json))
    except Exception as ex:
        print('\n\n{~} Unknown error at lookup: '+str(ex))

if __name__ == '__main__':
    try:
        print(_LOGO)
        usrIP = input('{~} Enter IP address, leave empty if you want to use your IP address:\n > ')

        usrIP = usrIP if re.search('[a-zA-Z0-9]', usrIP) else ''

        print('\n{~} Sending request ...', end='')
        starttime = time.time()
        print(lookup(usrIP))
        print('\n{0} Elapsed time: {1}'.format(_PREFIX, str(time.time() - starttime)))
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt')
        quit()
