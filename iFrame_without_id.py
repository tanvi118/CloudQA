from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")

wait = WebDriverWait(driver, 10)
iframe = wait.until(
    EC.presence_of_element_located((By.XPATH, "(//iframe)[1]"))
)

driver.switch_to.frame(iframe)
heading = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h1 | //h2 | //h3"))
)

print("Iframe heading found:", heading.text)

driver.switch_to.default_content()

print("Iframe test completed successfully.")
driver.quit()

