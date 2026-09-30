# pages/MACNotificationSettingsPage.py
from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage


class MACNotificationSettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 MACNotificationSettingsPage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        system_menu_locator = (By.CSS_SELECTOR, ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        MAC_NOTIFICATION_SETTINGS_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(20) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(MAC_NOTIFICATION_SETTINGS_menu_locator).click()

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)

    def get_mac_notification_settings_tier2_header_text(self):
        get_mac_notification_settings_tier2_header_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(get_mac_notification_settings_tier2_header_locator)

    def get_state_title_text(self):
        state_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")

        return self.find_element_then_get_text(state_title_locator)

    def get_state_option_one_text(self):
        state_option_one_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span > label")

        return self.find_element_then_get_text(state_option_one_locator)

    def get_state_option_two_text(self):
        state_option_two_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span:nth-child(2) > label")

        return self.find_element_then_get_text(state_option_two_locator)

    def get_checked_state_option(self):
        checked_state_option_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(1) > td:nth-child(2) > div")
        target_div = self.find_element_if_present(checked_state_option_locator)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)
        return text

    def get_interval_title_and_value(self):
        interval_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        interval_value_locator = (By.CSS_SELECTOR, "#Interval")

        title = self.find_element_then_get_text(interval_title_locator)
        value = self.find_input_value(interval_value_locator)

        return title, value

    def get_history_size_title_and_value(self):
        history_size_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")
        history_size_value_locator = (By.CSS_SELECTOR, "#HistorySize")

        title = self.find_element_then_get_text(history_size_title_locator)
        value = self.find_input_value(history_size_value_locator)

        return title, value

    def get_mac_notification_global_settings_button_text(self):
        mac_notification_global_settings_button_locator = (By.CSS_SELECTOR, "#Apply1")

        return self.find_input_value(mac_notification_global_settings_button_locator)

    def get_MAC_Notification_Port_Settings_Table_header_text(self):
        MAC_Notification_Port_Settings_Table_header_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > legend")

        return self.find_element_then_get_text(MAC_Notification_Port_Settings_Table_header_locator)

    def get_from_port_title_and_value(self):
        from_port_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td")
        from_port_value_locator = (By.CSS_SELECTOR, "#fromPort")

        title = self.find_element_then_get_text(from_port_title_locator)
        value = self.find_selected_value_within(from_port_value_locator)

        return title, value

    def get_to_port_title_and_value(self):
        to_port_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td:nth-child(2)")
        to_port_value_locator = (By.CSS_SELECTOR, "#ToPort")

        title = self.find_element_then_get_text(to_port_title_locator)
        value = self.find_selected_value_within(to_port_value_locator)

        return title, value

    def get_state_title_and_value(self):
        state_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td:nth-child(3)")
        state_value_locator = (By.CSS_SELECTOR, "#State")

        title = self.find_element_then_get_text(state_title_locator)
        value = self.find_selected_value_within(state_value_locator)

        return title, value

    def get_MAC_Notification_Port_Settings_Table_button_text(self):
        MAC_Notification_Port_Settings_Table_button_locator = (By.CSS_SELECTOR, "#Apply2")

        return self.find_input_value(MAC_Notification_Port_Settings_Table_button_locator)

    def get_MAC_Notification_Port_State_Table_header_text(self):
        MAC_Notification_Port_State_Table_header_locator = (By.CSS_SELECTOR, "div:nth-child(4) > fieldset > legend")

        return self.find_element_then_get_text(MAC_Notification_Port_State_Table_header_locator)

    def get_MAC_Notification_Port_State_table_title(self):
        MAC_Notification_Port_State_table_title_locator = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"

        return self.find_cells_value_within(MAC_Notification_Port_State_table_title_locator, cells_class_name)

    def get_MAC_Notification_Port_State_table_value(self):
        MAC_Notification_Port_State_table_value_locator = (By.CSS_SELECTOR, ".el-table__row")
        cells_class_name = "cell"

        return self.find_cells_value_within(MAC_Notification_Port_State_table_value_locator, cells_class_name)
