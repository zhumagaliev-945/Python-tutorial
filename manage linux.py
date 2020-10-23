from selenium import webdriver
from selenium.webdriver import ActionChains



browser = webdriver.Chrome('/home/kanagat/Документы/GitHub/Python-tutorial/chromedriver')
browser.get('https://vk.com')
browser.maximize_window()
browser.find_element_by_xpath('//*[@id="index_email"]').send_keys('87071431070')
browser.find_element_by_xpath('//*[@id="index_pass"]').send_keys('Jameco_08')
browser.find_element_by_xpath('//*[@id="index_login_button"]').click()
browser.find_element_by_class_name().click()

