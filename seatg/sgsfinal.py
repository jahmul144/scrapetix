#!/usr/bin/env python3.5
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup

EVENTSECTION = ('date', 'time', 'title', 'button')
CLUBURLEND = ('atlanta-united-fc-tickets','chicago-fire-tickets','colorado-rapids-tickets','fc-dallas-tickets','columbus-crew-sc','dc-united','houston-dynamo','la-galaxy','new-england-revolution','minnesota-united-fc','portland-timbers','new-york-city-fc','new-york-reb-bulls','real-salt-lake','san-jose-earthquakes','orlando-city-sc','philadelphia-union','seattle-sounders-fc','sporting-kansas-city')


def get_data(column, soup):
	"""Returns date, time, event, and price specified by *column*."""
	event_data_list = []
	for element in soup.find_all(class_='event-listing-{}'.format(column)):
		text = element.get_text().strip()
		if 'From' in text:
			value = text.strip('From').strip()	
			event_data_list.append(value)
		else:
			event_data_list.append(text)
	return event_data_list

def pack_data():
	"""Return all data for event based on team"""
	display = Display(visible=0, size=(800,600))
	#display must start before calling webdriver
	display.start()
	driver= webdriver.Chrome('/home/ubuntu/Downloads/chromedriver')
	for element in CLUBURLEND:
		driver.get('https://seetgeek.com/{}'.format(element))
		print (driver.title)
		html_source = driver.page_source
		soup = BeautifulSoup(html_source, 'html.parser')

		#calls get_data function drops in EVENTSECTION data/time etc into parameters for function, get_data loops through EVENTSECTION returns data
		data_list = [get_data(e, soup) for e in EVENTSECTION]
		#data_list returns list of list for each EVENTSECTION, so zip each list together to merge 
		print(list(zip(data_list[0],data_list[1],data_list[2],data_list[3])))

	driver.quit()
	display.stop()

if __name__ == "__main__":
	pack_data()


