from selenium.webdriver.common.by import By


class OrderListLocators:
    ORDER_LIST = (By.XPATH, '//h1[text()="Лента заказов"]')
    FIRST_ORDER_FROM_LIST = (By.XPATH, '//ul/li[1][contains(@class, "OrderHistory") and contains(@class, "listItem")]')