from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.google.com")
text_area = driver.find_element(By.ID, 'APjFqb')
# before clearing , i need to wait for web page to load up
time.sleep(2)
text_area.clear()
text_area.send_keys("machine learning")
text_area.send_keys(Keys.RETURN)
time.sleep(5)
driver.back()
time.sleep(5)
elem_click = driver.find_element(By.LINK_TEXT, 'English')
time.sleep(2)
elem_click.click()
time.sleep(5)
elem_click = driver.find_element(By.LINK_TEXT, 'About')
time.sleep(2)
elem_click.click()
time.sleep(5)
elem_click = driver.find_element(By.LINK_TEXT, 'View all our products')
time.sleep(5)
elem_click.click()
# refresh the web page
driver.refresh()
time.sleep(5)
# forward and backward navigation buttons
driver.back()
time.sleep(5)
driver.forward()
# scrolling
elem = driver.find_element(By.TAG_NAME, 'html')
# scroll down
elem.send_keys(Keys.END)
time.sleep(5)
# scroll up
elem.send_keys(Keys.HOME)
# getting current url
print(driver.current_url)
time.sleep(20)
