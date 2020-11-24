import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver


if __name__ == "__main__":

    def site_login():
        url = "https://www.learncodinganywhere.com/LMS#/drillReportResultsInstructor/Jason%20Saar,be6bc60b-c58f-4c42-a862-9f207128f6f0,Portland%20Campus"
        driver = webdriver.Chrome('C:\dev\chromedriver.exe')
        driver.get("https://www.learncodinganywhere.com/Account/Login")
        username = "liveproject@gmail.com"
        password = "findadam2019"
        driver.find_element_by_id('Email').send_keys(username)
        driver.find_element_by_id ('Password').send_keys(password)
        time.sleep(3)
        driver.find_element_by_class_name("btn").click()
        time.sleep(3)
        driver.get(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        # result = soup.find_all(class_="panel-danger")
        result = soup.find_all("a")
        for i in result:
            print(i.text + "\n")
        driver.quit()

    
     def scrape():
         page = requests.get(url)
         soup = BeautifulSoup(page.content, 'html.parser')
         # result = soup.find_all(class_="panel-danger")
         result = soup.find_all("a")
         for i in result:
             print(i.text + "\n")
            
         result = soup.find_all('')
         return print(result)


    site_login()
    # scrape()


# TESTED
# https://www.usatoday.com/money/investing


    # https://www.allrecipes.com/recipes/1642/everyday-cooking