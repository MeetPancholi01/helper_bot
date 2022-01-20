from selenium import webdriver
import re
import os
def covid_state(state='Gujarat'):
    state = state.lower()
    state = state + ' '
    #GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google_chrome'
    #CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    #options.add_argument('--ignore-certificate-errors-spki-list')
    #options.add_argument('--ignore-ssl-errors')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)

    driver.get('https://covid19tracker.in/')

    driver.implicitly_wait(20)

    driver.maximize_window()
    try:
        #Headings = driver.find_element_by_xpath('html/body/div/div/div[3]/div/div[3]/div[2]/div[1]/div[1]').text
        Headings = driver.find_element_by_xpath('html/body/div/div/div[3]/div/div[3]/div[2]/div[1]/div[1]').text
        #Headings = driver.find_element_by_xpath('//div[3]/div[1]/div[3]/div[2]/div/div[1]/div[1]').text
        #print('try executed')
    except:
        return 'Some error occured'
    headings = re.findall(r'\w+/?\w*',Headings)    # list of headings
    #print(headings)
    he = []
    for i in range(len(headings)):
        if i != len(headings)-3:
            he.append(headings[i])
        else:
            he.append('Vaccine Doses Administered')
            break
    #print(he)
    #print(country_stats)
    final = []
    j = 2
    processing = True
    while processing:
        try:
            country_stats = driver.find_element_by_xpath('html/body/div/div/div[3]/div/div[3]/div[2]/div[1]/div[{}]'.format(j)).text
            country_filt = re.findall(r'\S+',country_stats)
            #print(country_filt)
            #st = ' '.join(country_filt)
            #print(st)
            kk = 0
            while kk <= len(country_filt)-2:
                temp = country_filt[0].lower()
                comp = state[:3]
                if temp.startswith(comp):
                    targeted = country_filt
                    if ' ' in state:
                        k = state.count(" ")
                        st = ''
                        
                        for i in range(k+1):
                            st += f'{targeted[i]} '    
                        
                        for i in range(k+1):
                            targeted.pop(0)
                            
                        st = st.strip()
                        targeted.insert(0,st)
                        

                    return process(targeted)
                kk += 1
            
            j += 1
        except:
            processing = False
           
       
    

def process(targeted):
    i = 0
    country_final = []
    while i <= len(targeted)-1:
        if targeted[i].startswith('↑'):
            country_final.append(targeted[i]+' ' + targeted[i+1])
            i += 2
        
        else:
            country_final.append(targeted[i])
            i += 1

    return country_final
#print(headings)
#print(country_stats)
#print(covid_state('Gujarat'))
