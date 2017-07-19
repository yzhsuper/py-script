#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver

browser = webdriver.PhantomJS()
browser = webdriver.Firefox()
try:
    browser.get('http://www.igxe.cn/')
    login_btn = browser.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div[2]/ul/li[5]/a[2]')
    login_btn.click()
    # browser.refresh()
    browser.find_element_by_id("steamAccountName").send_keys('remainvitality')
    browser.find_element_by_id("steamPassword").send_keys('steamyzh1081250324')
    browser.find_element_by_id("imageLogin").click()
    time.sleep(5)
    print browser.current_url
    browser.save_screenshot('bd.png')
    browser.quit()
except BaseException as e:
    print e
