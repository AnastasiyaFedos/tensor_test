from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser):
        self.browser = browser

    def get_to_url(self, url):                                  #переход по юрл
        self.browser.get(url)

    def find_to_locator(self, locator):                  #поиск по локатору
         return WebDriverWait(self.browser, 10).until(
        EC.presence_of_element_located(locator))
    
    def click_locator(self, locator):                    #клик по найденному локатору
        self.find_to_locator(locator).click()
    
    def finds_element_by_locator(self, locator):         #множ поиск по локатору
        return self.browser.find_elements(*locator)
    
    def get_href_by_element(self, locator):  #получение атрибута (по умолчанию - получение ссылки)
        elem = self.find_to_locator(locator)

        return elem.get_attribute("href")
