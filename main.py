#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://avid-recruitment.azurewebsites.net")

# Login to application
formUsername = driver.find_element(By.ID, "formUsername")
formPassword = driver.find_element(By.ID, "formPassword")
sign_in_button = driver.find_element(By.ID, "sign-in-button")

formUsername.send_keys("admin")
formPassword.send_keys("testPassword")
sign_in_button.click()

wait = WebDriverWait(driver, 10)
elem = wait.until(EC.presence_of_all_elements_located((By.ID, "formLimit")))

formLimit = driver.find_element(By.ID, "formLimit")
formLimit.send_keys("1")

formQuery = driver.find_element(By.ID, "formQuery")
formQuery.send_keys("copyTest")


# driver.close()
