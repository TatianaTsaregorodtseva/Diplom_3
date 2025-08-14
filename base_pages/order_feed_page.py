import allure

from api.api_methods import ApiMethods
from base_pages.base_page import BasePage
from data import Ingredient
from locators.basic_functionality_locators import Locators_functionality
from locators.order_feed_locators import Locators_feed
from locators.personal_account_locators import Locators_account
from locators.feed_locators import LocatorsFeed
from locators.basic_functionality_locators import LocatorsFunctionality
from selenium.webdriver.common.by import By
import urls


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажимаем на заказ, получаем открытое окно с заказом.')
    def press_order(self, locator, locator_next):
        self.wait_visibility_of_element(locator)
        element = self.find_element_on_page(locator)
        self.scroll(element)
        self.click_on_element(locator)
        self.wait_visibility_of_element(locator_next)

        return self.text_of_element(locator_next)

    @allure.step('Находим на странице заказ и нажимаем на него.')
    def order_in_feed(self, account, order_user, history):
        self.click_on_element(account)
        self.wait_visibility_of_element(history)
        self.click_on_element(history)
        self.wait_visibility_of_element(order_user)
        self.find_element_on_page(order_user)
        id_in_account = self.text_of_element(order_user)
        self.click_on_element(Locators_feed.order_feed)
        locator = (By.XPATH, f".//p[text()='{id_in_account}']")
        self.wait_visibility_of_element(locator)
        order_in_feed = self.find_element_on_page(locator)
        return order_in_feed

    @allure.step('Создаем заказ.')
    def order_user(self, dry, element_from, element_to, place, cook, email, password):
        self.login(email, password)
        self.drag_and_drop(dry, element_from, element_to)
        self.click_on_element(place)
        self.wait_visibility_of_element(cook)

        return self.text_of_element(cook)

    @allure.step('Авторизуемся.')
    def login(self, email, password):
        self.wait_visibility_of_element(Locators_account.personal_account)
        self.click_on_element(Locators_account.personal_account)
        self.wait_visibility_of_element(Locators_account.entrance)
        self.find_element_on_page(Locators_account.field_email).send_keys(email)
        self.find_element_on_page(Locators_account.field_password).send_keys(password)
        self.click_on_element(Locators_account.button_entrance)
        self.click_on_element(Locators_functionality.constructor)
        self.wait_visibility_of_element(Locators_account.personal_account)
        self.click_on_element(Locators_account.personal_account)

    @allure.step('Получаем значения счетчиков до и поле заказа.')
    def counter_orders(self, counter, mail, password):
        self.wait_visibility_of_element(counter)
        count = self.text_of_element(counter)
        ApiMethods.order_new(mail, password, Ingredient.ingredient)
        self.wait_visibility_of_element(counter)
        count_after = self.text_of_element(counter)

        return count_after > count

    @allure.step('Получаем номер нового заказа в разделе В работе.')
    def number_order(self, number, finaly):
        self.wait_visibility_of_element(number)
        number_order = self.text_of_element(number)
        final = self.text_of_element(finaly)
        number_order_final = str(number_order) + str(final)
        return number_order_final

    @allure.step("Перейти на страницу ленты заказов")
    def go_to_order_feed(self):
        self.get_url(urls.order_feed)

    @allure.step("Открыть карточку заказа")
    def open_order_card(self):
        self.click(LocatorsFeed.order_in_feed)
        return self.get_text(LocatorsFunctionality.card_order)

    @allure.step("Проверить видимость заказов пользователя")
    def check_user_orders_visibility(self):
        self.click(LocatorsFeed.personal_account)
        return self.is_element_visible(LocatorsFeed.order_in_account) and \
               self.is_element_visible(LocatorsFeed.history_orders)

    @allure.step("Проверить счетчик выполненных заказов за все время")
    def check_total_orders_counter(self, email, password):
        initial_count = self.get_text(LocatorsFeed.counter)
        # Логика создания заказа
        new_count = self.get_text(LocatorsFeed.counter)
        return int(new_count) > int(initial_count)

    @allure.step("Проверить счетчик выполненных заказов за сегодня")
    def check_today_orders_counter(self, email, password):
        initial_count = self.get_text(LocatorsFeed.counter_now)
        # Логика создания заказа
        new_count = self.get_text(LocatorsFeed.counter_now)
        return int(new_count) > int(initial_count)

    @allure.step("Получить номер заказа в работе")
    def get_order_number_in_progress(self):
        return self.get_text(LocatorsFeed.at_work).split()[-1]