# pages/PeripheralSettingsPage.py
from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage


class PeripheralSettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 PeripheralSettings
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        system_menu_locator = (By.CSS_SELECTOR, ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        Peripheral_SettingsPage_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(9) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(Peripheral_SettingsPage_menu_locator).click()

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)

    def get_fan_settings_tier2_header_text(self):
        fan_settings_tier2_header_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(fan_settings_tier2_header_locator)

    def get_fan_trap_title_text(self):
        fan_trap_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")

        return self.find_element_then_get_text(fan_trap_title_locator)

    def get_fan_trap_option_one_text(self):
        fan_trap_option_one_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span > label")

        return self.find_element_then_get_text(fan_trap_option_one_locator)

    def get_fan_trap_option_two_text(self):
        fan_trap_option_two_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span:nth-child(2) > label")

        return self.find_element_then_get_text(fan_trap_option_two_locator)

    def get_checked_fan_trap_option(self):
        fan_trap_option_div = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(1) > td:nth-child(2) > div")

        target_div = self.find_element_if_present(fan_trap_option_div)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)

        return text

    def get_fan_mode_title_and_value(self):
        fan_mode_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        fan_mode_value_locator = (By.CSS_SELECTOR, "#FanMode")

        title = self.find_element_then_get_text(fan_mode_title_locator)
        value = self.find_selected_value_within(fan_mode_value_locator)

        return title, value

    def get_fan_settings_button_value(self):
        fan_settings_button_locator = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table/tr[3]/td/input")

        return self.find_input_value(fan_settings_button_locator)

    def get_environment_temperature_settings_tier2_header_text(self):
        environment_temperature_settings_tier2_header_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > legend")

        return self.find_element_then_get_text(environment_temperature_settings_tier2_header_locator)

    def get_temperature_trap_title_text(self):
        temperature_trap_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td > span")

        return self.find_element_then_get_text(temperature_trap_title_locator)

    def get_temperature_trap_option_one_text(self):
        temperature_trap_option_one_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td:nth-child(2) > div > span > label")

        return self.find_element_then_get_text(temperature_trap_option_one_locator)

    def get_temperature_trap_option_two_text(self):
        temperature_trap_option_two_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td:nth-child(2) > div > span:nth-child(2) > label")

        return self.find_element_then_get_text(temperature_trap_option_two_locator)

    def get_checked_temperature_trap_option(self):
        temperature_trap_option_div = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr:nth-child(1) > td:nth-child(2) > div")

        target_div = self.find_element_if_present(temperature_trap_option_div)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)

        return text

    def get_high_threshold_title_and_value(self):
        high_threshold_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr:nth-child(2) > td")
        high_threshold_value_locator = (By.CSS_SELECTOR, "#environmentTempThresholdHigh")

        title = self.find_element_then_get_text(high_threshold_title_locator)
        value = self.find_input_value(high_threshold_value_locator)

        return title, value

    def get_high_threshold_option_text(self):
        high_threshold_option_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > div:nth-child(2)")

        return self.find_element_then_get_text(high_threshold_option_locator)

    def get_low_threshold_title_and_value(self):
        low_threshold_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr:nth-child(3) > td")
        low_threshold_value_locator = (By.CSS_SELECTOR, "#environmentTempThresholdLow")

        title = self.find_element_then_get_text(low_threshold_title_locator)
        value = self.find_input_value(low_threshold_value_locator)

        return title, value

    def get_low_threshold_option_text(self):
        low_threshold_option_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr:nth-child(3) > td:nth-child(2) > div:nth-child(2)")

        return self.find_element_then_get_text(low_threshold_option_locator)

    def get_environment_temperature_settings_button_value(self):
        environment_temperature_settings_button_locator = (By.XPATH, "/html/body/div/div/div/section/div/div/div[3]/fieldset/table/tr[3]/td[3]/input")

        return self.find_input_value(environment_temperature_settings_button_locator)
