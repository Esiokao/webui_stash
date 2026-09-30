# pages/PortSettingsPage.py
from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class PortSettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 PortSettingsPage
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
        SERIAL_Port_Configuration_MENU_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > div > div > div > div > ul > div:nth-child(2) > li > ul > div:nth-child(10) > li > div > span:nth-child(4)")
        SERIAL_PORT_SETTINGS_MENU_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > div > div > div > div > ul > div:nth-child(2) > li > ul > div:nth-child(10) > li > ul > div > a > li > span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SERIAL_Port_Configuration_MENU_LOCATOR).click()
        self.find_element_if_present(SERIAL_PORT_SETTINGS_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)
    
    def get_port_settings_tier2_header_text(self):
        PORT_SETTINGS_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(PORT_SETTINGS_TIER2_HEADER_LOCATOR)
    
    def get_from_port_title_and_value(self):
        FROM_PORT_TITLE_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr > td")
        FROM_PORT_VALUE_LOCATOR = (By.CSS_SELECTOR, "#fromPort")
        title = self.find_element_then_get_text(FROM_PORT_TITLE_LOCATOR)
        value = self.find_selected_value_within(FROM_PORT_VALUE_LOCATOR)
        return title, value
    
    def get_to_port_title_and_value(self):
        TO_PORT_TITLE_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr > td:nth-child(2)")
        TO_PORT_VALUE_LOCATOR = (By.CSS_SELECTOR, "#toPort")
        title = self.find_element_then_get_text(TO_PORT_TITLE_LOCATOR)
        value = self.find_selected_value_within(TO_PORT_VALUE_LOCATOR)
        return title, value
    
    def get_media_title_and_value(self):
        MEDIA_TITLE_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr > td:nth-child(3)")
        MEDIA_VALUE_LOCATOR = (By.CSS_SELECTOR, "#media")
        title = self.find_element_then_get_text(MEDIA_TITLE_LOCATOR)
        value = self.find_selected_value_within(MEDIA_VALUE_LOCATOR)
        return title, value
    
    def get_state_title_and_value(self):
        STATE_TITLE_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr > td:nth-child(4)")
        STATE_VALUE_LOCATOR = (By.CSS_SELECTOR, "#state")
        title = self.find_element_then_get_text(STATE_TITLE_LOCATOR)
        value = self.find_selected_value_within(STATE_VALUE_LOCATOR)
        return title, value
    
    def get_speed_title_and_value(self):
        SPEED_TITLE_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr > td:nth-child(5)")
        SPEED_VALUE_LOCATOR = (By.CSS_SELECTOR, "#speed")
        title = self.find_element_then_get_text(SPEED_TITLE_LOCATOR)
        value = self.find_selected_value_within(SPEED_VALUE_LOCATOR)
        return title, value
    
    def get_mdi_mdix_title_and_value(self):
        MDI_MDIX_TITLE_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr > td:nth-child(6)")
        MDI_MDIX_VALUE_LOCATOR = (By.CSS_SELECTOR, "#MDI_MDIX")
        title = self.find_element_then_get_text(MDI_MDIX_TITLE_LOCATOR)
        value = self.find_selected_value_within(MDI_MDIX_VALUE_LOCATOR)
        return title, value
    
    def get_flow_control_title_and_value(self):
        FLOW_CONTROL_TITLE_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr > td:nth-child(7)")
        FLOW_CONTROL_VALUE_LOCATOR = (By.CSS_SELECTOR, "#flowControl")
        title = self.find_element_then_get_text(FLOW_CONTROL_TITLE_LOCATOR)
        value = self.find_selected_value_within(FLOW_CONTROL_VALUE_LOCATOR)
        return title, value
    
    def get_auto_downgrade_title_and_value(self):
        AUTO_DOWNGRADE_TITLE_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr > td:nth-child(8)")
        AUTO_DOWNGRADE_VALUE_LOCATOR = (By.CSS_SELECTOR, "#AutoDowngrade")
        title = self.find_element_then_get_text(AUTO_DOWNGRADE_TITLE_LOCATOR)
        value = self.find_selected_value_within(AUTO_DOWNGRADE_VALUE_LOCATOR)
        return title, value
    
    def get_10_half_text(self):
        TEN_HALF_TEXT_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")
        return self.find_element_then_get_text(TEN_HALF_TEXT_LOCATOR)
    
    def get_10_full_text(self):
        TEN_FULL_TEXT_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span:nth-child(2)")
        return self.find_element_then_get_text(TEN_FULL_TEXT_LOCATOR)
    
    def get_100_half_text(self):
        ONE_HUNDRED_HALF_TEXT_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span:nth-child(3)")
        return self.find_element_then_get_text(ONE_HUNDRED_HALF_TEXT_LOCATOR)

    def get_100_full_text(self):
        ONE_HUNDRED_FULL_TEXT_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span:nth-child(4)")
        return self.find_element_then_get_text(ONE_HUNDRED_FULL_TEXT_LOCATOR)
    
    def get_1000_full_text(self):
        ONE_THOUSAND_FULL_TEXT_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span:nth-child(5)")
        return self.find_element_then_get_text(ONE_THOUSAND_FULL_TEXT_LOCATOR)
    
    def get_table_title(self):
        table_title_locator = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(table_title_locator, cells_class_name)

    def get_table_value(self):
        table_value_locator = (By.CSS_SELECTOR, ".el-table__row")
        cells_class_name = "cell"
        return self.find_cells_value_within(table_value_locator, cells_class_name)

    def get_port_speed_checkbox_value(self):
        port_speed_checkbox_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div.sx-section > fieldset > table > tr:nth-child(3) > td:nth-child(1)")
        return self.find_checked_checkboxes_text(port_speed_checkbox_locator, self.get_sibling_text)

    def get_port_settings_button1_value(self):
        port_settings_button1_locator = (By.CSS_SELECTOR,
                         "#Apply")
        return self.find_input_value(port_settings_button1_locator)
    
    def get_port_settings_button2_value(self):
        port_settings_button2_locator = (By.CSS_SELECTOR,
                         "#Refresh")
        return self.find_input_value(port_settings_button2_locator)
    

