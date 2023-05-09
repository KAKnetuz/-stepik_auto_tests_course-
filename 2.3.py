from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def main():
    try:
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        button = browser.find_element(By.CSS_SELECTOR, ".card-body button")

        WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".card h5#price"), "$100")
        )
        button.click()

        x_ = browser.find_element(By.CSS_SELECTOR, ".form-group #input_value")
        x = int(x_.text)
        y = calc(x)

        input1 = browser.find_element(By.CSS_SELECTOR, ".form-group input")
        input1.send_keys(y)

        submit_button = browser.find_element(By.CSS_SELECTOR, ".form-group button")
        submit_button.click()

        print(browser.switch_to.alert.text.split(': ')[-1])

    finally:
        time.sleep(10)
        browser.quit()


if __name__ == '__main__':
    main()
