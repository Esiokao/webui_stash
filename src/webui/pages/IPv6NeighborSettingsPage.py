# pages/IPv6SystemSettings.py
from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage


class IPv6NeighborSettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 IPv6NeighborSettings
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        system_menu_locator = (By.CSS_SELECTOR, ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        IPv6_Neighbor_SettingsPage_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(6) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(IPv6_Neighbor_SettingsPage_menu_locator).click()

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)

    def get_v6_neighbor_settings_tier2_header_text(self):
        v6_neighbor_settings_tier2_header_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(v6_neighbor_settings_tier2_header_locator)

    def get_interface_name_title_and_value(self):
        #  span
        title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        value_locator = (By.CSS_SELECTOR, "#InterfaceName1")

        title = self.find_element_then_get_text(title_locator)
        value = self.find_element_then_get_text(value_locator)

        return title, value

    def get_Neighbor_IPv6_Address_title_and_value(self):
        #  span
        title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        value_locator = (By.CSS_SELECTOR, "#NeighborIPv6Address > input")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_element_then_get_text(value_locator)

        return title, value

    def get_Link_Layer_MAC_Address_title_and_value(self):
        #  span
        title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")
        value_locator = (By.CSS_SELECTOR, "#LinkLayerMACAddress > input")

        title = self.find_element_then_get_text(title_locator)
        value = self.find_element_then_get_text(value_locator)

        return title, value

    def get_ipv6_neighbor_settings_button_text(self):
        ipv6_neighbor_settings_button_locator = (By.CSS_SELECTOR, "#ApplyTrap")

        return self.find_input_value(ipv6_neighbor_settings_button_locator)

    def get_ipv6_neighbor_Table_header_text(self):
        ipv6_neighbor_Table_header_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > legend")

        return self.find_element_then_get_text(ipv6_neighbor_Table_header_locator)

    def get_Neighbor_Table_interface_name_title_and_value(self):
        #  span
        title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td > span")
        value_locator = (By.CSS_SELECTOR, "#InterfaceName2")

        title = self.find_element_then_get_text(title_locator)
        value = self.find_element_then_get_text(value_locator)

        return title, value

    def get_state_title_and_value(self):
        #  span
        title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr:nth-child(2) > td > span")
        value1_locator = (By.CSS_SELECTOR, "#State")
        value2_locator = (By.CSS_SELECTOR, "#NeighborIPv6Address2 > input")
        title = self.find_element_then_get_text(title_locator)
        value1 = self.find_selected_value_within(value1_locator)
        value2 = self.find_element_then_get_text(value2_locator)

        return title, value1, value2

    def get_ipv6_neighbor_table_button1_text(self):
        ipv6_neighbor_table_button1_locator = (By.CSS_SELECTOR, "#Find")
        return self.find_input_value(ipv6_neighbor_table_button1_locator)

    def get_ipv6_neighbor_table_button2_text(self):
        ipv6_neighbor_table_button2_locator = (By.CSS_SELECTOR, "#Clear")
        return self.find_input_value(ipv6_neighbor_table_button2_locator)

    def get_total_entries_title(self):
        total_entries_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > div > table > tr > td > span")
        return self.find_element_then_get_text(total_entries_title_locator)

    def get_table_title(self):
        table_locator = (By.CSS_SELECTOR, ".has-gutter")
        cell_class_name = "cell"
        return self.find_cells_value_within(table_locator, cell_class_name)

    def get_table_default_is_empty(self):
        # span
        table_locator = (By.CSS_SELECTOR, ".table")
        expected_string = "< < Table is empty > >"

        return self.text_is_existed_within(table_locator, expected_string)
