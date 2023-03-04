from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
#Посчитать математическую функцию от x. Используйте функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле. Не забудьте добавить этот код в начало вашего скрипта    
def calc(x): return str(math.log(abs(12*math.sin(int(x)))))

#Открыть страницу http://suninjuly.github.io/get_attribute.html
link = "http://suninjuly.github.io/get_attribute.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
#Найти на ней элемент-картинку, который является изображением сундука с сокровищами    
    x_element = browser.find_element(By.ID, "treasure")
#Взять у этого элемента значение атрибута valuex, которое является значением x для задачи    
    x = x_element.get_attribute("valuex")
    y = calc(x)
#Ввести ответ в текстовое поле
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
#Отметить checkbox "I'm the robot
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
#Выбрать radiobutton "Robots rule!"
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
#Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
# Успеваем скопировать код за 30 секунд
    time.sleep(30)
# Закрываем браузер после всех манипуляций
    browser.quit()

# Hе забываем оставить пустую строку в конце файла