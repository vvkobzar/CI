import pytest
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login_page(self, creds):
        login, password = creds
        self.is_element_present(
            LoginPageLocators.EMAIL_FIELD).send_keys(login)
        self.is_element_present(
            LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.is_element_present(LoginPageLocators.SING_IN_BUTTON).click()

    def get_message_error(self):
        message_error = self.is_element_present(
            LoginPageLocators.MESSAGE_ERROR_FIELD).text
        assert message_error == "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."