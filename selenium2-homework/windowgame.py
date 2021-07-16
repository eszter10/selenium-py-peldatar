from selenium import webdriver
import random

driver = webdriver.Chrome()

driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/windowgame.html")
button_list = driver.find_elements_by_tag_name("button")
for _ in range(10):
    button_list[random.randint(0, len(button_list)-1)].click()
    driver.switch_to.window(driver.window_handles[-1])
    print(driver.find_element_by_tag_name("h1").text)
    driver.switch_to.window(driver.window_handles[0])

driver.close()