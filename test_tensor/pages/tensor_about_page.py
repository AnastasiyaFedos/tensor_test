from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from loguru import logger


class TensorAboutPage(BasePage):

    LINK_CORRECT = 'https://tensor.ru/about'
    VALUE_WORKING_POST = (By.XPATH, '//img[contains(@class, "tensor_ru-About__block3-image")]')
    
    def url_is_correct(self):
        tensor_url_correct = WebDriverWait(self.browser, 10).until(
            EC.url_to_be(self.LINK_CORRECT)
        )

        assert tensor_url_correct
        logger.info('Корректный переход. URL имеет адрес: https://tensor.ru/about')

    def correct_photos(self):
        working_photos = self.finds_element_by_locator(self.VALUE_WORKING_POST)
        widths, heights = [], []

        for photo in working_photos:
            heights.append(photo.get_attribute('height'))
            logger.info(photo.get_attribute('height'))
            widths.append(photo.get_attribute('width'))

        if len(set(widths)) == 1 and len(set(heights)) == 1:
            correct_photo = True
        else:
            correct_photo = False

        assert correct_photo

        logger.info(f'Корректные размеры фотографий раздела "Работаем"')