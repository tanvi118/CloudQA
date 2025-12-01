from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")

wait = WebDriverWait(driver, 10)
def switch_to_frame_containing_element(by, value, driver):
    try:
        element = driver.find_element(by, value)
        return True
    except:
        pass

    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    for iframe in iframes:
        driver.switch_to.frame(iframe)
        found = switch_to_frame_containing_element(by, value, driver)
        if found:
            return True
        driver.switch_to.parent_frame()
    return False

if switch_to_frame_containing_element(By.TAG_NAME, "h1", driver):
    heading = driver.find_element(By.TAG_NAME, "h1")
    print("Found heading in nested iframe:", heading.text)
else:
    print("Element not found in any iframe.")

driver.switch_to.default_content()
driver.quit()


