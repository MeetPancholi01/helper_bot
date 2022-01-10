from bs4 import BeautifulSoup
import requests
import datetime

def process_date(date):
    date = str(date)
    #pattern = re.findall(r'[0-9]+',date)
    # li = []
    # for i in range(len(pattern)):
    #     li.append(int(pattern[i]))
    # print(pattern)
    #print(li)
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    today = str(today)
    yesterday = str(yesterday)
    return today,yesterday
    

def covid_data_country(query='india'):
    date = datetime.date.today()
    #print(date)
    #print(str(date))
    url = 'https://www.worldometers.info/coronavirus/country/{}/'.format(query)

    def getHTML_doc(url):
        try:
            res = requests.get(url)
            return res.text
        except:
            return 'URL not working'


    doc = getHTML_doc(url)

    tod,yest = process_date(date)

    if doc == 'URL not working':
        return 'Some error occured,check your internet or recheck the spelling of the country you have given.'

    soup = BeautifulSoup(doc,'lxml')
    covid_tod_stats = []
    covid_tod_addr = []
    res = soup.find_all('div',id="maincounter-wrap")
    #print(res[0].span.text)
    #print(res[1].span.text)
    #print(res[2].span.text)
    for i in range(3):
        covid_tod_stats.append(res[i].span.text)
    for i in range(3):
        covid_tod_addr.append(res[i].h1.text)

    covid_fin_data_today = []
    for i in range(len(covid_tod_addr)):
        covid_fin_data_today.append('Total ' + covid_tod_addr[i] + ' ' + covid_tod_stats[i])

    #print(covid_fin_data_today)
    #print(res[0].span.text)
    #print(covid_tod_stats)
    #print(covid_tod_addr)


    try:
        res2 = soup.find_all('div',id="newsdate"+yest)
        covid_yest = []

        res3 = res2[0].div.div.ul.li.find_all('strong')[0:2]
        res31 = res3[0].text
        res32 = res3[1].text
        covid_yest.append(res31)
        covid_yest.append(res32)
    except:
        y = datetime.date.today()
        y_1 = y - datetime.timedelta(days=2)
        y_1 = str(y_1)
        res2 = soup.find_all('div',id="newsdate"+y_1)
        covid_yest = []

        res3 = res2[0].div.div.ul.li.find_all('strong')[0:2]
        res31 = res3[0].text
        res32 = res3[1].text
        covid_yest.append(res31)
        covid_yest.append(res32)

    #print(covid_yest)

    return covid_fin_data_today,covid_yest

#print(covid_data_country('india'))

