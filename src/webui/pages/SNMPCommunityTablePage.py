# pages/SNMPCommunityTablePage.py
from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class SNMPCommunityTablePage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 SNMPCommunityTablePage
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
        SNMP_COMMUNITY_TABLE_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(11) > li > ul > div:nth-child(5) > a > li > span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_SETTINGS_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_COMMUNITY_TABLE_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)
    
    def get_snmp_community_table_tier2_header_text(self):
        SNMP_COMMUNITY_TABLE_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(SNMP_COMMUNITY_TABLE_TIER2_HEADER_LOCATOR)
    
    def get_community_name_title_and_value(self):
        COMMUNITY_NAME_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        COMMUNITY_NAME_VALUE_LOCATOR = (By.CSS_SELECTOR, "#CommunityName")
        title = self.find_element_then_get_text(COMMUNITY_NAME_TITLE_LOCATOR)
        value = self.find_input_value(COMMUNITY_NAME_VALUE_LOCATOR)
        return title, value
    
    def get_view_name_title_and_value(self):
        VIEW_NAME_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        VIEW_NAME_VALUE_LOCATOR = (By.CSS_SELECTOR, "#viewName")
        title = self.find_element_then_get_text(VIEW_NAME_TITLE_LOCATOR)
        value = self.find_input_value(VIEW_NAME_VALUE_LOCATOR)
        return title, value
    
    def get_access_right_title_and_value(self):
        ACCESS_RIGHT_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")
        ACCESS_RIGHT_VALUE_LOCATOR = (By.CSS_SELECTOR, "#UserNameViewPolicy")
        title = self.find_element_then_get_text(ACCESS_RIGHT_TITLE_LOCATOR)
        value = self.find_selected_value_within(ACCESS_RIGHT_VALUE_LOCATOR)
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
    
    def get_private_table_value(self):
        PRIVATE_TABLE_VALUE_LOCATOR = (By.CSS_SELECTOR, ".el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1)")
        cells_class_name = "cell"
        return self.find_cells_value_within(PRIVATE_TABLE_VALUE_LOCATOR, cells_class_name)
    
    def get_private_table_button_text(self):
        PRIVATE_TABLE_BUTTON_TEXT_LOCATOR = (By.CSS_SELECTOR, "#delete_0")
        return self.find_input_value(PRIVATE_TABLE_BUTTON_TEXT_LOCATOR)
    
    def get_public_table_value(self):
        PUBLIC_TABLE_VALUE_LOCATOR = (By.CSS_SELECTOR, ".el-table__row.el-table__row--striped")
        cells_class_name = "cell"
        return self.find_cells_value_within(PUBLIC_TABLE_VALUE_LOCATOR, cells_class_name)
    
    def get_public_table_button_text(self):
        PUBLIC_TABLE_BUTTON_TEXT_LOCATOR = (By.CSS_SELECTOR, "#delete_1")
        return self.find_input_value(PUBLIC_TABLE_BUTTON_TEXT_LOCATOR)
    
