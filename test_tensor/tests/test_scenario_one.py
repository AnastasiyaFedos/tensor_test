"""

    Первый сценарий.
    1. Перейти на https://sbis.ru/ в раздел "Контакты"
    2. Найти баннер Тензор, кликнуть по нему
    3. Перейти на https://tensor.ru/
    4. Проверить, что есть блок "Сила в людях"
    5. Перейти в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
    6. Находим раздел Работаем и проверяем, что у всех фотографии хронологии
       одинаковые высота (height) и ширина (width)

"""
from pages.sbis_main_page import SbisMainPage
    

def test_scenario_one(browser):
    sbis_main_page = SbisMainPage(browser)
    sbis_contact_page = sbis_main_page.go_to_contacts() #открыли окно Контакты
    sbis_contact_page = sbis_main_page.get_to_contacts() #перешли в окно Контакты
    tensor_mane_page = sbis_contact_page.go_to_banner()  #найти баннер тензор и перейти на https://tensor.ru/
    tensor_mane_page.url_is_correct() #проверить, что юрл https://tensor.ru/
    tensor_mane_page.block_is() #проверить, что есть блок "Сила в людях"
    tensor_about_page = tensor_mane_page.go_to_about_tensor() #перейти на https://tensor.ru/about
    tensor_about_page.url_is_correct() #проверить, что юрл https://tensor.ru/about
    tensor_about_page.correct_photos() #проверить размеры фото в разделе "Работаем"
