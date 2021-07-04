from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

try:
    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/")
    found_elements = [driver.find_element_by_id("element1"), driver.find_element_by_id("element2"), driver.find_element_by_id("element3"),
                      driver.find_element_by_id("element4"), driver.find_element_by_id("element5")]
    for element in found_elements:
        if element.tag_name == "button" or element.get_attribute("onclick") is not None:
            button_text = element.text
            element.click()
            break
    message_text = driver.find_element_by_id("result").text
    assert f'{button_text} was clicked' == message_text
    print("test finished OK")

except NoSuchElementException as e:
    print('Element not found: ', e)
finally:
    driver.close()
