from selenium import webdriver
import json
import os
import requests
import sys

def scrape_google(searchterm):

    if(len(searchterm) > 0):
        url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
        browser = webdriver.Chrome('chromedriver')
        browser.get(url)
        counter = 0

        abs_path = os.path.dirname(os.path.abspath(__file__)) + "/static/scraped-data/"

        if not os.path.exists(abs_path + searchterm):
            os.mkdir(abs_path + searchterm + "/")

        for _ in range(1000):
            browser.execute_script("window.scrollBy(0,10000)")

        image_links = []
        image_types = []

        for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
            counter = counter + 1
            try:
                print("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])
                image_links.append(json.loads(x.get_attribute('innerHTML'))["ou"])
                image_types.append(json.loads(x.get_attribute('innerHTML'))['ity'])
            except:
                    continue

        browser.close()

        for i in range(0, len(image_links)):
            try:
                r = requests.get(image_links[i], timeout=5)
                extension = "jpg" if image_types[i] == "" else image_types[i]
                with open(abs_path + searchterm + "/" + searchterm + "_" + str(i) + "." + extension, 'wb') as outfile:
                    outfile.write(r.content)
                print(i+1, "/", len(image_links), "done!")
            except:
                continue

    else:
        print("Enter search prompt!")
