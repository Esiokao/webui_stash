# pages/IPv6SystemSettings.py
from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class AccessProfileListPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 Access Profile List
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        ACL_menu_locator = (
            By.CSS_SELECTOR,
            "#app > div > div > div > div > div > div > ul > div:nth-child(8) > li > div > i")
        Access_Profile_List_menu_locator = (By.CSS_SELECTOR, "#app > div > div > div > div > div > div > ul > div:nth-child(8) > li > ul > div:nth-child(2) > a > li > span")

        self.find_element_if_present(ACL_menu_locator).click()
        self.find_element_if_present(Access_Profile_List_menu_locator).click()

    def get_page_header_text(self):
        header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(header_locator)
    
    def get_ACL_Profile_List_tier2_header_text(self):
        ACL_Profile_List_tier2_header_locator = (
            By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(ACL_Profile_List_tier2_header_locator)
    
    def get_ACL_Profile_button1_text(self):
        ACL_Profile_button_locator = (
            By.CSS_SELECTOR, "#AddACLProfile")

        return self.find_input_value(ACL_Profile_button_locator)
    
    def get_ACL_Profile_button2_text(self):
        ACL_Profile_List_table_title_locator = (
            By.CSS_SELECTOR, "#DeleteAll")

        return self.find_input_value(ACL_Profile_List_table_title_locator)
    
    def get_table_title(self):
        # table title
        table_locator = (By.CSS_SELECTOR, ".has-gutter")
        cell_class_name = 'cell'

        return self.find_cells_value_within(table_locator, cell_class_name)

    def get_ACL_Profile_table_total_text(self):
        ACL_Profile_table_total_locator = (
            By.CSS_SELECTOR, ".sx-section > fieldset > table:nth-child(4) > tr > td > span")

        return self.find_element_then_get_text(ACL_Profile_table_total_locator)

    def get_table_default_is_empty(self):
        # span
        table_locator = (By.CSS_SELECTOR, ".table")
        expected_string = '< < Table is empty > >'

        return self.text_is_existed_within(table_locator, expected_string)
