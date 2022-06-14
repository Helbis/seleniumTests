#!/usr/bin/env python3

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://avid-recruitment.azurewebsites.net")

# Login to application
formUsername = driver.find_element(By.ID, "formUsername")
formPassword = driver.find_element(By.ID, "formPassword")
sign_in_button = driver.find_element(By.ID, "sign-in-button")

formUsername.send_keys("admin")
formPassword.send_keys("testPassword")
sign_in_button.click()


# driver.close()
