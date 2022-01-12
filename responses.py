import re
import datetime as dt
import automate
import wikipedia
import time
import random
import math
import pyjokes
import pytz
import webbrowser as wb
import covid_scr
import covid_state_scr2
import covid_state
from iso3166 import countries
#print(selenium.__version__())we
arr = ['music.youtube','open.spotify','jiosaavn']
states = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli and Daman and Diu","Lakshadweep","Delhi","Puducherry"]
# from selenium.webdriver.common.keys import Keys
IST = pytz.timezone('Asia/Kolkata')
d = dt.date.today()
curr_time = time.localtime()
curr_clock = time.strftime("%H:%M:%S", curr_time)
t = dt.datetime.now(IST)
day = dt.datetime.today().weekday()
arr = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def bool_country(message):
    for i in message:
        if i in countries:
            return i
        
    query = message[1:]
    query = ' '.join(query)
    if query in countries:
        return query
      
    return None

def bool_state(message):
    if len(message) > 2 and len(message) <= 10:
        query = message[2:]
        query = ' '.join(query) 
        for i in range(len(states)):
            if query.lower() == states[i].lower():
                return states[i]
        return None
    else:
        return None


def process_mssg(message):
    pattern = re.findall(r"[\w*]+|[.,!?;]",message.lower())
    return pattern

def get_response(message):
    #GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google_chrome'
    #CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    mssg = process_mssg(message)
    if 'hello' in mssg or 'hii' in mssg or 'Hii' in mssg:
        return 'Hii, nice to talk to you sir !'

    if ('I' in mssg and 'am' in mssg) or ('i' in mssg and 'am' in mssg):
        name = ' '.join(mssg[2:])
        return f'Hello {name}'

    if ('who' in mssg and 'you' in mssg) or ('what' in mssg and 'your' in mssg and 'name' in mssg):
        return 'I am shadow, a python bot.'

    if 'date' in mssg:
        return f"\nToday's date is {d}"

    elif 'day' in mssg:
        return f"\nToday's day is {arr[day]}"

    elif 'time' in mssg:
        return f"\nCurrent time in IST: {t}"

    elif 'learn' in mssg:
        index = mssg.index('learn')
        query = ' '.join(mssg[index+1:])
        automate.execute('{}'.format(query))
        q = ''
        for i in query:
            if i != ' ':
                q += i
            else:
                q += '+'
        return 'https://www.youtube.com/results?search_query={}+tutorial'.format(q)

    elif 'wikipedia' in mssg or 'information' in mssg:
        if 'wikipedia' not in mssg:
            query = ' '.join(mssg)
            ind = query.index('information')
            query = query[:ind-1]
            #print(query)
            try:
                res = wikipedia.summary(query,sentences=10)
                return res
            except:
                #automate.execute_search(query)
                q = ''
                for i in query:
                    if i != ' ':
                        q += i
                    else:
                        q += '%20'
                return 'https://en.wikipedia.org/wiki/{}'.format(q)


        else:
            query = ' '.join(mssg)
            #print(query)
            #query = query.replace('wikipedia','informaton')
            ind = query.index('wikipedia')
            query = query[:ind-1]
            #print(query)
            #print(query)
            try:
               res = wikipedia.summary(query,sentences=10)
               return res
            except:
               #automate.execute_search(query)
               q = ''
               for i in query:
                    if i != ' ':
                       q += i
                    else:
                        q += '%20'
               return 'https://en.wikipedia.org/wiki/{}'.format(q)

    elif 'news' in mssg:
        query = ' '.join(mssg)
        res = automate.news_mod(query)
        return res

    elif 'music' in mssg:
        num = math.floor((random.random())*3)
        if num == 1:
            return 'https://music.youtube.com'

        elif num == 2:
            return 'https://open.spotify.com'

        else:
            return 'https://www.jiosaavn.com'

    elif 'play' in mssg and 'music' not in mssg:
        num = math.floor((random.random())*3)
        query = ' '.join(mssg[1:])
        #automate.play_music(query)
        if num == 0:
            q = ''
            for i in query:
                if i != ' ':
                    q += i
                else:
                    q += '+'
            return 'https://music.youtube.com/search?q={}'.format(q)
        else:
            q = ''
            for i in query:
                if i != ' ':
                    q += i
                else:
                    q += '%20'
            if num == 1:
                return 'https://open.spotify.com/search/{}'.format(q)
            else:
                return 'https://www.jiosaavn.com/search/{}'.format(q)
        #automate.play_music(query)
        #return
    elif 'joke' in mssg or 'jokes' in mssg:
        text = pyjokes.get_joke()
        return text

    elif 'open' in mssg and mssg[0] == 'open':
        try:
            #chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            mssg = mssg[1:]
            query = ''.join(mssg)
            wb.get("GOOGLE_CHROME_BIN").open(query)
            #wb.open(query)
            return
        except:
            return 'Some error occured while using chrome browser!'

    elif 'covid-19' in mssg or 'covid' in mssg or 'corona' in mssg or 'Covid' in mssg:
        k1 = bool_country(mssg)
        k2 = bool_state(mssg)
        if k1 != None and k2 == None:
            res1,res2 = covid_scr.covid_data_country(k1)
            return '''{} 
            {} 
            {} 
            {}
            {}'''.format(res1[0],res1[1],res1[2],res2[0],res2[1])

        elif k1 != None and k2 != None:
            try:
                res1,res2 = covid_state_scr2.covid_state(k2)
                if res1[0].strip() in states:
                    return ''' State {}
                    Confirmed Cases {}
                    Active {}
                    Recovered {}
                    Deceased {}
                    Tested {}
                    Vaccine Doses Administered {}'''.format(res1[0],res1[1],res1[2],res1[3],res1[4],res1[5],res1[6])
                else:
                    res = covid_state.covid_state(k2)
                    return res
            except:
                res = covid_state.covid_state(k2)
                return res

        else:
            return '''Please recheck the country/state name or try some other name of the same country
            Note -: To obtain the covid information you can ask me in one of the following ways
            1) covid <country name>
            2) covid india <state name>
            '''

    else:
        return 'Sorry I am not yet trained to understand things you wrote !'
        
#https://music.youtube.com/search?q=unstoppable
#https://open.spotify.com/search/unstoppable
#https://www.jiosaavn.com/search/unstoppable
#https://en.wikipedia.org/wiki/Book_of_Revelation 

#print(countries.get('United States'))
    
#print(get_response('open youtube.com'))
