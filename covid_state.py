from selenium import webdriver
import os

def covid_state(state='Gujarat'):
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver  = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
    driver.get('https://prsindia.org/covid-19/cases')
    driver.maximize_window()
    headings = []
    processing = True
    i = 2
    while processing:
        try:
            ele = driver.find_element_by_xpath('//table/thead/tr/th[{}]'.format(i)).text
            headings.append(ele)
            i += 1
        except:
            processing = False

#print(headings)

    states_data = []
    processing = True
    j = 1
    while processing:
        try:
            state_wise_data = []
            for i in range(2,7):
                ele = driver.find_element_by_xpath('//table/tbody/tr[{}]/td[{}]'.format(j,i)).text

                state_wise_data.append(ele)

            states_data.append(state_wise_data)

            j += 1

        except:
            processing = False
    st = ''
    for i in range(len(states_data)):
        if state.lower() == states_data[i][0].lower():
            st =    '''{} -->  {}
            {} --> {}
            {} --> {}
            {} --> {}
            {} --> {}'''.format(headings[0],states_data[i][0],headings[1],states_data[i][1],headings[2],states_data[i][2],headings[3],states_data[i][3],headings[4],states_data[i][4])
            
            return st

    return 'Please recheck the state name,I was not able to find this state.'

#print(covid_state('Gujarat'))
