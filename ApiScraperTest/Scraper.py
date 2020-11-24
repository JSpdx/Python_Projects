import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
   
    
    
    def scrape():
        url = "https://blog.naxos.com/"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        # result = soup.find_all(class_="slick-slide")
        result = soup.find_all('p')

        for i in result:
             print(i.text + "\n")
        return

    def test_scrape():
        testUrl = "https://www.sciencemag.org/news/latest-news" #  Test url confirmed to work
        page = requests.get(testUrl)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find_all('a') #  Test result to be used with test url

       # change to testResult to run test.
        for i in result:
             print(i.text + "\n")
        return

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    #  scrape()
    # test_scrape()
    x = print('stuff')
    x
     