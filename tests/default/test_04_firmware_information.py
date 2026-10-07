# tests/test4_firmware_information.py
import os

import allure


@allure.title("Firmware Information")
class TestFirmwareInformation:
    def test_collapse_system_menu_then_click_system_settings(self, firmware_information_page):
        res = firmware_information_page.init()
        assert res, "error while init firmware information"

    def test_check_firmware_information_table_title(self, firmware_information_page):
        title_cells = firmware_information_page.get_firmware_information_table_title()
        expected_titles = ["ID", "Version", "Size(B)", "Update Time", "From", "User"]

        assert expected_titles == title_cells

    def test_check_firmware_version_exists(self, firmware_information_page):
        result = firmware_information_page.get_firmware_version_exists()
        assert result == True, "global setting firmware version not exists"

    def test_check_select_prompt_text(self, firmware_information_page):
        select_prompt_text = firmware_information_page.find_selected_input_text()
        expected_text = "Please select the boot up image and config of device."

        assert expected_text == select_prompt_text

    def test_check_config_default_option(self, firmware_information_page):
        option = firmware_information_page.get_config_default_option()
        expected_option = "Config_id" + " " + os.getenv("BOOT_UP_CONFIG_ID")

        assert expected_option == option

    def test_check_firmware_default_option(self, firmware_information_page):
        option = firmware_information_page.get_firmware_default_option()
        expected_option = "Image_id" + " " + os.getenv("BOOT_UP_IMAGE_ID")

        assert expected_option == option

    def test_check_apply_btn_is_presented(self, firmware_information_page):
        apply_btn = firmware_information_page.get_apply_button_element()

        assert apply_btn

    def test_check_apply_btn_text(self, firmware_information_page):
        apply_btn_txt = firmware_information_page.get_apply_button_text()
        expected_val = "Apply"

        assert expected_val == apply_btn_txt

    def test_check_explain_row_1_title_and_description(self, firmware_information_page):
        title, desc = firmware_information_page.get_row_1_title_and_desc()
        expect_title = "'c'"
        expect_desc = ":Current boot up firmware"

        assert expect_title == title
        assert expect_desc == desc

    def test_check_explain_row_2_title_and_description(self, firmware_information_page):
        title, desc = firmware_information_page.get_row_2_title_and_desc()
        expect_title = "'*'"
        expect_desc = ":Boot up firmware"

        assert expect_title == title
        assert expect_desc == desc

    def test_check_explain_row_3_title_and_description(self, firmware_information_page):
        title, desc = firmware_information_page.get_row_3_title_and_desc()
        expect_title = "(SSH)"
        expect_desc = ":Firmware update through SSH"

        assert expect_title == title
        assert expect_desc == desc

    def test_check_explain_row_4_title_and_description(self, firmware_information_page):
        title, desc = firmware_information_page.get_row_4_title_and_desc()
        expect_title = "(Web)"
        expect_desc = ":Firmware update through Web"

        assert expect_title == title
        assert expect_desc == desc

    def test_check_explain_row_5_title_and_description(self, firmware_information_page):
        title, desc = firmware_information_page.get_row_5_title_and_desc()
        expect_title = "(SNMP)"
        expect_desc = ":Firmware update through SNMP"

        assert expect_title == title
        assert expect_desc == desc

    def test_check_explain_row_6_title_and_description(self, firmware_information_page):
        title, desc = firmware_information_page.get_row_6_title_and_desc()
        expect_title = "(Telnet)"
        expect_desc = ":Firmware update through Telnet"

        assert expect_title == title
        assert expect_desc == desc

    def test_check_explain_row_7_title_and_description(self, firmware_information_page):
        title, desc = firmware_information_page.get_row_7_title_and_desc()
        expect_title = "(CONSOLE)"
        expect_desc = ":Firmware update through CONSOLE"

        assert expect_title == title
        assert expect_desc == desc
