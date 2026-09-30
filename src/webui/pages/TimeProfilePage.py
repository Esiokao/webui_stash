# pages/TimeProfilePage.py
from selenium.webdriver.common.by import By
import re

from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class TimeProfilePage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 TimeProfilePage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        system_menu_locator = (
            By.CSS_SELECTOR,
            ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        TIME_PROFILE_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(24) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(TIME_PROFILE_menu_locator).click()

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)

    def get_time_range_tier2_header_text(self):
        get_time_range_tier2_header_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(get_time_range_tier2_header_locator)

    def get_range_name_title_and_value(self):
        get_range_name_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        range_name_value_locator = (By.CSS_SELECTOR, "#RangeName")

        title = self.find_element_then_get_text(get_range_name_title_locator)
        value = self.find_input_value(range_name_value_locator)

        return title, value
    
    def get_date_title_and_value(self):
        get_date_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        date_value_locator1 = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > div > div > div > input")
        date_value_locator2 = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > div > div > div > input:nth-child(2)")

        title = self.find_element_then_get_text(get_date_title_locator)
        value1 = self.find_input_value(date_value_locator1)
        value2 = self.find_input_value(date_value_locator2)

        return title, value1, value2
    
    def get_hours_title_and_value(self):
        get_hours_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")
        hours_value_locator1 = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > div > div > div > input")
        hours_value_locator2 = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > div > div > div:nth-child(2) > input")

        title = self.find_element_then_get_text(get_hours_title_locator)
        value1 = self.find_input_value(hours_value_locator1)
        value2 = self.find_input_value(hours_value_locator2)

        return title, value1, value2

    def get_weekdays_title_and_value(self):
        get_weekdays_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(4) > td > span")
        get_weekdays_value_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(4) > td:nth-child(3)")

        title = self.find_element_then_get_text(get_weekdays_title_locator)
        value2 = self.find_element_then_get_text(get_weekdays_value_locator)
        weekdays_td_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(4) > td:nth-child(2)")
        value = self.find_element_then_get_text(weekdays_td_locator)
        value = value.replace('\xa0', ' ').replace('\n', ' ')
        value = re.sub(r'\s+', ' ', value).strip()

        return title, value, value2

    def get_button_text(self):
        button_text_locator = (By.CSS_SELECTOR, "#Apply")
        return self.find_input_value(button_text_locator)
    
    def get_time_range_information_header_text(self):
        time_range_information_header_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > legend")

        return self.find_element_then_get_text(time_range_information_header_locator)

    def get_total_entries_title(self):
        total_entries_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > div > table > tr > td > span")
        return self.find_element_then_get_text(total_entries_title_locator)
    
    def get_table_title(self):
        table_title_locator = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(table_title_locator, cells_class_name)
    
    def get_table_default_is_empty(self):
        # span
        table_locator = (By.CSS_SELECTOR, ".table")
        expected_string = '< < Table is empty > >'

        return self.text_is_existed_within(table_locator, expected_string)
    
    
