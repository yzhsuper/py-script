#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver

browser = webdriver.Firefox()
try:
    # browser.get('http://www.play.com:6969/login_debug/76561198308782250?')
    # time.sleep(3)
    browser.get('http://vacations.ctrip.com/tours/d-thailand-100021#ctm_ref=va_hom_s2_idx_p0_l5_5_txt')
    browser.find_element_by_class_name('.top-nav > li:nth-child(6) > a:nth-child(1)').click()
    time.sleep(5)
    browser.save_screenshot('bd.png')
    # browser.quit()
except BaseException as e:
    print e
