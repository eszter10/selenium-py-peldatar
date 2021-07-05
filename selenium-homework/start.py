from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

q = driver.find_element_by_name("q")
q.send_keys("idokep.hu")
time.sleep(5)

#submit = driver.find_element_by_name('btnK')
#submit.click()

q.submit()

time.sleep(3)

driver.close()
