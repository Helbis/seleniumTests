#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exp


# Create browser instance and check if website loaded
idLooked = 10
azure = "azurewebsites"
url = "https://avid-recruitment." + azure + ".net"


def fdElement(driver, name, by=By.ID, wait=0):
    """
    fdElement returns False if fails or found element otherwise
    """
    global exp, WebDriverWait, EC

    try:
        wait = WebDriverWait(driver, wait)
        element = wait.until(EC.presence_of_element_located((by, name)))

    except exp.NoSuchElementException as e:
        print(e)
        return False

    except Exception as e:
        print(e)
        return False

    return element


driver = webdriver.Firefox()
driver.get(url)
wait = WebDriverWait(driver, 100)
waitElem = wait.until(EC.presence_of_element_located((By.ID, "formUsername")))
print(f"waitElem: {waitElem}")

# Login to application
formUsername = driver.find_element(By.ID, "formUsername")
print(f"formUsername: {formUsername}")
formPassword = driver.find_element(By.ID, "formPassword")
sign_in_button = driver.find_element(By.ID, "sign-in-button")

formUsername.send_keys("admin")
formPassword.send_keys("testPassword")
sign_in_button.click()

# Wait for the website to load
wait = WebDriverWait(driver, 10)
elem = wait.until(EC.presence_of_all_elements_located((By.ID, "formLimit")))

# Check how many elements are in a list
print("Trying to locate all elements with folder-id className")
try:
    folder = driver.find_elements(By.CLASS_NAME, "folder-id")
    folder_path = driver.find_element(By.CLASS_NAME, "folder-path")
    print(type(folder))

    if type(folder) == "list":
        for tr in folder:
            print(f"tr: {tr}")

except exp.NoSuchElementException as e:
    print(e)

# Find and type parameters for search
formLimit = driver.find_element(By.ID, "formLimit")
formLimit.clear()
formLimit.send_keys("1")

formQuery = driver.find_element(By.ID, "formQuery")
formQuery.send_keys("copyTest")

buttonOptions = driver.find_element(By.ID, "buttonOptions")
buttonOptions.click()

# Check if folder with id 10 was presented
wait = WebDriverWait(driver, 10)
elems = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))

try:
    folder = driver.find_element(By.CLASS_NAME, "folder-id")
    folder_path = driver.find_element(By.CLASS_NAME, "folder-path")
    # print(type(folder))

    folder.click()
except exp.NoSuchElementException as e:
    print(e)


wait = WebDriverWait(driver, 10)
elems = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "h3")))
folderNumber = driver.find_element(By.ID, "folder-id")

print(f"folderNumber.text: {folderNumber.text}")
if folderNumber.text == idLooked:
    print("Successfully picked number 10")

# driver.close()
