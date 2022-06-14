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


def fdElement(name, by=By.ID, wait=5):
    global driver, exp, WebDriverWait, EC

    try:
        wait = WebDriverWait(driver, wait)
        element = wait.until(EC.presence_of_element_located((by, name)))

    except exp.NoSuchElementException as e:
        print(f"Looking for {name}")
        print(e)
        exit(1)

    except Exception as e:
        print(f"Looking for {name}")
        print(e)
        exit(1)

    return element


driver = webdriver.Firefox()
driver.get(url)


# Login to application
formUsername = fdElement("formUsername")
formPassword = fdElement("formPassword")
sign_in_button = fdElement("sign-in-button")

formUsername.send_keys("admin")
formPassword.send_keys("testPassword")
sign_in_button.click()

# Wait for the website to load
_ = fdElement("formLimit")

# Check how many elements are in a list
print("Trying to locate all elements with folder-id className")
folder = fdElement("folder-id")
folder_path = fdElement("folder-path")
print(type(folder))

if type(folder) == "list":
    for tr in folder:
        print(f"tr: {tr}")


# Find and type parameters for search
formLimit = fdElement("formLimit")
formLimit.clear()
formLimit.send_keys("1")

formQuery = fdElement("formQuery")
formQuery.send_keys("copyTest")

buttonOptions = fdElement("buttonOptions")
buttonOptions.click()

# Check if folder with id 10 was presented
wait = WebDriverWait(driver, 10)
elems = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))

folder = fdElement("folder-id", by=By.CLASS_NAME)
folder_path = fdElement("folder-path", by=By.CLASS_NAME)
# print(type(folder))

folder.click()

wait = WebDriverWait(driver, 10)
elems = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "h3")))
folderNumber = fdElement("folder-id")

print(f"folderNumber.text: {folderNumber.text}")
if folderNumber.text == idLooked:
    print("Successfully picked number 10")

# driver.close()
