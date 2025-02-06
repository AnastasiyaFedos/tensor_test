"""

    Второй сценарий.
    1. Перейти на https://sbis.ru/ в раздел "Контакты"
    2. Проверить, что определился ваш регион (в нашем примере Ярославская обл.) и есть список партнеров.
    3. Изменить регион на Камчатский край
    4. Проверить, что подставился выбранный регион, список партнеров изменился, url и title содержат информацию выбранного региона

"""
from pages.sbis_main_page import SbisMainPage
    

def test_scenario_two(browser):
    sbis_main_page = SbisMainPage(browser)
    sbis_contact_page = sbis_main_page.go_to_contacts() #открыли окно Контакты
    sbis_contact_page = sbis_main_page.get_to_contacts() #перешли в окно Контакты
    sbis_contact_page.find_region() #определить регион
    sbis_contact_page.find_list_partners() # определить список партнеров
    sbis_contact_page.change_region() #сменить регион, проверить регион
    sbis_contact_page.find_list_partners_new() #проверить список партнеров