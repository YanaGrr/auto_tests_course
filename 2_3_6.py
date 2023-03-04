from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
#Посчитать математическую функцию от x. Используйте функцию calc(), которая рассчитает и вернет вам значение функции, которое нужно ввести в текстовое поле. Не забудьте добавить этот код в начало вашего скрипта    
def calc(x): return str(math.log(abs(12*math.sin(int(x)))))

#Открыть страницу
link = "http://suninjuly.github.io/redirect_accept.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
#Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
#Переключиться на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
#Считать значение для переменной x. Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
#Ввести ответ в текстовое поле
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)    
#Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
# Успеваем скопировать код за 30 секунд
    time.sleep(30)
# Закрываем браузер после всех манипуляций
    browser.quit()

# Hе забываем оставить пустую строку в конце файла