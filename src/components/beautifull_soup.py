from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import pandas as pd
import traceback # for detailed error logging
import time # for sleep
import random # for random sleep intervals
from bs4 import BeautifulSoup
import requests_oauthlib # for OAuth1 session
import os # for environment variables   
import json # for parsing JSON responses
from requests.exceptions import RequestException # for handling request exceptions
from requests_oauthlib import OAuth1Session # for OAuth1 session
import requests # for making HTTP requests
class EmailScraper:
    def __init__(self):
        pass    
    
    def beautiful_soup_get_emails_using_api(self,domain):
        try:
            # Load API credentials from environment variables
            api_key = os.getenv('HUNTER_API_KEY')
            api_secret = os.getenv('HUNTER_API_SECRET')
            if not api_key or not api_secret:
                raise ValueError("API credentials are not set in environment variables.")
            else:
                print("api loaded succesfullly")
        except Exception as e:
            print(f"Error loading API credentials: {e}")
            
    def beautiful_soup_get_emails_using_url(self,url):
        
        response=requests.get(url)
        if response.status_code==403:
            print("Access forbidden: 403")
            print("redirecting to  headers method")
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            response=requests.get(url, headers=headers)
            
            print(response.text)
            soup=BeautifulSoup(response.text, 'html.parser')
            print(soup.prettify())
            return soup
        else:
            print(response.text)
            soup=BeautifulSoup(response.text, 'html.parser')
            print(soup.prettify())
        

            return soup
        
class allparser(EmailScraper):
    def __init__(self):
        super().__init__()
        
    def find_data_email(self,soup):
        quotes = soup.find_all(string=lambda text: "@" in text)
        emails = [quote.strip() for quote in quotes if "@" in quote] 
        return emails  
        
    def find_data_phone(self,soup):
        quotes = soup.find_all(string=lambda text: "+" in text)
        phones = [quote.strip() for quote in quotes if "+" in quote]
        return phones
    def miscellenous(self,soup):
        quotes = []
        quote_boxes = soup.find_all('div', class_='col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top')
        for box in quote_boxes:
            quote_text = box.img['alt'].split(" #")
            quote = {
                'theme': box.h5.text.strip(),
                'image_url': box.img['src'],
                'lines': quote_text[0],
                'author': quote_text[1] if len(quote_text) > 1 else 'Unknown'
            }
            quotes.append(quote)
        # Display extracted quotes
        for q in quotes[:5]:  # print only first 5 for brevity
            print(q)
        return quotes

if __name__ == "__main__":
    parser=EmailScraper()
    
    url_i="".join((input("ArithmeticError: Enter the URL of the website to scrape emails from: ")))
    print(f"URL entered: {url_i}")
    traceback.print_stack()
    try:
        
        
        soup=parser.beautiful_soup_get_emails_using_url(url_i)
        import csv
        allparser=allparser()
        qoutes=allparser.miscellenous(soup)
        fptr=os.path.join(os.getcwd(),"scrapping_result_1.csv")
        with open(fptr,mode='w')as f:
        
            writer=csv.DictWriter(f,fieldnames=['theme', 'image_url', 'lines', 'author'])
            writer.writeheader()
            for quote in qoutes:
                writer.writerow(quote)
        
    except RequestException as e:
        print(f"Request failed: {e}")  
        print(f"URL entered: {url_i}")
        print(f"file_path: {fptr} already exists")       
