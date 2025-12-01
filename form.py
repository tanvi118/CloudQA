from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")

wait = WebDriverWait(driver, 10)

def get_by_label(text):
    return wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//label[contains(text(), '{text}')]/following::input[1]")
        )
    )

first = get_by_label("First Name")
first.send_keys("Tanvi")

last = get_by_label("Last Name")
last.send_keys("Vitankar")

gender = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Female')]/preceding::input[1]")))
gender.click()

print("Form test done.")
driver.quit()

