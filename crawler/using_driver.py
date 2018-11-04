

#coding=utf-8

#Reference address: https://blog.csdn.net/chengxuyuanyonghu/article/details/79154468

import time

from splinter import Browser
from selenium import webdriver


def splinter(url):
    browser=Browser()
    browser.visit(url)
    time.sleep(5)
    browser.find_by_id('idInput').fill('xxxxx')
    browser.find_by_id('pwdInput').fill('xxxxx')
    browser.find_by_id('loginBtn').click()
    time.sleep(8)
    browser.quit()


def selenium(url):
    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com")
    print(driver.title)
    driver.maximize_window()
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    driver.get_screenshot_as_file("D:/data/baidu.png")
    driver.refresh()
    time.sleep(3)
    driver.close()
    driver.quit()


if __name__=='__main__':
    url='http://www.126.com'
    splinter(url)