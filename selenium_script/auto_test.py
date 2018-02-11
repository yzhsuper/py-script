#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver

browser = webdriver.PhantomJS()
browser = webdriver.Firefox()
try:
    browser.get('https://store.steampowered.com/join/')
    time.sleep(3)
    browser.find_element_by_id("accountname").send_keys('remain')
    account_check_btn = browser.find_element_by_xpath('//*[@id="account_form_box"]/div[2]/div[1]/div[2]/span[1]/a')
    account_check_btn.click()

    # account_check_result = browser.get('https://store.steampowered.com/join/checkavail/?accountname=%s&count=1' % 'remain')
    # print account_check_result
    # browser.refresh()
    browser.find_element_by_id("password").send_keys('test_pass')
    browser.find_element_by_id("reenter_password").send_keys('test_pass')
    # browser.find_element_by_id("imageLogin").click()
    # time.sleep(5)
    # print browser.current_url
    # browser.save_screenshot('bd.png')
    # browser.quit()
except BaseException as e:
    print e
finally:
    pass
    # browser.quit()