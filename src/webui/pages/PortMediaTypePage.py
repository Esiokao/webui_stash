# pages/PortMediaTypePage.py
from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage


class PortMediaTypePage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 PortMediaTypePage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        SYSTEM_MENU_LOCATOR = (By.CSS_SELECTOR, ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        SERIAL_Port_Configuration_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(10) > li > div > span:nth-child(4)")
        SERIAL_PORT_MEDIA_TYPE_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(10) > li > ul > div:nth-child(4) > a > li > span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SERIAL_Port_Configuration_MENU_LOCATOR).click()
        self.find_element_if_present(SERIAL_PORT_MEDIA_TYPE_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)

    def get_port_media_type_tier2_header_text(self):
        PORT_MEDIA_TYPE_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(PORT_MEDIA_TYPE_TIER2_HEADER_LOCATOR)

    def get_table_title(self):
        table_locator = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(table_locator, cells_class_name)

    def get_table_value(self):
        table_locator = (By.CSS_SELECTOR, ".el-table__row")
        cells_class_name = "cell"
        return self.find_cells_value_within(table_locator, cells_class_name)
