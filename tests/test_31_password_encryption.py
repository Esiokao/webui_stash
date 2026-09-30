# test_31_password_encryption.py


import allure


@allure.title("Password_Encryption")
class TestPasswordEncryption:
    def test_check_header(self, password_encryption_page):
        result = password_encryption_page.get_page_header_text()
        expected_val = "Password Encryption"

        assert expected_val == result

    def test_check_password_encryption_tier2_header(self, password_encryption_page):
        result = password_encryption_page.get_password_encryption_tier2_header_text()
        expected_val = "Password Encryption Settings"

        assert expected_val == result

    def test_check_password_encryption_title(self, password_encryption_page):
        result = password_encryption_page.get_password_encryption_title_text()
        expected_val = "Password Encryption State:"

        assert expected_val == result

    def test_check_password_encryption_option_one_text(self, password_encryption_page):
        result = password_encryption_page.get_password_encryption_option_one_text()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_password_encryption_option_two_text(self, password_encryption_page):
        result = password_encryption_page.get_password_encryption_option_two_text()
        expected_val = "Disabled"

        assert expected_val == result

    def test_default_password_encryption_is_disabled(self, password_encryption_page):
        opt = password_encryption_page.get_checked_password_encryption_option()
        expected_val = "Disabled"

        assert opt == expected_val, "default password encryption is not Disabled"

    def test_check_password_encryption_apply_button_text(self, password_encryption_page):
        result = password_encryption_page.get_password_encryption_apply_button_text()
        expected_val = "Apply"

        assert expected_val == result
