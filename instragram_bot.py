from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = "your_dummy_username"
PASSWORD = "your_dummy_password"

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")

time.sleep(4)

# Login
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)

time.sleep(5)

# Dismiss dialogs
try:
    driver.find_element(By.XPATH, "//button[text()='Not Now']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Not Now']").click()
except:
    pass

# Search for cbitosc
search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_box.send_keys("cbitosc")
time.sleep(3)
search_box.send_keys(Keys.RETURN)
search_box.send_keys(Keys.RETURN)

time.sleep(5)

# Follow the account
try:
    follow_button = driver.find_element(By.XPATH, "//button[text()='Follow']")
    follow_button.click()
    time.sleep(2)
except:
    print("Already following or button not found")

# Extract bio and follower info
time.sleep(2)
bio = driver.find_element(By.XPATH, "//div[@class='_aacl _aacp _aacw _aacx _aada']").text
stats = driver.find_elements(By.CLASS_NAME, "_ac2a")

followers = stats[1].text if len(stats) > 1 else "N/A"
following = stats[2].text if len(stats) > 2 else "N/A"

with open("cbitosc_info.txt", "w", encoding="utf-8") as f:
    f.write(f"Bio: {bio}\n")
    f.write(f"Followers: {followers}\n")
    f.write(f"Following: {following}\n")

print("✅ Data saved to cbitosc_info.txt")
driver.quit()
