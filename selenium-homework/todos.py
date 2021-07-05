from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

try:
    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/todo.html")
    todos = driver.find_elements_by_xpath('//*[@class="done-false"]')
    for todo in todos:
        print('TODO:', todo.text)
except NoSuchElementException as e:
    print('Element not found: ', e)
finally:
    driver.close()
