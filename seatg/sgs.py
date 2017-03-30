#!/usr/bin/env python3.5
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup

display = Display(visible=0, size=(800, 600))
display.start()
driver=webdriver.Chrome(
"/home/ubuntu/Downloads/chromedriver")
driver.get('https://seetgeek.com/atlanta-united-fc-tickets')
print(driver.title)


html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

data = []

time = []
for element in soup.find_all(class_='event-listing-date'):
	time.append(element.get_text().strip())

date =[]
for element in soup.find_all(class_='event-listing-time'):
	date.append(element.get_text().strip())

event = []
for element in soup.find_all(class_='event-listing-title'):
	event.append(element.get_text().strip())

price = []
for element in soup.find_all(class_='event-listing-button'):
	price.append(element.get_text().strip())



data.append(list(zip(time,date,event,price)))
print(data)
driver.quit()
display.stop()




