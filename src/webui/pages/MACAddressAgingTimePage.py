# pages/MACAddressAgingTimePage.py
from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage


class MACAddressAgingTimePage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 MACAddressAgingTimePage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        system_menu_locator = (By.CSS_SELECTOR, ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        MAC_ADDRESS_AGING_TIME_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(13) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(MAC_ADDRESS_AGING_TIME_menu_locator).click()

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)

    def get_mac_address_aging_time_tier2_header_text(self):
        get_mac_address_aging_time_tier2_header_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(get_mac_address_aging_time_tier2_header_locator)

    def get_mac_address_aging_time_title_and_value(self):
        get_mac_address_aging_time_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        get_mac_address_aging_time_value_locator = (By.CSS_SELECTOR, "#MACAddressAgingTime")

        title = self.find_element_then_get_text(get_mac_address_aging_time_title_locator)
        value = self.find_input_value(get_mac_address_aging_time_value_locator)

        return title, value

    def get_get_mac_address_aging_time_button_text(self):
        get_mac_address_aging_time_button_locator = (By.CSS_SELECTOR, "#Apply")

        return self.find_input_value(get_mac_address_aging_time_button_locator)

    # Action / Setting Methods
    def set_mac_address_aging_time(self, time_val: str):
        locator = (By.CSS_SELECTOR, "#MACAddressAgingTime")
        self.input_text(locator, str(time_val))

    def click_apply(self):
        self.click_element((By.CSS_SELECTOR, "#Apply"))

