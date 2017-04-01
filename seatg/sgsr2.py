#!/usr/bin/env python3.5
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup

DISPLAY = Display(visible=0,size=(800,600))
DRIVER=webdriver.Chrome('/home/ubuntu/Downloads/chromedriver')


def get_title():
	DISPLAY.start()
	
	DISPLAY.stop()
	
	
	

get_title()







