from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

try:
    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/videos.html")
    html5video = driver.find_element_by_id("html5video")
    html5video.send_keys(Keys.SPACE)
    time.sleep(6)
    html5video.screenshot('video_scrnshot.png')
    time.sleep(5)

    button = driver.find_element_by_xpath('/html/body/div/button[1]')
    button.click()
   # video1.send_keys(Keys.SPACE)
    time.sleep(6)
    video1 = driver.find_element_by_id('video1')
    video1.screenshot('video1_scrnshot.png')
    time.sleep(5)

    youtubeframe = driver.find_element_by_id("youtubeframe")
    youtubeframe.click()
   # youtubeframe.send_keys(Keys.SPACE)
    time.sleep(6)
    youtubeframe.screenshot('youtubeframe_scrnshot.png')
    time.sleep(5)
finally:
    driver.close()