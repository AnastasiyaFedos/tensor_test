from pages.base_page import BasePage
from pages.tensor_main_page import TensorMainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
import time

class SbisContactPage(BasePage):

    VALUE_TENSOR = (By.CSS_SELECTOR, "[title='tensor.ru']")
    VALUE_REGION = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text')
    VALUE_LIST_PARTNERS = (By.CSS_SELECTOR, '.sbisru-Contacts-List__city')
    VALUE_NEW_REGION = (By.XPATH, '//span[text()="41 Камчатский край"]')
    VALUE_CORRECT_CITY = (By.ID, 'city-id-2')

    CORRECT_REGION = 'Республика Башкортостан'
    CORRECT_CITY = 'Уфа'
    NEW_CORRECT_REGION = 'Камчатский край'
    NEW_CORRECT_CITY = 'Петропавловск-Камчатский'

    def go_to_banner(self):
        link_banner = self.get_href_by_element(self.VALUE_TENSOR)
        self.get_to_url(link_banner)

        return TensorMainPage(self.browser)
    
    def find_region(self):
        region_right = WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(self.VALUE_REGION, self.CORRECT_REGION)
        )

        assert region_right

        logger.info(f'Корректно определен регион.')
        
    def find_list_partners(self):
        partners_right = WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(self.VALUE_CORRECT_CITY, self.CORRECT_CITY)
        )

        assert partners_right

        logger.info('Корректный список партнеров РБ.')
    
    def change_region(self):
        region = self.click_locator(self.VALUE_REGION)
        new_region = self.click_locator(self.VALUE_NEW_REGION)
        new_region_right = WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(self.VALUE_REGION, self.NEW_CORRECT_REGION)
        )

        assert new_region_right

        logger.info('Корректно сменен регион на Камчатский край.')
    
    def find_list_partners_new(self):
        partners_right = WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(self.VALUE_CORRECT_CITY, self.NEW_CORRECT_CITY)
        )

        assert partners_right

        logger.info('Корректный новый список партнеров.')
