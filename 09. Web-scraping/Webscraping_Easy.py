import selenium
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import datetime

# Set up driver, and get the target URL to load in browser

url = 'https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148'
pth = r'D:\Users\lusty\Strive\GitHub\Strive_AI_22\09. Web-scraping\chromedriver.exe'
brave_path = 'C:\Program Files\BraveSoftware\Brave-Browser\Application'

option = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path=pth, options=option)
driver.get(url)

# Set up a box, and find the days to be checked, and add them as columns to the dataframe.

box = driver.find_element_by_xpath('//*[@id="detailed-forecast-body"]')
day_name = box.find_elements_by_xpath('//*[@class="col-sm-2 forecast-label"]')

days = []
for i in range(0, 10, 2):
    days.append(day_name[i].text)
row = ['Date', 'Conditions', 'High', 'Low']

forecast = pd.DataFrame(columns=days, index=row)

# Scrape today's date, convert it into the right format.

today_date = driver.find_element_by_xpath('//*[@id="about_forecast"]/div[2]/div[2]')
today_date = today_date.text
today_date = today_date.split()
y = int(today_date[-1])
m = today_date[-3]
d = int(today_date[-2].replace(',', ''))

print(today_date)
for i in range(0, 5, 1):
    forecast.iloc[0, i] = f'{d + i}/{m}/{y}'
    # TODO: this gives false value when in the last few days of a month. Fix for more generalized solution.

# Scrape the condition descriptions

conditions = []
cond = box.find_elements_by_xpath('//*[@class="col-sm-10 forecast-text"]')
for i in range(0, 10, 2):
    conditions.append(cond[i].text)

forecast.iloc[1, :] = conditions

# Scrape the High fahrenheit values, convert them to Celsius and add them to the dataframe.

highs = []
high = driver.find_elements_by_xpath('//*[@class="temp temp-high"]')

for i in range(len(high)):
    highs.append(high[i].text)
h = []

for i in highs:
    n = ''
    for k in i:
        if k.isdigit():
            n += k
    h.append(round((int(n) - 32) * 5 / 9, ndigits=0))
highs = h
if len(highs) < len(day_name):
    highs.append(np.nan)
forecast.iloc[2, :] = highs

# Same with lows.

lows = []
low = driver.find_elements_by_xpath('//*[@class="temp temp-low"]')

for i in range(len(low)):
    lows.append(low[i].text)
l = []

for i in lows:
    n = ''
    for k in i:
        if k.isdigit():
            n += k
    l.append(round((int(n) - 32) * 5 / 9, ndigits=0))
lows = l
if len(lows) < len(day_name):
    lows.append(np.nan)

forecast.iloc[3, :] = lows
forecast.to_excel('Weather_Forecast_Easy.xlsx')
print(forecast)
