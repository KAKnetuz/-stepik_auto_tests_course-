from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

# находим элементы
num1_in_text = browser.find_element(By.ID, "num1")
num2_in_text = browser.find_element(By.ID, "num2")

# вытаскиваем заданные числа
num1 = int(num1_in_text.text)
num2 = int(num2_in_text.text)

# находим и выбираем значение, которое является суммой этих 2 чисел
select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
select.select_by_value(str(num1 + num2))

# нажимаем на кнопку
send_button = browser.find_element(By.CLASS_NAME, "btn-default")
send_button.click()