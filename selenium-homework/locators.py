from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

try:
    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/kitchensink.html")

    driver.find_element_by_name("cars")
    driver.find_element_by_id("bmwradio")
    driver.find_element_by_xpath('//*[@id="openwindow"]')

    print("test finished OK")

except NoSuchElementException as e:
    print('Element not found: ', e)
finally:
    driver.close()



