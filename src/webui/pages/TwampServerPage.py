# pages/TwampServerPage.py
from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage


class TwampServerPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 TwampServerPage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        system_menu_locator = (By.CSS_SELECTOR, ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        TWAMP_SERVER_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(22) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(TWAMP_SERVER_menu_locator).click()

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)

    def get_twamp_server_tier2_header_text(self):
        get_twamp_server_tier2_header_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(get_twamp_server_tier2_header_locator)

    def get_state_title_and_value(self):
        state_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        state_value_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > select")
        title = self.find_element_then_get_text(state_title_locator)
        value = self.find_selected_value_within(state_value_locator)

        return title, value

    def get_protocol_title_and_value(self):
        protocol_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        protocol_value_locator = (By.CSS_SELECTOR, "#Protocol")
        title = self.find_element_then_get_text(protocol_title_locator)
        value = self.find_selected_value_within(protocol_value_locator)

        return title, value

    def get_age_time_title_and_value(self):
        age_time_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")
        age_time_value_locator = (By.CSS_SELECTOR, "#AgeTime")
        title = self.find_element_then_get_text(age_time_title_locator)
        value = self.find_input_value(age_time_value_locator)

        return title, value

    def get_auth_mode_title_and_value(self):
        auth_mode_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(3) > span")
        auth_mode_value_locator = (By.CSS_SELECTOR, "#AuthMode")
        title = self.find_element_then_get_text(auth_mode_title_locator)
        value = self.find_selected_value_within(auth_mode_value_locator)

        return title, value

    def get_minimum_udp_port_title_and_value(self):
        minimum_udp_port_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(3) > span")
        minimum_udp_port_value_locator = (By.CSS_SELECTOR, "#MinimumUDPPort")
        title = self.find_element_then_get_text(minimum_udp_port_title_locator)
        value = self.find_input_value(minimum_udp_port_value_locator)

        return title, value

    def get_twamp_server_button_text(self):
        twamp_server_button_locator = (By.CSS_SELECTOR, "#Apply")
        button_text = self.find_input_value(twamp_server_button_locator)

        return button_text

    def get_twamp_server_table_title(self):
        twamp_server_table_title_locator = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        title = self.find_cells_value_within(twamp_server_table_title_locator, cells_class_name)

        return title

    def get_table_default_is_empty(self):
        # span
        table_locator = (By.CSS_SELECTOR, ".table")
        expected_string = "< < Table is empty > >"

        return self.text_is_existed_within(table_locator, expected_string)

    def get_refresh_button_text(self):
        refresh_button_locator = (By.CSS_SELECTOR, "#Refresh")
        button_text = self.find_input_value(refresh_button_locator)

        return button_text
