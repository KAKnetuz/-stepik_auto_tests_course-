from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


def sel(link):
    browser = webdriver.Chrome()
    browser.get(link)

    num_list = ['first', 'second', 'third']
    for num in num_list:
        element = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.{}".format(num))
        element.send_keys("My answer")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text
    browser.quit()
    return welcome_text


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            sel(link),
            "Congratulations!"
        )

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.assertEqual(
            "Congratulations! You have successfully registered!",
            sel(link),
            "Congratulations!"
        )


if __name__ == '__main__':
    unittest.main()