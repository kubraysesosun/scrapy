from scrapy import Request, Spider
from selenium import webdriver
from time import sleep

class Salvin(Spider):   
    name = "salvin"
    
    def __init__(self):
        self.url="www.salvin.com"
        self.open_driver()
        
    # def start_request(self):
    #     url = "www.salvin.com"
    #     yield Request(url, self.parse)
    
    def open_driver(self):
        driver = webdriver.Firefox()
        driver.get(self.url)
        sleep(3)
    