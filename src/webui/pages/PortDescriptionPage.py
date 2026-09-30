# pages/PortDescription.Page.py
from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class PortDescriptionPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 PortDescriptionPage
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
        SERIAL_Port_Configuration_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(10) > li > div > span:nth-child(4)")
        SERIAL_PORT_DESCRIPTION_MENU_LOCATOR = (By.CSS_SELECTOR, 
        "div:nth-child(2) > li > ul > div:nth-child(10) > li > ul > div:nth-child(2) > a > li > span")

        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SERIAL_Port_Configuration_MENU_LOCATOR).click()
        self.find_element_if_present(SERIAL_PORT_DESCRIPTION_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")

        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)
    
    def get_port_description_tier2_header_text(self):
        PORT_DESCRIPTION_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(PORT_DESCRIPTION_TIER2_HEADER_LOCATOR)
    
    def get_from_port_title_and_value(self):
        FROM_PORT_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td")
        FROM_PORT_VALUE_LOCATOR = (By.CSS_SELECTOR, "#fromPort")

        title = self.find_element_then_get_text(FROM_PORT_TITLE_LOCATOR)
        value = self.find_selected_value_within(FROM_PORT_VALUE_LOCATOR)

        return title, value
    
    def get_to_port_title_and_value(self):
        TO_PORT_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2)")
        TO_PORT_VALUE_LOCATOR = (By.CSS_SELECTOR, "#toPort")

        title = self.find_element_then_get_text(TO_PORT_TITLE_LOCATOR)
        value = self.find_selected_value_within(TO_PORT_VALUE_LOCATOR)

        return title, value
    
    def get_medium_type_title_and_value(self):
        MEDIUM_TYPE_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(3)")
        MEDIUM_TYPE_VALUE_LOCATOR = (By.CSS_SELECTOR, "#media")

        title = self.find_element_then_get_text(MEDIUM_TYPE_TITLE_LOCATOR)
        value = self.find_selected_value_within(MEDIUM_TYPE_VALUE_LOCATOR)

        return title, value
    
    def get_description_title_and_value(self):
        DESCRIPTION_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(4)")
        DESCRIPTION_VALUE_LOCATOR = (By.CSS_SELECTOR, "#description")

        title = self.find_element_then_get_text(DESCRIPTION_TITLE_LOCATOR)
        value = self.find_input_value(DESCRIPTION_VALUE_LOCATOR)

        return title, value
    
    def get_table_title(self):
        TABLE_TITLE_LOCATOR = (By.CSS_SELECTOR, ".has-gutter")

        return self.find_cells_value_within(TABLE_TITLE_LOCATOR, "cell")
    
    def get_table_value(self):
        TABLE_VALUE_LOCATOR = (By.CSS_SELECTOR, ".el-table__row")

        return self.find_cells_value_within(TABLE_VALUE_LOCATOR, "cell")
    
    def get_port_description_button_value(self):
        PORT_DESCRIPTION_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#Apply")
        
        return self.find_input_value(PORT_DESCRIPTION_BUTTON_LOCATOR)
    

    

