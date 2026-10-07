# test_11_dhcp_auto_Image.py


import allure


@allure.title("dhcp_auto_Image")
class TestDHCPAutoImage:
    def test_check_header(self, dhcp_auto_image_page):
        result = dhcp_auto_image_page.get_page_header_text()
        expected_val = "DHCP Auto Image"

        assert expected_val == result

    def test_check_dhcp_auto_image_tier2_header(self, dhcp_auto_image_page):
        result = dhcp_auto_image_page.get_dhcp_auto_image_tier2_header_text()
        expected_val = "DHCP Auto Image"

        assert expected_val == result

    def test_check_auto_image_title(self, dhcp_auto_image_page):
        result = dhcp_auto_image_page.get_auto_image_title_text()
        expected_val = "DHCP Auto Image"

        assert expected_val == result

    def test_check_dhcp_auto_image_option_one_text(self, dhcp_auto_image_page):
        result = dhcp_auto_image_page.get_auto_image_option_one_text()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_dhcp_auto_image_option_two_text(self, dhcp_auto_image_page):
        result = dhcp_auto_image_page.get_auto_image_option_two_text()
        expected_val = "Disabled"

        assert expected_val == result

    def test_default_auto_image_mode_is_disabled(self, dhcp_auto_image_page):
        opt = dhcp_auto_image_page.get_checked_auto_image_mode_option()
        expected_val = "Disabled"

        assert opt == expected_val, "default auto image mode is not Disabled"

    def test_check_Timeout_title_and_value(self, dhcp_auto_image_page):
        title, value = dhcp_auto_image_page.get_Timeout_title_and_value()
        expected_title = "Timeout (1-65535)"
        expected_val = "50"

        assert expected_title == title
        assert expected_val == value

    def test_check_dhcp_auto_image_button(self, dhcp_auto_image_page):
        result = dhcp_auto_image_page.get_dhcp_auto_image_button_value()
        expected_result = "Apply"

        assert expected_result == result
