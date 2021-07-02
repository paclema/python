# Requeriments:
#   - Beautifulsoup --> pip install bs4
#   - Selenium: https://stackoverflow.com/a/18131102 --> pip install selenium
#   - Drivers Firefox: https://selenium-python.readthedocs.io/installation.html#drivers
#       Download the geckodriver in your folder and:
#       export PATH=$PATH:/path/to/directory/of/executable/downloaded/in/previous/step
#   - Drivers Chrome: https://linuxhint.com/chrome_selenium_headless_running/  --> with rpi4: sudo apt-get install chromium-chromedriver
#   - InfluxDB:  pip install influxdb

# START /B python3 boulderhalle_status.py > out2.txt

# import libraries

from bs4 import BeautifulSoup
import ssl
import selenium.webdriver as webdriver
import os
import time
import re

from influxdb import InfluxDBClient
from datetime import datetime

# Using Firefox:
# -------------
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# binary = FirefoxBinary('/usr/bin/firefox-esr')
# driver = webdriver.Firefox(firefox_binary=binary)

# Selenium webdriver object:
# os.environ['MOZ_HEADLESS'] = '1'    # We avoid to open the browser
# driver = webdriver.Firefox()


# Using Chrome:
# -------------
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.headless = True   # We avoid to open the browser
chromeOptions.add_argument("--no-sandbox")
# chromeOptions.add_argument("--window-size=1280,720")

# Windows:
if os.name == 'nt':
    driver = webdriver.Chrome(executable_path="C:/Users/pacle/Downloads/chromedriver_win32/chromedriver", options=chromeOptions)  # Optional argument, if not specified will search path.
# Linux
elif os.name == 'posix':
    # driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver", options=chromeOptions)  # Optional argument, if not specified will search path.
    driver = webdriver.Chrome(options=chromeOptions)  # Optional argument, if not specified will search path.


# Configurations:
UPDATE_DB_DELAY = 0.5     # Minutes between updates

def check_ampel_status(url):

    # # specify the url
    # url = 'https://boulderhalle-leipzig.de/'
    #  Also reading the html from last page, we can assume that the call is made using the service provided by:
    # url = 'https://147.webclimber.de/de/trafficlight?key=pZ5rnsqNK6ZRBnDkesDha1MF1tcXa88M'

    # Files to print html web processed
    file = open("html.txt","w")

    # Instagram html is processed by javascript so we need to open the url with Firefox to be processed:
    # os.environ['MOZ_HEADLESS'] = '1'    # We avoid to open the browser
    # driver = webdriver.Firefox()
    driver.get(url)

    soup = BeautifulSoup(driver.page_source,'html.parser')

    # file.write(str(soup.body))
    headline_results = soup.find_all('div', attrs={'class':'trafficlight'})
    # print ("headline_results: " + str(headline_results))
    # <div class="trafficlight">
    #     <div class="container">
    #         <div class="circle red"></div>
    #         <div class="circle yellow"></div>
    #         <div class="circle green active"></div>
    # </div></div>

    # Using regular expresion get the active color:
    container = headline_results[0]
    color_actived = container.find('div', {"class": re.compile("active$")})
    if (color_actived != None ):
        # print ("color_actived: " + str(type(color_actived)))
        color = color_actived['class'][1]
        # print ("color: " + str(color)) # class="circle green active" the color is the element id 1
    else:
        color = "off"
    # driver.close()

    return color

