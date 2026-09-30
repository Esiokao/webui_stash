# tests/test_1_login.py

from datetime import datetime

import allure
import pytest


@allure.title("Login")
class TestLogin:
    def test_open_page(self, login_page):
        result = login_page.open()

        assert "DGS" in result, "Login Error"

    def test_switch_to_main_frame(self, login_page):
        result = login_page.switch_to_main_frame()

        assert result, "failed to switch to main frame"

    def test_valid_login(self, login_page):
        result = login_page.login("admin", "admin")

        assert result, "failed to login"

    def test_login_check(self, login_page):
        result = login_page.is_login_successful()

        assert result, "failed to check login information"
