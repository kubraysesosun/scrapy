from scrapy import Request, Spider
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Salvin(Spider):   
    name = "salvin"
    start_urls = ["www.salvin.com"]
    def __init__(self):
        # self.url="www.salvin.com"
        self.open_driver()
        
    # def start_request(self):
    #     url = "www.salvin.com"
    #     yield Request(url, self.parse)
    
    def open_driver(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver.get(self.url)
        sleep(5)
    