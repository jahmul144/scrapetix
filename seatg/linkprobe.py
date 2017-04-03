#!/usr/bin/env python3.5
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


CLUBURLEND = ('atlanta-united-fc-tickets','chicago-fire-tickets')



def pack_data():
	"""Return all data for event based on team"""
	display = Display(visible=0, size=(800,600))
	#display must start before calling webdriver
	display.start()
	driver= webdriver.Chrome('/home/ubuntu/Downloads/chromedriver')
	for element in CLUBURLEND:
		driver.get('https://seetgeek.com/{}'.format(element))
		#print (driver.title)
		#find_element just find one find_elements find all the classes
		links = driver.find_elements_by_class_name('event-listing-title')
		list_links_text = []
		for link in links:
			list_links_text.append(link.text)
		
		for linktext in list_links_text:
			driver.find_element_by_link_text(linktext).click()

			print(driver.title)
			driver.back()
	driver.quit()
	display.stop()

if __name__ == "__main__":
	pack_data()

