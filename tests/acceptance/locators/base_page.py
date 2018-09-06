from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'h1'  # the same thing as initiating a tuple
    NAV_LINKS = By.CLASS_NAME, 'nav-link'
