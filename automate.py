
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
import os

def execute(mssg = 'Python'):
    #chr_options = Options()
    #chr_options.add_experimental_option("detach", True)
    #GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google_chrome'
    #CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    #options.add_argument('--ignore-certificate-errors-spki-list')
    #options.add_argument('--ignore-ssl-errors')

    driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)

    driver.get('https://youtube.com')

    #driver.maximize_window()

    searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')

    searchbox.send_keys('{} tutorial'.format(mssg))
    searchbox.send_keys(Keys.RETURN)
    #searchButton = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button')

    #searchButton.click()
    driver.implicitly_wait(10)

    #ele = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a')

    return

def execute_search(mssg):
    #GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google_chrome'
    #CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    #options.add_argument('--ignore-certificate-errors-spki-list')
    #options.add_argument('--ignore-ssl-errors')

    driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)


    driver.get('https://google.com')

    driver.maximize_window()

    searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')

    searchbox.send_keys('{}'.format(mssg))
    searchbox.send_keys(Keys.RETURN)

# def news():
#     driver = webdriver.Chrome()

#     driver.get('https://google.com')

#     driver.maximize_window()

#     searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')

#     searchbox.send_keys('{}'.format('Latest News'))
#     searchbox.send_keys(Keys.RETURN)

#     ds = driver.find_element_by_xpath('/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a')

#     ds.click()
#     return 'https://www.google.com/search?q=Latest+News&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjDlKb54J_1AhXIxYsBHTguAO8Q_AUoAXoECAEQAw&biw=1536&bih=708&dpr=1.25'

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

    

def play_music(name = None):
    
        #GOOGLE_CHROME_BIN = '/app/.apt/usr/bin/google_chrome'
        #CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    if name == None:
        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        #options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        #options.add_argument('--ignore-certificate-errors-spki-list')
        #options.add_argument('--ignore-ssl-errors')

        driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
        #driver = webdriver.Chrome()

        driver.get('https://google.com')

        driver.maximize_window()

        searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')
        searchbox.send_keys('youtube music')
        searchbox.send_keys(Keys.RETURN)

        df = driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div[1]/a')
        df.click()

        return
    
    else:
        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        #options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        #options.add_argument('--ignore-certificate-errors-spki-list')
        #options.add_argument('--ignore-ssl-errors')
        #driver = webdriver.Chrome()
        driver = webdriver.Chrome(executable_path= os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)

        driver.get('https://google.com')

        driver.maximize_window()

        searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input')
        searchbox.send_keys('youtube music')
        searchbox.send_keys(Keys.RETURN)


        df = driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div[1]/a')
        df.click()

        driver.implicitly_wait(10)

        ds = driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/span')
        ds.click()

        df = driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input')
        df.send_keys(name)
        df.send_keys(Keys.RETURN)
        try:
            dd = driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-search-page/ytmusic-tabbed-search-results-renderer/div[2]/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div[2]/ytmusic-responsive-list-item-renderer/div[2]/div[1]/yt-formatted-string/a')
            dd.click()

        except:
            dd = driver.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-search-page/ytmusic-tabbed-search-results-renderer/div[2]/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[2]/div[2]/ytmusic-responsive-list-item-renderer[1]/div[2]/div[1]/yt-formatted-string/a')
            dd.click()
        
        #dl = driver.find_element_by_xpath('/html/body/div[1]/div[2]/header/aside/div[2]/div/div[1]/article/div[1]/figure/figcaption/h4/a')

        #dl.click()

        #driver.implicitly_wait(30)

        # ds.send_keys(Keys.RETURN)
        # ds.send_keys(name)
        # ds.send_keys(Keys.RETURN)





    
