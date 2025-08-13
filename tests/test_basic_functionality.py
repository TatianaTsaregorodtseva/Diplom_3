import allure
from base_pages.basic_functionality_page import FunctionalityPage
import urls


class TestFunctionality:

    @allure.title('Нажимаем кнопку Конструктор.')  # декораторы
    @allure.description('На странице ищем кнопку, нажимаем, переходим на главную страницу с Конструктором, получаем текущий урл, сравниваем текущий урл с урл главной страницы.')
    def test_press_button_constructor(self, browser):
        page = FunctionalityPage(browser)
        page.go_to_login_page()
        current_url = page.click_constructor_button()

        assert current_url == urls.main_page

    @allure.title('Нажимаем кнопку Лента заказов.')  # декораторы
    @allure.description(
        'На странице ищем кнопку, нажимаем, переходим на страницу с заказами, получаем текущий урл, сравниваем текущий урл с урл Ленты заказов.')
    def test_press_button_order_feed(self, browser):
        page = FunctionalityPage(browser)
        page.go_to_main_page()
        current_url = page.click_order_feed_button()

        assert current_url == urls.order_feed

    @allure.title('Получаем карточку ингредиента.')  # декораторы
    @allure.description(
        'На странице ищем заказ, нажимаем, открывается карточка заказа, в карточке ищем слово Состав.')
    def test_press_button_ingredient(self, browser):
        page = FunctionalityPage(browser)
        page.go_to_main_page()
        card_title = page.open_ingredient_card()

        assert card_title == "Детали ингредиента"

    @allure.title('Закрываем карточку ингредиента.')  # декораторы
    @allure.description(
        'На странице ищем заказ, нажимаем, открывается карточка заказа, нажимаем на крестик, карточка заказа закрывается.')
    def test_press_exit_order(self, browser):
        page = FunctionalityPage(browser)
        page.go_to_main_page()

        assert page.close_ingredient_card()

    @allure.title('Перетаскиваем ингредиент, получаем увеличение каунтера.')  # декораторы
    @allure.description(
        'Запоминаем первоначальное число каунтера ингредиента, перетаскиваем ингредиент, получаем новое значение каунтера, проверяем, что каунтер увеличился.')
    def test_count(self, browser):
        page = FunctionalityPage(browser)
        page.go_to_main_page()

        assert page.drag_ingredient_to_basket()

    @allure.step('Проверяем возможность создания заказа авторизованным пользователем, заказ с ингредиентами.')
    def test_order_user(self, register, browser):
        page = FunctionalityPage(browser)
        page.go_to_main_page()
        order_status = page.create_order(register[0], register[1])

        assert order_status == 'Ваш заказ начали готовить'

