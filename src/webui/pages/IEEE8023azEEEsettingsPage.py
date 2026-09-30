# pages/IEEE8023azEEEsettingsPage.py
from selenium.webdriver.common.by import By
import re

from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class IEEE8023azEEEsettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 IEEE802.3azEEEsettingsPage
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
        IEEE802_3az_EEE_settings_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(26) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(IEEE802_3az_EEE_settings_menu_locator).click()

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)

    def get_ieee802_3az_eee_settings_header_text(self):
        get_ieee802_3az_eee_settings_header_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(get_ieee802_3az_eee_settings_header_locator)
    
    def get_from_port_title_and_value(self):
        get_from_port_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td")
        get_from_port_value_locator = (By.CSS_SELECTOR, "#fromPort")

        title = self.find_element_then_get_text(get_from_port_title_locator)
        value = self.find_selected_value_within(get_from_port_value_locator)

        return title, value
    
    def get_to_port_title_and_value(self):
        get_to_port_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2)")
        get_to_port_value_locator = (By.CSS_SELECTOR, "#ToPort")

        title = self.find_element_then_get_text(get_to_port_title_locator)
        value = self.find_selected_value_within(get_to_port_value_locator)

        return title, value
    
    def get_state_title_and_value(self):
        get_state_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(3)")
        get_state_value_locator = (By.CSS_SELECTOR, "#State")

        title = self.find_element_then_get_text(get_state_title_locator)
        value = self.find_selected_value_within(get_state_value_locator)

        return title, value
    
    def get_button_text(self):
        get_button_locator = (By.CSS_SELECTOR, "#Apply")

        return self.find_input_value(get_button_locator)
    
    def get_title_table(self):
        title_table_locator = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(title_table_locator, cells_class_name)
    
    def get_port1_table_value(self):
        port1_table_value_locator = (By.CSS_SELECTOR, ".el-table__row")
        cells_class_name = "cell"
        return self.find_cells_value_within(port1_table_value_locator, cells_class_name)
        
        
        