# pages/SNMPHostTable.py
from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class SNMPHostTablePage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 SNMPHostTablePage
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
        SNMP_HOST_TABLE_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(11) > li > ul > div:nth-child(6) > a > li > span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_SETTINGS_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_HOST_TABLE_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)
    
    def get_snmp_host_table_tier2_header_text(self):
        SNMP_HOST_TABLE_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(SNMP_HOST_TABLE_TIER2_HEADER_LOCATOR)
    
    def get_host_ip_address_title_and_v4_value_v6_value(self):
        title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        ipv6_locator = (By.CSS_SELECTOR, "#IPv6 > input")
        title = self.find_element_then_get_text(title_locator)
        ipv6_addr = self.find_input_value(ipv6_locator)
        ipv4_octets = [
            self.find_input_value(locator)
            for locator in [
                (By.CSS_SELECTOR, "#IPv4 > span > input[type=text]:nth-child(1)"),
                (By.CSS_SELECTOR, "#IPv4 > span > input[type=text]:nth-child(3)"),
                (By.CSS_SELECTOR, "#IPv4 > span > input[type=text]:nth-child(5)"),
                (By.CSS_SELECTOR, "#IPv4 > span > input[type=text]:nth-child(7)"),
            ]
        ]

        ipv4_addr = ".".join(ipv4_octets)
        return title, ipv4_addr, ipv6_addr

    def get_v4_mode_option_text(self):
        v4_mode_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2)")
        return self.find_element_then_get_text(v4_mode_locator)

    def get_v6_mode_option_text(self):
        v6_mode_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(2)")
        return self.find_element_then_get_text(v6_mode_locator)
        
    def get_checked_v4_mode_option(self):
        v4_mode_locator = (By.CSS_SELECTOR, "#IPv4Radio")
        return self.find_checkbox_checked(v4_mode_locator)

    def get_checked_v6_mode_option(self):
        v6_mode_locator = (By.CSS_SELECTOR, "#IPv6Radio")
        return self.find_checkbox_checked(v6_mode_locator)
        
    def get_snmp_version_title_and_value(self):
        SNMP_VERSION_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")
        SNMP_VERSION_VALUE_LOCATOR = (By.CSS_SELECTOR, "#SNMPVersion")
        title = self.find_element_then_get_text(SNMP_VERSION_TITLE_LOCATOR)
        value = self.find_selected_value_within(SNMP_VERSION_VALUE_LOCATOR)
        return title, value

    def get_community_string_snmpv3_user_name_title_and_value(self):
        COMMUNITY_STRING_SNMPV3_USER_NAME_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(4) > td > span")
        COMMUNITY_STRING_SNMPV3_USER_NAME_VALUE_LOCATOR = (By.CSS_SELECTOR, "#CommunityStringSNMPv3UserName")
        title = self.find_element_then_get_text(COMMUNITY_STRING_SNMPV3_USER_NAME_TITLE_LOCATOR)
        value = self.find_input_value(COMMUNITY_STRING_SNMPV3_USER_NAME_VALUE_LOCATOR)
        return title, value
        
    def get_button_text(self):
        BUTTON_TEXT_LOCATOR = (By.CSS_SELECTOR, "#Apply")
        return self.find_input_value(BUTTON_TEXT_LOCATOR)
    
    def get_total_entries_title(self):
        TOTAL_ENTRIES_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > div > table > tr > td > span")
        return self.find_element_then_get_text(TOTAL_ENTRIES_TITLE_LOCATOR)
    
    def get_table_title(self):
        TABLE_TITLE_LOCATOR = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(TABLE_TITLE_LOCATOR, cells_class_name)

    def get_table_default_is_empty(self):
        # span
        table_locator = (By.CSS_SELECTOR, ".table")
        expected_string = '< < Table is empty > >'

        return self.text_is_existed_within(table_locator, expected_string)