def check_number_status(url):

    # # specify the url
    # url = 'http://kosmos-bouldern.de/'
    # <div data-value="36" id="visitorcount-container" class="freepercent1 ">
	# 	<div data-value="36" class="actcounter zoom">
    #         <div class="actcounter-title"><span>Besucher</span></div>
                # <div class="actcounter-content"><span data-value="36">36</span></div></div>
    #     <div data-value="44" class="freecounter zoom">
    #         <div class="freecounter-title"><span>Frei</span></div><div class="freecounter-content"><span data-value="44">44</span></div></div>
	# </div>

    # https://www.boulderado.de/boulderadoweb/gym-clientcounter/index.php?mode=get&token=eyJhbGciOiJIUzI1NiIsICJ0eXAiOiJKV1QifQ.eyJjdXN0b21lciI6Iktvc21vcyJ9.CElSaqJrlW0okupB9PMYfJBGjkNx_sJcYSsythLhKPw

    # Files to print html web processed
    # file = open("html.txt","w")

    # Instagram html is processed by javascript so we need to open the url with Firefox to be processed:
    # os.environ['MOZ_HEADLESS'] = '1'    # We avoid to open the browser
    # driver = webdriver.Firefox()
    driver.get(url)

    soup = BeautifulSoup(driver.page_source,'html.parser')

    # file.write(str(soup.body))

    # headline_results = soup.find_all('div', attrs={'class':'freepercent1'})
    # <div data-value="113" class="actcounter zoom"><div class="actcounter-title"><span>Besucher</span></div><div class="actcounter-content"><span data-value="113">113</span></div></div>
    headline_results = soup.find_all('div', attrs={'class':'actcounter zoom'})


    # print ("headline_results: " + str(headline_results))

    visitors = headline_results[0]['data-value']
    # print ("visitors: " + str(visitors))

    # driver.close()

    return visitors

def update_db(halle, data):
    """Instantiate a connection to the InfluxDB."""
    host='localhost'
    port = 8086
    user = 'user'
    password = 'pass'
    dbname = 'namedb'

    client = InfluxDBClient(host, port, user, password, dbname)
    # client.get_list_database() # [{'name': '_internal'}, {'name': 'homeassistant'}, {'name': 'boulder'}]
    # client.switch_database('boulder')

    if (halle == "BLOC" or halle == "NoLimit"):
        data_name = "status"
        if (data == "green"): data = 0
        elif (data == "yellow"): data = 1
        elif (data == "red"): data = 2
        elif (data == "off"): data = -1
    else:
        data_name = "visitors"

    current_time = current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # json_body = [
    #     {
    #         "measurement": "clients",
    #         "tags": {
    #             "boulderhalle": halle
    #         },
    #         "time": current_time,
    #         "fields": {
    #             data_name: data
    #         }
    #     }
    # ]

    json_body = [
        {
            "measurement": halle,
            "tags": {},
            "time": current_time,
            "fields": {
                data_name: data
            }
        }
    ]

    # print("Write points: {0}".format(json_body))
    client.write_points(json_body)

    query = 'select Float_value from cpu_load_short;'



### Main loop:
while(1):

    print ("=== Klettern & Boulderhalle availability === ")
    # bloc = check_ampel_status('https://boulderhalle-leipzig.de/')
    bloc = check_ampel_status('https://147.webclimber.de/de/trafficlight?key=pZ5rnsqNK6ZRBnDkesDha1MF1tcXa88M')
    print (" BLOC no limit: " + str(bloc))
    try:
      update_db(halle = "BLOC", data = str(bloc))
    except Exception as e:
        print("update_db not successful: " + str(e))

    # noLimit = check_ampel_status('https://kletterhalle-nolimit.de/')
    noLimit = check_ampel_status('https://148.webclimber.de/de/trafficlight?key=T09KUqx3WXP1yF5AMCmYbHX6pG9DaGF2')
    print (" No limit: " + str(noLimit))
    try:
      update_db(halle = "NoLimit", data = str(noLimit))
    except Exception as e:
        print("update_db not successful: " + str(e))


    # kosmos = check_number_status('http://kosmos-bouldern.de/')  # Better take the iframe url embeded from boulderado
    kosmos = check_number_status('https://www.boulderado.de/boulderadoweb/gym-clientcounter/index.php?mode=get&token=eyJhbGciOiJIUzI1NiIsICJ0eXAiOiJKV1QifQ.eyJjdXN0b21lciI6Iktvc21vcyJ9.CElSaqJrlW0okupB9PMYfJBGjkNx_sJcYSsythLhKPw')
    print (" Kosmos: " + str(kosmos))
    try:
        update_db(halle = "kosmos", data = int(kosmos))
    except Exception as e:
        print("update_db not successful: " + str(e))

    # Timestamp:
    dateTimeObj = datetime.now()
    print('Last update: ', dateTimeObj.hour, ':', dateTimeObj.minute, ':', dateTimeObj.second)

    # break
    time.sleep(60*UPDATE_DB_DELAY)


driver.quit()
