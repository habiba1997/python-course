from selenium import webdriver
import time

from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
a = driver.find_element(By.ID, 'email')
a.send_keys('cuonglieu3256@gmail.com')
b = driver.find_element(By.ID, 'pass')
b.send_keys('password')
c = driver.find_element(By.ID, 'loginbutton')
c.click()
post_box = driver.find_element(By.XPATH, "//*[@name='xhpc_message']")
time.sleep(5)
post_box.click()
time.sleep(5)
post_box.send_keys("Testing using Name not ID.Selenium is easy.")
time.sleep(5)
post_it = driver.find_element(By.XPATH, "//*[@id='u_0_1a']/div/div[6]/div/ul/li[2]/button")
post_it.click()
