# pages/SNMPGroupTablePage.py
from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class SNMPGroupTablePage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 SNMPGroupTablePage
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
        SNMP_GROUP_TABLE_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(11) > li > ul > div:nth-child(3) > a > li > span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_SETTINGS_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_GROUP_TABLE_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)
    
    def get_snmp_group_table_tier2_header_text(self):
        SNMP_GROUP_TABLE_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(SNMP_GROUP_TABLE_TIER2_HEADER_LOCATOR)
    
    def get_group_name_title_and_value(self):
        GROUP_NAME_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        GROUP_NAME_VALUE_LOCATOR = (By.CSS_SELECTOR, "#GroupName")
        title = self.find_element_then_get_text(GROUP_NAME_TITLE_LOCATOR)
        value = self.find_input_value(GROUP_NAME_VALUE_LOCATOR)
        return title, value

    def get_read_view_name_title_and_value(self):
        READ_VIEW_NAME_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        READ_VIEW_NAME_VALUE_LOCATOR = (By.CSS_SELECTOR, "#ReadViewName")
        title = self.find_element_then_get_text(READ_VIEW_NAME_TITLE_LOCATOR)
        value = self.find_input_value(READ_VIEW_NAME_VALUE_LOCATOR)
        return title, value

    def get_write_view_name_title_and_value(self):
        WRITE_VIEW_NAME_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")
        WRITE_VIEW_NAME_VALUE_LOCATOR = (By.CSS_SELECTOR, "#WriteViewName")
        title = self.find_element_then_get_text(WRITE_VIEW_NAME_TITLE_LOCATOR)
        value = self.find_input_value(WRITE_VIEW_NAME_VALUE_LOCATOR)
        return title, value

    def get_security_model_title_and_value(self):
        SECURITY_MODEL_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(3) > span")
        SECURITY_MODEL_VALUE_LOCATOR = (By.CSS_SELECTOR, "#SecurityModel")
        title = self.find_element_then_get_text(SECURITY_MODEL_TITLE_LOCATOR)
        value = self.find_selected_value_within(SECURITY_MODEL_VALUE_LOCATOR)
        return title, value

    def get_security_level_title_and_value(self):
        SECURITY_LEVEL_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(3) > span")
        SECURITY_LEVEL_VALUE_LOCATOR = (By.CSS_SELECTOR, "#SecurityLevel")
        title = self.find_element_then_get_text(SECURITY_LEVEL_TITLE_LOCATOR)
        value = self.find_selected_value_within(SECURITY_LEVEL_VALUE_LOCATOR)
        return title, value

    def get_notify_view_name_title_and_value(self):
        NOTIFY_VIEW_NAME_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td:nth-child(3) > span")
        NOTIFY_VIEW_NAME_VALUE_LOCATOR = (By.CSS_SELECTOR, "#NotifyViewName")
        title = self.find_element_then_get_text(NOTIFY_VIEW_NAME_TITLE_LOCATOR)
        value = self.find_input_value(NOTIFY_VIEW_NAME_VALUE_LOCATOR)
        return title, value

    def get_snmp_group_table_button_text(self):
        SNMP_GROUP_TABLE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#Apply")
        return self.find_input_value(SNMP_GROUP_TABLE_BUTTON_LOCATOR)

    def get_total_entries_title(self):
        TOTAL_ENTRIES_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > div > table > tr > td > span")
        return self.find_element_then_get_text(TOTAL_ENTRIES_TITLE_LOCATOR)

    def get_table_title(self):
        TABLE_TITLE_LOCATOR = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(TABLE_TITLE_LOCATOR, cells_class_name)
        
    def get_readonly_v1_table_value(self):
        TABLE_VALUE_LOCATOR = (By.CSS_SELECTOR, ".el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1)")
        cells_class_name = "cell"
        return self.find_cells_value_within(TABLE_VALUE_LOCATOR, cells_class_name)

    def get_readonly_v1_table_button_text(self):
        TABLE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#delete_0")
        return self.find_input_value(TABLE_BUTTON_LOCATOR)

    def get_readonly_v2c_table_value(self):
        TABLE_VALUE_LOCATOR = (By.CSS_SELECTOR, ".el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(2)")
        cells_class_name = "cell"
        return self.find_cells_value_within(TABLE_VALUE_LOCATOR, cells_class_name)

    def get_readonly_v2c_table_button_text(self):
        TABLE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#delete_1")
        return self.find_input_value(TABLE_BUTTON_LOCATOR)
    
    def get_read_write_v1_table_value(self):
        TABLE_VALUE_LOCATOR = (By.CSS_SELECTOR, ".el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(3)")
        cells_class_name = "cell"
        return self.find_cells_value_within(TABLE_VALUE_LOCATOR, cells_class_name)

    def get_read_write_v1_table_button_text(self):
        TABLE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#delete_2")
        return self.find_input_value(TABLE_BUTTON_LOCATOR)

    def get_read_write_v2c_table_value(self):
        TABLE_VALUE_LOCATOR = (By.CSS_SELECTOR, ".el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(4)")
        cells_class_name = "cell"
        return self.find_cells_value_within(TABLE_VALUE_LOCATOR, cells_class_name)

    def get_read_write_v2c_table_button_text(self):
        TABLE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#delete_3")
        return self.find_input_value(TABLE_BUTTON_LOCATOR)
        
    def get_group_table_page_text(self):
        GROUP_TABLE_PAGE_TEXT_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > span.counter")
        return self.find_element_then_get_text(GROUP_TABLE_PAGE_TEXT_LOCATOR)
    
    def get_group_table_page_button1_text(self):
        GROUP_TABLE_PAGE_BUTTON1_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > a.firstPage.isdisabled-btn")
        return self.find_element_then_get_text(GROUP_TABLE_PAGE_BUTTON1_LOCATOR)
    
    def get_group_table_page_button2_text(self):
        GROUP_TABLE_PAGE_BUTTON2_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > a.prevPage.isdisabled-btn")
        return self.find_element_then_get_text(GROUP_TABLE_PAGE_BUTTON2_LOCATOR)
    
    def get_group_table_page_button3_text(self):
        GROUP_TABLE_PAGE_BUTTON3_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > span.pageNum.slected")
        return self.find_element_then_get_text(GROUP_TABLE_PAGE_BUTTON3_LOCATOR)
    
    def get_group_table_page_button4_text(self):
        GROUP_TABLE_PAGE_BUTTON4_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > a.nextPage.isdisabled-btn")
        return self.find_element_then_get_text(GROUP_TABLE_PAGE_BUTTON4_LOCATOR)
    
    def get_group_table_page_button5_text(self):
        GROUP_TABLE_PAGE_BUTTON5_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > a.lastPage.isdisabled-btn")
        return self.find_element_then_get_text(GROUP_TABLE_PAGE_BUTTON5_LOCATOR)

    def get_group_table_page_value(self):
        GROUP_TABLE_PAGE_VALUE_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > input.nPageNum")
        return self.find_input_value(GROUP_TABLE_PAGE_VALUE_LOCATOR)

    def get_group_table_page_button6_text(self):
        GROUP_TABLE_PAGE_BUTTON6_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > input.goButton")
        return self.find_input_value(GROUP_TABLE_PAGE_BUTTON6_LOCATOR)

