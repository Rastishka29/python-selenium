from selenium.webdriver.common.by import By


class NewPostPageLocators:
    NEW_POST_FORM = By.ID, 'post-form'
    TITLE_FIELD = By.ID, 'title'
    CONTENT_FIELD = By.ID, 'content'
    SUBMIT_BTN = By.ID, 'create-post'
