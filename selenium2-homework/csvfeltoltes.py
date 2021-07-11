import csv
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://gentle-bay-0e4e13803.azurestaticapps.net/another_form.html')


def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element


submit_button = driver.find_element_by_id('submit')

with open('table_in.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        print(row)
        find_and_clear_by_id('fullname').send_keys(row[0])

        find_and_clear_by_id('email').send_keys(row[1])

        find_and_clear_by_id('dob').send_keys(row[2])

        find_and_clear_by_id('phone').send_keys(row[3])

        submit_button.click()

save = driver.find_element_by_xpath('/html/body/main/div/button')
save.click()
