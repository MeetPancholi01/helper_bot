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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
import os
#print(selenium.__version__())we
arr = ['music.youtube','open.spotify','jiosaavn']
country_names = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "South Korea", 'North Korea', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russia', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Vietnam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
states = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli and Daman and Diu","Lakshadweep","Delhi","Puducherry"]
# from selenium.webdriver.common.keys import Keys
#IST = pytz.timezone('Asia/Kolkata')
curr_time = time.localtime()
curr_clock = time.strftime("%H:%M:%S", curr_time)
#day = dt.datetime.today().weekday()
#arr = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def news_mod2(query):
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    #options.add_argument('--ignore-certificate-errors-spki-list')
    #options.add_argument('--ignore-ssl-errors')

    driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
    try:
        query = query.replace(' ','%20')
        driver.get('https://news.google.com/search?q={}&hl=en-IN&gl=IN&ceid=IN%3Aen'.format(query))
        ele = driver.find_element_by_xpath("//a[@class='NAv2Bc']").get_attribute('href')
        return ele
    
    except:
        return 'https://news.google.com/search?q={}&hl=en-IN&gl=IN&ceid=IN%3Aen'.format(query)
    return None
    
def news_mod(query):
    #GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google_chrome'
    #CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    #options.add_argument('--ignore-certificate-errors-spki-list')
    #options.add_argument('--ignore-ssl-errors')

    driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
    driver.get('https://google.com')

    #driver.maximize_window()

    searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')

    searchbox.send_keys('{}'.format(query))
    searchbox.send_keys(Keys.RETURN)
    processing = True
    i = 2
    while processing:
        try:
            ds = driver.find_element_by_xpath('//div[4]/div/div[1]/div/div[1]/div/div[{}]/a'.format(i)).text
            if ds == 'News':
                target = driver.find_element_by_xpath('//div[4]/div/div[1]/div/div[1]/div/div[{}]/a'.format(i)).get_attribute('href')
                return target
        except:
            return 'https://www.google.com/search?q=Latest+News&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjDlKb54J_1AhXIxYsBHTguAO8Q_AUoAXoECAEQAw&biw=1536&bih=708&dpr=1.25'
        
        i += 1
def get_date():
    d = dt.date.today()
    return d

def get_time():
    IST = pytz.timezone('Asia/Kolkata')
    t = dt.datetime.now(IST)
    return t

def get_day():
    arr = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day = dt.datetime.today().weekday()
    return arr[day]
    
    

def bool_country(message):
    global country_names
    #for i in message:
    #    if i in countries or i in country_names:
    #        return i
    if 'india' not in message and 'India' not in message and 'INDIA' not in message:
        query = message[1:]
        query = ' '.join(query)
        if query in countries or query in country_names:
            return query
    
        for i in range(len(country_names)):
            if query.lower() == country_names[i].lower():
                return query
            
    else:
        return 'india'
        
        
    
#     for i in message:
#         for j in country_names:
#             if i.lower() == j.lower():
#                 return i   
    return None

def bool_state(message):
    global states
    process = None
    if len(message) > 2 and len(message) <= 10:
        query = message[2:]
        query = ' '.join(query) 
        for i in range(len(states)):
            if query.lower() == states[i].lower():
                process = states[i]
                return process
            else:
                continue
        return process
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
        d = get_date()
        return f"\nToday's date is {d}"

    elif 'day' in mssg:
        var = get_day()
        return f"\nToday's day is {var}"

    elif 'time' in mssg:
        t = get_time()
        return f"\nCurrent time in IST: {t}"

    elif 'learn' in mssg:
        index = mssg.index('learn')
        query = ' '.join(mssg[index+1:])
        #automate.execute('{}'.format(query))
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
        #query = ' '.join(mssg)
#       res = automate.news_mod(query)
        try:
            k = mssg[:len(mssg)-1]
            query = ' '.join(k)
            res = news_mod2(query)
            return res
        except:
            query = ' '.join(mssg)
            res = news_mod(query)
            return res
            
#         except:
#             res = news_mod(query)
#             return res

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
            if res2 == -1:
                return 'Check your internet or there might be some error in country spelling you have given'
            return '''{} 
            {} 
            {} 
            {}
            {}'''.format(res1[0],res1[1],res1[2],res2[0],res2[1])

        elif k1 != None and k2 != None:
            try:
                res1 = covid_state_scr2.covid_state(k2)
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
