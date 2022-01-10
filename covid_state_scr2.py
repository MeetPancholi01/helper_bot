from selenium import webdriver
import re
import os
def covid_state(state='Gujarat'):
    state = state.lower()
    state = state + ' '

    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-sh-usage')

    driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)

    driver.get('https://covid19tracker.in/')

    driver.implicitly_wait(20)

#driver.maximize_window()
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
            
            #st = ' '.join(country_filt)
            #print(st)
            country_filt2 = []
            pr = True
            cnt = 1
            kl = 0
            while kl <= len(country_filt)-1:
                st = ''
                if cnt == 1:
                    while pr:
                        st += country_filt[kl] + ' '
                        kl += 1
                        if not country_filt[kl].startswith('↑'):
                            try:
                                jj = int(country_filt[kl][1])
                                break
                            except:
                                continue
                        else:
                            cnt += 1
                            break
                    country_filt2.append(st)

                country_filt2.append(country_filt[kl])
                kl += 1

            #print(country_filt2)
                
            i = 0
            country_final = []
            while i <= len(country_filt2)-1:
                if country_filt2[i].startswith('↑'):
                    country_final.append(country_filt2[i]+' ' + country_filt2[i+1])
                    i += 2
        
                else:
                    country_final.append(country_filt2[i])
                    i += 1

            #print(country_final)
            final.append(country_final)
            j += 1
            #print(final)

        except:
            processing = False
    #print(final[0][0])
    for i in range(len(final)-1):
        if final[i][0].lower() == state:
            return final[i],he
    return 'Oops, Looks like some error occured !'
#print(headings)
#print(country_stats)
#print(covid_state('Gujarat'))
