# pages/SerialPortSettingsPage.py
from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class SerialPortSettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 SerialPortSettingsPage
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
        SERIAL_PORT_SETTINGS_MENU_LOCATOR = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(3) span")

        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SERIAL_PORT_SETTINGS_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, ".sx-title1")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)

    def get_tier2_header_text(self):
        TIER2_PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, ".sx-title2")
        return self.find_element_then_get_text(TIER2_PAGE_HEADER_LOCATOR)

    def get_baud_rate(self):
        baud_rate_title_locator = (By.CSS_SELECTOR, ".sx-form > tr:nth-child(1) > td:nth-child(1) > span:nth-child(1)")
        baud_rate_select_box_locator = (By.CSS_SELECTOR, "#BaudRate")
        title = self.find_element_then_get_text(baud_rate_title_locator)
        value = self.find_selected_value_within(baud_rate_select_box_locator)

        return title, value

    def get_auto_logout(self):
        auto_logout_title_locator = (By.CSS_SELECTOR, ".sx-form > tr:nth-child(2) > td:nth-child(1) > span:nth-child(1)")
        auto_logout_select_box_locator = (By.CSS_SELECTOR, "#AutoLogout")
        title = self.find_element_then_get_text(auto_logout_title_locator)
        value = self.find_selected_value_within(auto_logout_select_box_locator)

        return title, value

    def get_data_bits(self):
        data_bits_title_locator = (By.CSS_SELECTOR, ".sx-form > tr:nth-child(3) > td:nth-child(1) > span:nth-child(1)")
        data_bits_value_locator = (By.CSS_SELECTOR, ".sx-form > tr:nth-child(3) > td:nth-child(2) > span:nth-child(1)")
        title = self.find_element_then_get_text(data_bits_title_locator)
        value = self.find_element_then_get_text(data_bits_value_locator)

        return title, value

    def get_parity_bits(self):
        parity_bits_title_locator = (By.CSS_SELECTOR, ".sx-form > tr:nth-child(4) > td:nth-child(1) > span:nth-child(1)")
        data_bits_value_locator = (By.CSS_SELECTOR, ".sx-form > tr:nth-child(4) > td:nth-child(2) > span:nth-child(1)")
        title = self.find_element_then_get_text(parity_bits_title_locator)
        value = self.find_element_then_get_text(data_bits_value_locator)

        return title, value

    def get_stop_bits(self):
        stop_bits_title_locator =  (By.CSS_SELECTOR, ".sx-form > tr:nth-child(5) > td:nth-child(1) > span:nth-child(1)")
        stop_bits_value_locator = (By.CSS_SELECTOR, ".sx-form > tr:nth-child(5) > td:nth-child(2) > span:nth-child(1)")
        title = self.find_element_then_get_text(stop_bits_title_locator)
        value = self.find_element_then_get_text(stop_bits_value_locator)

        return title, value
