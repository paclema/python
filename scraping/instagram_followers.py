# Requeriments:
#   - Beautifulsoup
#   - Selenium: https://stackoverflow.com/a/18131102


# import libraries

from bs4 import BeautifulSoup
import ssl
import selenium.webdriver as webdriver
import os
import time

def check_instagram_followers(url):

    # # specify the url
    # url = 'http://www.instagram.com/wundercurves.de/'

    # Files to print html web processed
    file = open("html.txt","w")

    # Instagram html is processed by javascript so we need to open the url with Firefox to be processed:
    os.environ['MOZ_HEADLESS'] = '1'    # We avoid to open the browser
    driver = webdriver.Firefox()
    driver.get(url)

    soup = BeautifulSoup(driver.page_source,'html.parser')

    # file.write(str(soup.body))

    headline_numbers = soup.find_all('span', attrs={'class':'g47SY'})
    # print "headline_numbers: " + str(headline_numbers)
    # followers = headline_numbers[1].find("span",{'class':'g47SY lOXF2'})["title"]
    followers = headline_numbers[1]["title"]

    #print followers
    return followers

    driver.quit()
    # driver.close()

while(1):

    wundercurves = check_instagram_followers('http://www.instagram.com/wundercurves.de/')
    paclema = check_instagram_followers('http://www.instagram.com/paclema/')
    print "=== Instagram Followers === "
    print " @paclema: " + str(paclema)
    print " @wundercurves: " + str(wundercurves) + "\n"
    # break
    time.sleep(10)
