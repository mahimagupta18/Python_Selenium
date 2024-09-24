# Test Case
# ---------------------------------------
# Open web Browser (chrome/firefox/edge).
# Open URL(https://opensource-demo.orangehrmlive.com/)
# Enter username (Admin)
# Enter password (admin123).
# Click on Login
# Capture title of the home page.(Actual title).
# Verify title of the page : OrangeHRm (Expected)
# Close browser.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Specify the path to the chromedriver executable
service = Service('D:\Java\Selenium\Driver\chromedriver-win64\chromedriver.exe')

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service)

# Open a webpage
driver.get("https://opensource-demo.orangehrmlive.com")

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.ID, "password").send_keys("admin123")
driver.find_element(By.ID, "submit").click()

act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
driver.close()

# Wait for a few seconds to see the results
# driver.implicitly_wait(5)
