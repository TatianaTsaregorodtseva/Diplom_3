from selenium import webdriver


class WebdriverFactory:
    """Фабрика для создания WebDriver на основе переданного имени браузера."""

    @staticmethod
    def getWebdriver(browserName):
        """Метод создает и возвращает WebDriver для указанного браузера."""
        if browserName == "firefox":
            return webdriver.Firefox()
        elif browserName == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported browser: {browserName}")


def pytest_addoption(parser):
    """
    Добавляет аргумент командной строки '--browser' для выбора браузера.
    По умолчанию используется Chrome.
    """
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")
