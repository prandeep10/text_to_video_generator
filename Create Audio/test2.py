from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Create a new Chrome WebDriver (assuming chromedriver is in the same folder as your script)
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://www.narakeet.com/languages/hindi-text-to-voice/')

# Find the select element and choose the "nitesh" option
select_element = Select(driver.find_element(By.ID, 'cfgVideoVoice'))
select_element.select_by_value('nitesh')

# Get the Python variable named 'text'
text = "Your text goes here."

# Find the textarea element and paste the text
textarea_element = driver.find_element(By.NAME, 'unparsedScript')
textarea_element.send_keys(text)

# Find the submit button and click on it
submit_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
submit_button.click()

# Close the browser
driver.quit()
