#!/usr/bin/python
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
print browser, browser.title

# elem = browser.find_element_by_name("p") # Find the query box
# elem.send_keys("seleniumhq" + Keys.RETURN)
# time.sleep(0.2) # Let the page load, will be added to the API
try:
    ele = browser.find_element_by_xpath("id('kw')")
    print ele
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
browser.close()