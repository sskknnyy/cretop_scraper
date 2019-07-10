#!/usr/bin/python3

from selenium import webdriver

## Settings
cretop_id = ""
cretop_pw = ""

## Driver Load
## Chrome Test
# driver = webdriver.Chrome('./chromedriver')
driver = webdriver.Ie('./chromedriver')
driver.implicitly_wait(3)

## Page Connect
driver.get('https://www.cretop.com')

## Login Sessing
driver.find_element_by_id('in_id').send_keys(cretop_id)
driver.find_element_by_id('in_pw').send_keys(cretop_pw)

driver.find_element_by_id('loginBtn1').click()