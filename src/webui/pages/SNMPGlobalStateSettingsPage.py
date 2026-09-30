# pages/SNMPGlobalStateSettingsPage.py
from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class SNMPGlobalStateSettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 SNMPGlobalStateSettingsPage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        SYSTEM_MENU_LOCATOR = (
            By.CSS_SELECTOR,
            ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        SNMP_SETTINGS_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(11) > li > div > span:nth-child(4)")
        SNMP_GLOBAL_STATE_SETTINGS_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(11) > li > ul > div > a > li > span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_SETTINGS_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_GLOBAL_STATE_SETTINGS_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)
    
    def get_snmp_global_state_settings_tier2_header_text(self):
        SNMP_GLOBAL_STATE_SETTINGS_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(SNMP_GLOBAL_STATE_SETTINGS_TIER2_HEADER_LOCATOR)

    def get_snmp_global_state_settings_title_text(self):
        SNMP_GLOBAL_STATE_SETTINGS_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        return self.find_element_then_get_text(SNMP_GLOBAL_STATE_SETTINGS_TITLE_LOCATOR)

    def get_snmp_global_state_settings_option_one_text(self):
        SNMP_GLOBAL_STATE_SETTINGS_OPTION_ONE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span > label")
        return self.find_element_then_get_text(SNMP_GLOBAL_STATE_SETTINGS_OPTION_ONE_LOCATOR)

    def get_snmp_global_state_settings_option_two_text(self):
        SNMP_GLOBAL_STATE_SETTINGS_OPTION_TWO_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span:nth-child(2) > label")
        return self.find_element_then_get_text(SNMP_GLOBAL_STATE_SETTINGS_OPTION_TWO_LOCATOR)

    def get_checked_snmp_global_state_settings_option(self):
        snmp_global_state_settings_option_div = (By.CSS_SELECTOR, "div.sx-section > fieldset > table > tr > td:nth-child(2) > div")
        target_div = self.find_element_if_present(snmp_global_state_settings_option_div)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)
        return text

    def get_snmp_global_state_settings_button_text(self):
        SNMP_GLOBAL_STATE_SETTINGS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#Apply")
        return self.find_input_value(SNMP_GLOBAL_STATE_SETTINGS_BUTTON_LOCATOR)


