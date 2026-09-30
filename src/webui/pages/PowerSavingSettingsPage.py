# pages/PowerSavingSettingsPage.py
from selenium.webdriver.common.by import By
import re

from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class PowerSavingSettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 PowerSavingSettingsPage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        system_menu_locator = (
            By.CSS_SELECTOR,
            ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        POWER_SAVING_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(25) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(POWER_SAVING_menu_locator).click()

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)

    def get_global_settings_tier2_header_text(self):
        get_global_settings_tier2_header_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(get_global_settings_tier2_header_locator)
    
    def get_function_version_title_and_value(self):
        get_function_version_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        get_function_version_value_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > span")

        title = self.find_element_then_get_text(get_function_version_title_locator)
        value = self.find_element_then_get_text(get_function_version_value_locator)

        return title, value
    
    def get_link_status_detection_version_title(self):
        get_link_status_detection_version_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        
        return self.find_element_then_get_text(get_link_status_detection_version_title_locator)
    
    def get_link_status_detection_version_option_one_text(self):
        get_link_status_detection_version_option_one_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > div > span > label")

        return self.find_element_then_get_text(get_link_status_detection_version_option_one_locator)
    
    def get_link_status_detection_version_option_two_text(self):
        get_link_status_detection_version_option_two_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > div > span:nth-child(2) > label")

        return self.find_element_then_get_text(get_link_status_detection_version_option_two_locator)

    def get_checked_link_status_detection_version_option(self):
        link_status_detection_version_option_div = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > div")
        target_div = self.find_element_if_present(link_status_detection_version_option_div)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)
        return text

    def get_Global_Settings_button_text(self):
        Global_Settings_button_locator = (By.CSS_SELECTOR, "#onApply1")
        
        return self.find_input_value(Global_Settings_button_locator)

    def get_advanced_power_saving_settings_title(self):
        get_advanced_power_saving_settings_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > legend")

        return self.find_element_then_get_text(get_advanced_power_saving_settings_title_locator)

    def get_type_title_and_value(self):
        get_type_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td > span")
        get_type_value_locator = (By.CSS_SELECTOR, "#Type")

        title = self.find_element_then_get_text(get_type_title_locator)
        value = self.find_selected_value_within(get_type_value_locator)

        return title, value

    def get_time_profile_1_title_and_value(self):
        get_time_profile_1_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr:nth-child(2) > td > span")
        get_time_profile_1_value_locator = (By.CSS_SELECTOR, "#TimeProfile1")

        title = self.find_element_then_get_text(get_time_profile_1_title_locator)
        value = self.find_selected_value_within(get_time_profile_1_value_locator)

        return title, value

    def get_state_title_and_value(self):
        get_state_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td:nth-child(3) > span")
        get_state_value_locator = (By.CSS_SELECTOR, "#State")

        title = self.find_element_then_get_text(get_state_title_locator)
        value = self.find_selected_value_within(get_state_value_locator)

        return title, value

    def get_time_profile_2_title_and_value(self):
        get_time_profile_2_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr:nth-child(2) > td:nth-child(3) > span")
        get_time_profile_2_value_locator = (By.CSS_SELECTOR, "#TimeProfile2")

        title = self.find_element_then_get_text(get_time_profile_2_title_locator)
        value = self.find_selected_value_within(get_time_profile_2_value_locator)

        return title, value

    def get_select_all_button_text(self):
        get_select_all_button_locator = (By.CSS_SELECTOR, "#SelectAll")

        return self.find_input_value(get_select_all_button_locator)

    def get_clear_button_text(self):
        get_clear_button_locator = (By.CSS_SELECTOR, "#Clear")

        return self.find_input_value(get_clear_button_locator)

    def get_apply_button_text(self):
        get_apply_button_locator = (By.CSS_SELECTOR, "#Apply2")

        return self.find_input_value(get_apply_button_locator)

    def get_advanced_power_saving_settings_port_num_title(self):
        locator = (By.XPATH, "/html/body/div[1]/div/div/section/div/div/div[3]/fieldset/div/div/table/tbody")
        checked_numbers = self.find_unchecked_checkboxes_text(locator, self.get_head_span_text)
        return checked_numbers

    def get_summary_header_text(self):
        get_summary_header_locator = (By.CSS_SELECTOR, "div:nth-child(4) > fieldset > legend")

        return self.find_element_then_get_text(get_summary_header_locator)

    def get_table_title(self):
        table_title_locator = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(table_title_locator, cells_class_name)

    def get_led_shut_off_table_value(self):
        led_shut_off_table_value_locator = (By.CSS_SELECTOR, "div:nth-child(4) > fieldset > div > div > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1)")
        cells_class_name = "cell"
        return self.find_cells_value_within(led_shut_off_table_value_locator, cells_class_name)

    def get_port_shut_off_table_value(self):
        port_shut_off_table_value_locator = (By.CSS_SELECTOR, "div:nth-child(4) > fieldset > div > div > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr.el-table__row.el-table__row--striped")
        cells_class_name = "cell"
        return self.find_cells_value_within(port_shut_off_table_value_locator, cells_class_name)
    
    def get_system_hibernation_table_value(self):
        system_hibernation_table_value_locator = (By.CSS_SELECTOR, "div:nth-child(4) > fieldset > div > div > div.el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(3)")
        cells_class_name = "cell"
        return self.find_cells_value_within(system_hibernation_table_value_locator, cells_class_name)
    
    

    



