from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def main():
    try:
        link = "http://suninjuly.github.io/math.html"
        browser = webdriver.Chrome()
        browser.get(link)

        x_element = browser.find_element(By.CSS_SELECTOR, ".form-group #input_value")
        x = x_element.text
        y = calc(x)

        input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
        input1.send_keys(y)

        option1 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
        option1.click()

        option2 = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
        option2.click()

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()


    finally:
        time.sleep(10)
        browser.quit()


if __name__ == '__main__':
    main()
