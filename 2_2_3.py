from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#Открыть страницу
link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
#Посчитать сумму заданных чисел   
    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")
    x = int(x_element.text)
    y = int(y_element.text)
    sum_xy = x + y
    
#Выбрать в выпадающем списке значение равное расчитанной сумме    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum_xy))

#Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
# Успеваем скопировать код за 30 секунд
    time.sleep(30)
# Закрываем браузер после всех манипуляций
    browser.quit()

# Hе забываем оставить пустую строку в конце файла