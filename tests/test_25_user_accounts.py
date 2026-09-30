# test_25_user_accounts.py

import allure
import pytest
import asyncio
import os
from webui.utils.all_exist_in_order import all_exist_in_order


@allure.title("user_accounts")
class TestUserAccounts:

    def test_check_header(self, user_accounts_page):
        result = user_accounts_page.get_page_header_text()
        expected_val = "User Accounts"

        assert expected_val == result

    def test_check_user_accounts_tier2_header(self, user_accounts_page):
        result = user_accounts_page.get_user_accounts_tier2_header_text()
        expected_val = "Add User Accounts"

        assert expected_val == result

    def test_check_user_name_title_and_value(self, user_accounts_page):
        title, value = user_accounts_page.get_user_name_title_and_value()
        expected_title = "User Name"
        expected_value = ""

        assert expected_title == title
        assert expected_value == value

    def test_check_access_right_title_and_value(self, user_accounts_page):
        title, value = user_accounts_page.get_access_right_title_and_value()
        expected_title = "Access Right"
        expected_value = "Admin"

        assert expected_title == title
        assert expected_value == value

    def test_check_password_title_and_value(self, user_accounts_page):
        title, value = user_accounts_page.get_password_title_and_value()
        expected_title = "Password"
        expected_value = ""

        assert expected_title == title
        assert expected_value == value

    def test_check_confirm_password_title_and_value(self, user_accounts_page):
        title, value = user_accounts_page.get_confirm_password_title_and_value()
        expected_title = "Confirm Password"
        expected_value = ""

        assert expected_title == title
        assert expected_value == value

    def test_check_note_text(self, user_accounts_page):
        value1, value2, value3 = user_accounts_page.get_note_text()
        expected_val1 = "Note:"
        expected_val2 = "User Name should be less than 32 characters."
        expected_val3 = "Password should be less than 30 characters."

        assert expected_val1 == value1
        assert expected_val2 == value2
        assert expected_val3 == value3

    def test_check_add_user_accounts_apply_button_text(self, user_accounts_page):
        result = user_accounts_page.get_add_user_accounts_apply_button_text()
        expected_val = "Apply"

        assert expected_val == result

    def test_check_total_entries_title(self, user_accounts_page):
        result = user_accounts_page.get_total_entries_title()
        expected_val = "Total Entries : 0"

        assert expected_val == result

    def test_check_table_title(self, user_accounts_page):
        result = user_accounts_page.get_table_title()
        expected_val = ["User Name", "Access Right", "Password"]

        assert expected_val == result

    def test_check_table_default_is_empty(self, user_accounts_page):
        result = user_accounts_page.get_table_default_is_empty()

        assert result
