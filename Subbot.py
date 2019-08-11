# -*- coding: utf-8 -*-
"""

@author: ubermachine
"""
from selenium import webdriver
from time import sleep
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

options = webdriver.ChromeOptions()

# specify headless mode
#options.add_argument('headless')
# specify the desired user agent
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(10)
driver.get('https://www.youtube.com/') 
driver.find_element_by_xpath("/html[1]/body[1]/ytd-app[1]/div[1]/div[1]/ytd-masthead[1]/div[3]/div[2]/div[2]/ytd-button-renderer[1]/a[1]/paper-button[1]").click()
driver.find_element_by_xpath("//input[@id='identifierId']").send_keys("GMAIL ID")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
driver.find_element_by_name("password").send_keys("PASSWORD HERE")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[1]").click()
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/ul[1]/label[1]/li[1]/span[1]/span[1]/input[1]").click()
driver.find_element_by_xpath("//button[@id='identity-prompt-confirm-button']").click()

driver.get('https://www.subpals.com/') 
driver.find_element_by_link_text("Login / Register").click()
driver.switch_to.frame(1)
driver.find_element_by_name("channelid").send_keys("YOUR CHANNEL ID hERE")
driver.find_element_by_name("submit").click()
sleep(3)

#driver.find_element_by_xpath('//*[@id="image-1524687372382"]').click()
driver.find_element_by_name("password").send_keys("SUBPAL PASSWORD")
driver.find_element_by_name("submit").click()
sleep(5)
driver.switch_to.frame(0)
driver.find_element_by_link_text("Activate").click()


driver.find_element_by_id('likeSub2').click()
#driver.switch_to_window('win_ser_1')
driver.switch_to_window(driver.window_handles[2])
sleep(5)
driver.find_element_by_xpath("//*[@id='top-level-buttons']/ytd-toggle-button-renderer[1]/a").click()
driver.find_element_by_xpath("//yt-formatted-string[@class='style-scope ytd-subscribe-button-renderer']").click()
sleep(10)
driver.close()
driver.switch_to_window(driver.window_handles[0])
sleep(5)
driver.switch_to.frame(0)
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[4]/div[1]/a[2]/img[1]").click()




    