# pages/ARPAgingTimeSettingsPage.py
from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage


class ARPAgingTimeSettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 ARPAgingTimeSettingsPage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        system_menu_locator = (By.CSS_SELECTOR, ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        ARP_AGING_TIME_SETTINGS_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(14) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(ARP_AGING_TIME_SETTINGS_menu_locator).click()

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)

    def get_arp_aging_time_settings_tier2_header_text(self):
        get_arp_aging_time_settings_tier2_header_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(get_arp_aging_time_settings_tier2_header_locator)

    def get_arp_aging_time_title_and_value(self):
        get_arp_aging_time_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        get_arp_aging_time_value_locator = (By.CSS_SELECTOR, "#ARPAgingTime")

        title = self.find_element_then_get_text(get_arp_aging_time_title_locator)
        value = self.find_input_value(get_arp_aging_time_value_locator)

        return title, value

    def get_get_arp_aging_time_button_text(self):
        get_arp_aging_time_button_locator = (By.CSS_SELECTOR, "#Apply")

        return self.find_input_value(get_arp_aging_time_button_locator)
