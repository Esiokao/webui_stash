# pages/UserAccountsPage.py
from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage


class UserAccountsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 UserAccountsPage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

        self.init()

    def init(self):
        SYSTEM_MENU_LOCATOR = (By.CSS_SELECTOR, ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        USER_ACCOUNTS_MENU_LOCATOR = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(12) span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(USER_ACCOUNTS_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)

    def get_user_accounts_tier2_header_text(self):
        USER_ACCOUNTS_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(USER_ACCOUNTS_TIER2_HEADER_LOCATOR)

    def get_user_name_title_and_value(self):
        USER_NAME_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        USER_NAME_VALUE_LOCATOR = (By.CSS_SELECTOR, "#UserName")
        title = self.find_element_then_get_text(USER_NAME_TITLE_LOCATOR)
        value = self.find_input_value(USER_NAME_VALUE_LOCATOR)
        return title, value

    def get_access_right_title_and_value(self):
        ACCESS_RIGHT_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td > span")
        ACCESS_RIGHT_VALUE_LOCATOR = (By.CSS_SELECTOR, "#AccessRight")
        title = self.find_element_then_get_text(ACCESS_RIGHT_TITLE_LOCATOR)
        value = self.find_selected_value_within(ACCESS_RIGHT_VALUE_LOCATOR)
        return title, value

    def get_password_title_and_value(self):
        PASSWORD_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(3) > span")
        PASSWORD_VALUE_LOCATOR = (By.CSS_SELECTOR, "#UserPassword")
        title = self.find_element_then_get_text(PASSWORD_TITLE_LOCATOR)
        value = self.find_input_value(PASSWORD_VALUE_LOCATOR)
        return title, value

    def get_confirm_password_title_and_value(self):
        CONFIRM_PASSWORD_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(3) > span")
        CONFIRM_PASSWORD_VALUE_LOCATOR = (By.CSS_SELECTOR, "#ConfirmPassword")
        title = self.find_element_then_get_text(CONFIRM_PASSWORD_TITLE_LOCATOR)
        value = self.find_input_value(CONFIRM_PASSWORD_VALUE_LOCATOR)
        return title, value

    def get_note_text(self):
        NOTE_TEXT_LOCATOR = (By.CSS_SELECTOR, "tr:nth-child(4) > td > span")
        NOTE_TEXT_LOCATOR2 = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(4) > td > span:nth-child(2)")
        NOTE_TEXT_LOCATOR3 = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(5) > td > span")
        value1 = self.find_element_then_get_text(NOTE_TEXT_LOCATOR)
        value2 = self.find_element_then_get_text(NOTE_TEXT_LOCATOR2)
        value3 = self.find_element_then_get_text(NOTE_TEXT_LOCATOR3)
        return value1, value2, value3

    def get_add_user_accounts_apply_button_text(self):
        ADD_USER_ACCOUNTS_APPLY_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#Apply")
        return self.find_input_value(ADD_USER_ACCOUNTS_APPLY_BUTTON_LOCATOR)

    def get_total_entries_title(self):
        TOTAL_ENTRIES_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > div > table > tr > td > span")
        return self.find_element_then_get_text(TOTAL_ENTRIES_TITLE_LOCATOR)

    def get_table_title(self):
        TABLE_TITLE_LOCATOR = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(TABLE_TITLE_LOCATOR, cells_class_name)

    def get_table_default_is_empty(self):
        # span
        table_locator = (By.CSS_SELECTOR, ".table")
        expected_string = "< < Table is empty > >"

        return self.text_is_existed_within(table_locator, expected_string)
