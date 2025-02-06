from pages.base_page import BasePage
from pages.tensor_about_page import TensorAboutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from loguru import logger


class TensorMainPage(BasePage):

    LINK_CORRECT = 'https://tensor.ru/'
    BLOCK_NAME = 'Сила в людях'
    VALUE_BLOCK_LOCATOR = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content .tensor_ru-Index__card-title")
    VALUE_ABOUT_LOCATOR = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content .tensor_ru-link")
    
    def url_is_correct(self):
        tensor_url_correct = WebDriverWait(self.browser, 10).until(
            EC.url_to_be(self.LINK_CORRECT)
        )

        assert tensor_url_correct

        logger.info('Корректный юрл https://tensor.ru/.')

    def block_is(self):
        block = tensor_url_correct = WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element(self.VALUE_BLOCK_LOCATOR, self.BLOCK_NAME)
        )

        assert block

        logger.info('Блок "Сила в людях" присутствует.')

    def go_to_about_tensor(self):
        block_more_details = self.get_href_by_element(self.VALUE_ABOUT_LOCATOR)
        self.get_to_url(block_more_details)

        return TensorAboutPage(self.browser)