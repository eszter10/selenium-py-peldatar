
#from webdriver_manager.chrome import ChromeDriverManager


# In order for ChromeDriverManager to work you must pip install it in your own environment.
#driver = webdriver.Chrome(ChromeDriverManager().install())

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()

try:
    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/trickyelements.html")
    found_elements = [driver.find_element_by_id("element1"), driver.find_element_by_id("element2"), driver.find_element_by_id("element3"),
                      driver.find_element_by_id("element4"), driver.find_element_by_id("element5")]
    time.sleep(3)
    for element in found_elements:
        if element.tag_name == "button" or element.get_attribute("onclick") is not None:
            button_text = element.text
            element.click()
            break
    time.sleep(3)
    message_text = driver.find_element_by_id("result").text
    assert f'{button_text} was clicked' == message_text
    print("test finished OK")

except NoSuchElementException as e:
    print('Element not found: ', e)
finally:
    driver.close()
