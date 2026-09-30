# pages/SNMPViewTablePage.py
from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage


class SNMPViewTablePage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 SNMPViewTablePage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        SYSTEM_MENU_LOCATOR = (By.CSS_SELECTOR, ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        SNMP_SETTINGS_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(11) > li > div > span:nth-child(4)")
        SNMP_USER_TABLE_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(11) > li > ul > div:nth-child(4) > a > li > span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_SETTINGS_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_USER_TABLE_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)

    def get_snmp_view_table_tier2_header_text(self):
        SNMP_VIEW_TABLE_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(SNMP_VIEW_TABLE_TIER2_HEADER_LOCATOR)

    def get_view_name_title_and_value(self):
        VIEW_NAME_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        VIEW_NAME_VALUE_LOCATOR = (By.CSS_SELECTOR, "#ViewName")
        title = self.find_element_then_get_text(VIEW_NAME_TITLE_LOCATOR)
        value = self.find_input_value(VIEW_NAME_VALUE_LOCATOR)
        return title, value

    def get_subtree_oid_title_and_value(self):
        SUBTREE_OID_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        SUBTREE_OID_VALUE_LOCATOR = (By.CSS_SELECTOR, "#SubtreeOID")
        title = self.find_element_then_get_text(SUBTREE_OID_TITLE_LOCATOR)
        value = self.find_input_value(SUBTREE_OID_VALUE_LOCATOR)
        return title, value

    def get_oid_mask_title_and_value(self):
        OID_MASK_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")
        OID_MASK_VALUE_LOCATOR = (By.CSS_SELECTOR, "#OIDMask")
        title = self.find_element_then_get_text(OID_MASK_TITLE_LOCATOR)
        value = self.find_input_value(OID_MASK_VALUE_LOCATOR)
        return title, value

    def get_view_type_title_and_value(self):
        VIEW_TYPE_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(4) > td > span")
        VIEW_TYPE_VALUE_LOCATOR = (By.CSS_SELECTOR, "#ViewType")
        title = self.find_element_then_get_text(VIEW_TYPE_TITLE_LOCATOR)
        value = self.find_selected_value_within(VIEW_TYPE_VALUE_LOCATOR)
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

    def get_readonly_table_value(self):
        READONLY_TABLE_VALUE_LOCATOR = (By.CSS_SELECTOR, ".el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(1)")
        cells_class_name = "cell"
        return self.find_cells_value_within(READONLY_TABLE_VALUE_LOCATOR, cells_class_name)

    def get_readonly_table_button_text(self):
        READONLY_TABLE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#delete_0")
        return self.find_input_value(READONLY_TABLE_BUTTON_LOCATOR)

    def get_read_write_table_value(self):
        READWRITE_TABLE_VALUE_LOCATOR = (By.CSS_SELECTOR, ".el-table__body-wrapper.is-scrolling-none > table > tbody > tr:nth-child(2)")
        cells_class_name = "cell"
        return self.find_cells_value_within(READWRITE_TABLE_VALUE_LOCATOR, cells_class_name)

    def get_read_write_table_button_text(self):
        READWRITE_TABLE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#delete_1")
        return self.find_input_value(READWRITE_TABLE_BUTTON_LOCATOR)

    def get_view_table_page_text(self):
        VIEW_TABLE_PAGE_TEXT_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > span.counter")
        return self.find_element_then_get_text(VIEW_TABLE_PAGE_TEXT_LOCATOR)

    def get_view_table_page_button1_text(self):
        VIEW_TABLE_PAGE_BUTTON1_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > a.firstPage.isdisabled-btn")
        return self.find_element_then_get_text(VIEW_TABLE_PAGE_BUTTON1_LOCATOR)

    def get_view_table_page_button2_text(self):
        VIEW_TABLE_PAGE_BUTTON2_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > a.prevPage.isdisabled-btn")
        return self.find_element_then_get_text(VIEW_TABLE_PAGE_BUTTON2_LOCATOR)

    def get_view_table_page_button3_text(self):
        VIEW_TABLE_PAGE_BUTTON3_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > span.pageNum.slected")
        return self.find_element_then_get_text(VIEW_TABLE_PAGE_BUTTON3_LOCATOR)

    def get_view_table_page_button4_text(self):
        VIEW_TABLE_PAGE_BUTTON4_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > a.nextPage.isdisabled-btn")
        return self.find_element_then_get_text(VIEW_TABLE_PAGE_BUTTON4_LOCATOR)

    def get_view_table_page_button5_text(self):
        VIEW_TABLE_PAGE_BUTTON5_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > a.lastPage.isdisabled-btn")
        return self.find_element_then_get_text(VIEW_TABLE_PAGE_BUTTON5_LOCATOR)

    def get_view_table_page_value(self):
        VIEW_TABLE_PAGE_VALUE_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > input.nPageNum")
        return self.find_input_value(VIEW_TABLE_PAGE_VALUE_LOCATOR)

    def get_view_table_page_button6_text(self):
        VIEW_TABLE_PAGE_BUTTON6_LOCATOR = (By.CSS_SELECTOR, ".sx-section .sx-page > input.goButton")
        return self.find_input_value(VIEW_TABLE_PAGE_BUTTON6_LOCATOR)
