from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

q = driver.find_element_by_name("q")
q.send_keys("idokep.hu")


submit = driver.find_element_by_name("q")
submit.click()

driver.close()
