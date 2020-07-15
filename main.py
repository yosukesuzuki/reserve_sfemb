import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# install same version as your chrome
import chromedriver_binary

TARGET_URL = "https://www.timetap.com/emb/329380#/"


def scrape_sf() -> bool:
    driver = webdriver.Chrome()
    driver.get(TARGET_URL)
    next_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button#nextBtn"))
    )
    next_input.click()
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "mat-list"))
    )
    next_next_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button#nextBtn"))
    )
    next_next_input.click()
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "label.selectTimeLabel"))
    )
    next_next_next_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button#nextBtn"))
    )
    disabled = next_next_next_input.get_attribute('disabled')
    if disabled == 'true':
        for d in driver.find_elements_by_css_selector('span.ng-star-inserted'):
            print(d.text)
        driver.close()
        return False
    next_next_next_input.click()
    save_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button#saveBtn"))
    )
    save_input.click()
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h2"))
    )
    driver.save_screenshot("{}screenshot.png".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
    return True


def main():
    for i in range(1, 15):
        print("try: {}".format(i))
        results = scrape_sf()
        if results:
            break


if __name__ == '__main__':
    main()
