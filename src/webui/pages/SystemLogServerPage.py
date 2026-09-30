# pages/SystemLogServerPage.py
from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class SystemLogServerPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 SystemLogServerPage
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
        SYSTEM_LOG_SERVER_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(23) > li > div > span:nth-child(4)")
        SYSTEM_LOG_SERVER_LIST_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(23) > li > ul > div:nth-child(2) > a > li > span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SYSTEM_LOG_SERVER_MENU_LOCATOR).click()
        self.find_element_if_present(SYSTEM_LOG_SERVER_LIST_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)
    
    def get_add_system_log_server_tier2_header_text(self):
        ADD_SYSTEM_LOG_SERVER_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(ADD_SYSTEM_LOG_SERVER_TIER2_HEADER_LOCATOR)

    def get_server_id_title_and_value(self):
        SERVER_ID_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        SERVER_ID_VALUE_LOCATOR = (By.CSS_SELECTOR, "#ServerID")
        title = self.find_element_then_get_text(SERVER_ID_TITLE_LOCATOR)
        value = self.find_selected_value_within(SERVER_ID_VALUE_LOCATOR)
        return title, value

    def get_server_ipv4_address_title_and_value(self):
        title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        title = self.find_element_then_get_text(title_locator)
        ipv4_octets = [
            self.find_input_value(locator)
            for locator in [
                (By.CSS_SELECTOR, "#ServerIPv4Address > span > input[type=text]:nth-child(1)"),
                (By.CSS_SELECTOR, "#ServerIPv4Address > span > input[type=text]:nth-child(3)"),
                (By.CSS_SELECTOR, "#ServerIPv4Address > span > input[type=text]:nth-child(5)"),
                (By.CSS_SELECTOR, "#ServerIPv4Address > span > input[type=text]:nth-child(7)"),
            ]
        ]

        ipv4_addr = ".".join(ipv4_octets)
        return title, ipv4_addr
    
    def get_server_ipv6_address_title_and_value(self):
        title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")
        ipv6_locator = (By.CSS_SELECTOR, "#ServerIPv6Address > input")
        title = self.find_element_then_get_text(title_locator)
        ipv6_addr = self.find_input_value(ipv6_locator)
        return title, ipv6_addr

    def get_checked_v4_mode_option(self):
        v4_mode_locator = (By.CSS_SELECTOR, "#IPv4Radio")
        return self.find_checkbox_checked(v4_mode_locator)

    def get_checked_v6_mode_option(self):
        v6_mode_locator = (By.CSS_SELECTOR, "#IPv6Radio")
        return self.find_checkbox_checked(v6_mode_locator)
    
    def get_domain_title_and_value(self):
        title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(4) > td > span")
        value_locator = (By.CSS_SELECTOR, "#Domain")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_input_value(value_locator)
        return title, value
    
    def get_checked_domain_mode_option(self):
        domain_mode_locator = (By.XPATH, "/html/body/div[1]/div/div/section/div/section/div/div[2]/fieldset/table/tr[4]/td[1]/input")
        return self.find_checkbox_checked(domain_mode_locator)
    
    def get_severity_title_and_value(self):
        title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(3) > span")
        value_locator = (By.CSS_SELECTOR, "#Severity")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_selected_value_within(value_locator)
        return title, value

    def get_facility_title_and_value(self):
        title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(3) > span")
        value_locator = (By.CSS_SELECTOR, "#Facility")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_selected_value_within(value_locator)
        return title, value

    def get_udp_port_title_and_value(self):
        title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td:nth-child(3) > span")
        value_locator = (By.CSS_SELECTOR, "#UDPPort")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_input_value(value_locator)
        return title, value

    def get_status_title_and_value(self):
        title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(4) > td:nth-child(3) > span")
        value_locator = (By.CSS_SELECTOR, "#Status")
        title = self.find_element_then_get_text(title_locator)
        value = self.find_selected_value_within(value_locator)
        return title, value

    def get_button_text(self):
        button_locator = (By.CSS_SELECTOR, "#Apply")
        return self.find_input_value(button_locator)

    def get_system_log_server_list_header_text(self):
        SYSTEM_LOG_SERVER_LIST_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > legend")
        return self.find_element_then_get_text(SYSTEM_LOG_SERVER_LIST_HEADER_LOCATOR)

    def get_total_entries_title(self):
        total_entries_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > div > table > tr > td > span")
        return self.find_element_then_get_text(total_entries_locator)

    def get_table_title(self):
        TABLE_TITLE_LOCATOR = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(TABLE_TITLE_LOCATOR, cells_class_name)

    def get_table_default_is_empty(self):
        # span
        table_locator = (By.CSS_SELECTOR, ".table")
        expected_string = '< < Table is empty > >'

        return self.text_is_existed_within(table_locator, expected_string)


