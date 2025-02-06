from pages.base_page import BasePage
from pages.sbis_contact_page import SbisContactPage
from selenium.webdriver.common.by import By
import time


class SbisMainPage(BasePage):

    LINK_HOME = "https://sbis.ru/"
    VALUE_LOCATOR_CONTACT_MENU = (By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu")
    VALUE_LOCATOR_CONTACTS = (By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu .sbisru-link")
    VALUE_TENSOR = (By.CSS_SELECTOR, "[title='tensor.ru']")
    
    def go_to_contacts(self):
        self.get_to_url(self.LINK_HOME)
        self.click_locator(self.VALUE_LOCATOR_CONTACT_MENU)

        
    def get_to_contacts(self):
        link_contacts = self.get_href_by_element(self.VALUE_LOCATOR_CONTACTS)
        time.sleep(5)
        self.get_to_url(link_contacts)

        return SbisContactPage(self.browser)    
