import selenium
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime

url = 'https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148'
pth = r'D:\Users\lusty\Strive\GitHub\Strive_AI_22\09. Web-scraping\chromedriver.exe'
brave_path = 'C:\Program Files\BraveSoftware\Brave-Browser\Application'

option = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path=pth, options=option)
driver.get(url)

box = driver.find_element_by_xpath('//*[@id="detailed-forecast-body"]')
day_name = box.find_elements_by_xpath('//*[@class="col-sm-2 forecast-label"]')

days = []
for i in range(0, 10, 2):
    days.append(day_name[i].text)
row = ['Date', 'Conditions', 'High', 'Low']

forecast = pd.DataFrame(columns=days, index=row)

today_date = driver.find_element_by_xpath('//*[@id="about_forecast"]/div[2]/div[2]')
today_date = today_date.text
# for i in range(0, 10, 2):
forecast.iloc[0, 0] = today_date

print(forecast)
