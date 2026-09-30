# pages/SystemLogSettingsPage.py
from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage


class SystemLogSettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 SystemLogSettingsPage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        SYSTEM_MENU_LOCATOR = (By.CSS_SELECTOR, ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        SYSTEM_LOG_SETTINGS_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(23) > li > div > span:nth-child(4)")
        SYSTEM_LOG_GLOBAL_SETTINGS_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(23) > li > ul > div > a > li > span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SYSTEM_LOG_SETTINGS_MENU_LOCATOR).click()
        self.find_element_if_present(SYSTEM_LOG_GLOBAL_SETTINGS_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)

    def get_system_log_global_settings_tier2_header_text(self):
        SYSTEM_LOG_GLOBAL_SETTINGS_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(SYSTEM_LOG_GLOBAL_SETTINGS_TIER2_HEADER_LOCATOR)

    def get_system_log_global_settings_title_text(self):
        SYSTEM_LOG_GLOBAL_SETTINGS_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        return self.find_element_then_get_text(SYSTEM_LOG_GLOBAL_SETTINGS_TITLE_LOCATOR)

    def get_system_log_global_settings_option_one_text(self):
        SYSTEM_LOG_GLOBAL_SETTINGS_OPTION_ONE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span > label")
        return self.find_element_then_get_text(SYSTEM_LOG_GLOBAL_SETTINGS_OPTION_ONE_LOCATOR)

    def get_system_log_global_settings_option_two_text(self):
        SYSTEM_LOG_GLOBAL_SETTINGS_OPTION_TWO_LOCATOR = (
            By.CSS_SELECTOR,
            "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span:nth-child(2) > label",
        )
        return self.find_element_then_get_text(SYSTEM_LOG_GLOBAL_SETTINGS_OPTION_TWO_LOCATOR)

    def get_checked_system_log_global_settings_option(self):
        system_log_global_settings_option_div = (
            By.CSS_SELECTOR,
            "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div",
        )
        target_div = self.find_element_if_present(system_log_global_settings_option_div)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)
        return text

    def get_system_log_global_settings_button_text(self):
        SYSTEM_LOG_GLOBAL_SETTINGS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#Apply1")
        return self.find_input_value(SYSTEM_LOG_GLOBAL_SETTINGS_BUTTON_LOCATOR)

    def get_system_log_save_mode_settings_header_text(self):
        SYSTEM_LOG_SAVE_MODE_SETTINGS_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > legend")
        return self.find_element_then_get_text(SYSTEM_LOG_SAVE_MODE_SETTINGS_HEADER_LOCATOR)

    def get_save_mode_title_and_value(self):
        SAVE_MODE_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td > span")
        SAVE_MODE_VALUE_LOCATOR = (By.CSS_SELECTOR, "#SaveMode")
        SAVE_MODE_VALUE_LOCATOR_2 = (By.CSS_SELECTOR, "#Minutes")
        title = self.find_element_then_get_text(SAVE_MODE_TITLE_LOCATOR)
        value1 = self.find_selected_value_within(SAVE_MODE_VALUE_LOCATOR)
        value2 = self.find_input_value(SAVE_MODE_VALUE_LOCATOR_2)
        return title, value1, value2

    def get_save_mode_button_text(self):
        SAVE_MODE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#Apply2")
        return self.find_input_value(SAVE_MODE_BUTTON_LOCATOR)
