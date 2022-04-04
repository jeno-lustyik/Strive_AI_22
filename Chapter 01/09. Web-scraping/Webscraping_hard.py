import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c'
pth = r'D:\Users\lusty\Strive\GitHub\Strive_AI_22\09. Web-scraping\chromedriver.exe'
brave_path = 'C:\Program Files\BraveSoftware\Brave-Browser\Application'

option = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path=pth, options=option)
driver.get(url)

sleep(3)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[3]/button[1]').click()
sleep(1)
for i in range(0, 10, 1):
    button = f'/html/body/div[1]/main/div[2]/main/div[1]/section/div[2]/details[{i+2}]/summary'
    driver.find_element(By.XPATH, button).click()
    sleep(3)

box = driver.find_element(By.XPATH, '//*[@class="DailyForecast--DisclosureList--msYIJ"]')
print(box.text)
