# pages/IPv6SystemSettings.py
from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class IPv6SystemSettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 IPv6SystemSettings
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
        firmware_information_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(5) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(firmware_information_menu_locator).click()

    def get_page_header_text(self):
        header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(header_locator)

    def get_v6_settings_tier2_header_text(self):
        v6_settings_tier2_header_locator = (
            By.CSS_SELECTOR, "#app > div > div > section > div > div > div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(v6_settings_tier2_header_locator)

    def get_interface_name_title_and_value(self):
        #  span
        title_locator = (By.CSS_SELECTOR,
                         "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr > td > span")
        value_locator = (By.CSS_SELECTOR,
                         "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > span")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_element_then_get_text(value_locator)

        return title, value

    def get_ipv6_state_title_and_value(self):
        # select box
        title_locator = (By.CSS_SELECTOR,
                         "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr > td:nth-child(3) > span")
        value_locator = (By.CSS_SELECTOR, "#IPv6State")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_selected_value_within(value_locator)

        return title, value

    def get_interface_admin_state_title_and_value(self):
        # span
        title_locator = (By.CSS_SELECTOR,
                         "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        value_locator = (By.CSS_SELECTOR,
                         "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(2) > span")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_element_then_get_text(value_locator)

        return title, value

    def get_v6_network_address_title_and_value(self):
        # input
        title_locator = (By.CSS_SELECTOR,
                         "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(3) > span")
        value_locator = (By.CSS_SELECTOR, "#IPv6NetworkAddress > input")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_input_value(value_locator)

        return title, value

    def get_dhcp_v6_client_title_and_value(self):
        # select box
        title_locator = (By.CSS_SELECTOR,
                         "#app > div > div > section > div > div > div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")
        value_locator = (By.CSS_SELECTOR, "#DHCPv6Client")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_selected_value_within(value_locator)

        return title, value

    # NSRetransmitTimeSettings

    def get_ns_retransmit_time_header_text(self):
        # input
        header_locator = (
            By.CSS_SELECTOR, "#app > div > div > section > div > div > div:nth-child(3) > fieldset > legend")

        return self.find_element_then_get_text(header_locator)

    def get_ns_retransmit_time_title_and_value(self):
        # input
        title_locator = (By.CSS_SELECTOR,
                         "#app > div > div > section > div > div > div:nth-child(3) > fieldset > table > tr > td > span")
        value_locator = (By.CSS_SELECTOR, "#NSRetransmitTime")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_input_value(value_locator)

        return title, value

    # Automatic Link Local State Settings
    def get_automatic_link_local_state_header_text(self):
        # span
        header_locator = (
            By.CSS_SELECTOR, "#app > div > div > section > div > div > div:nth-child(4) > fieldset > legend")

        return self.find_element_then_get_text(header_locator)

    def get_automatic_link_local_state_title_and_value(self):
        # select box
        title_locator = (By.CSS_SELECTOR,
                         "#app > div > div > section > div > div > div:nth-child(4) > fieldset > table > tr > td > span")
        value_locator = (By.CSS_SELECTOR, "#AutomaticLinkLocalAddress")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_selected_value_within(value_locator)

        return title, value

    # ViewAllIPv6Address
    def get_view_all_ipv6_address_header_text(self):
        # span
        header_locator = (
            By.CSS_SELECTOR, "#app > div > div > section > div > div > div:nth-child(5) > fieldset > legend")

        return self.find_element_then_get_text(header_locator)

    def get_table_title(self):
        # table title
        table_locator = (By.CSS_SELECTOR, ".has-gutter")
        cell_class_name = 'cell'

        return self.find_cells_value_within(table_locator, cell_class_name)

    def get_table_default_is_empty(self):
        # span
        table_locator = (By.CSS_SELECTOR, ".table")
        expected_string = '< < Table is empty > >'

        return self.text_is_existed_within(table_locator, expected_string)
