# pages/FirmwareInformationPage.py
import os

from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage


class FirmwareInformationPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 FirmwareInformationPage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

    def init(self):
        SYSTEM_MENU_LOCATOR = (By.CSS_SELECTOR, ".menu-wrapper:nth-child(2) > .el-submenuTitle > .el-submenu__title > .el-submenu__icon-arrow")
        FIRMWARE_INFORMATION_MENU_LOCATOR = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(2) span")

        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(FIRMWARE_INFORMATION_MENU_LOCATOR).click()

        return True

    def get_firmware_information_table_title(self):
        FIRMWARE_INFORMATION_TABLE_LOCATOR = (By.CLASS_NAME, "has-gutter")
        cells_class_name = "cell"

        return self.find_cells_value_within(FIRMWARE_INFORMATION_TABLE_LOCATOR, cells_class_name)

    def find_selected_input_text(self):
        selected_input_label_text_locator = (
            By.CSS_SELECTOR,
            "#app > div > div > section > div > div > div.sx-section > fieldset > table:nth-child(3) > tr:nth-child(1) > td > span",
        )

        return self.find_element_then_get_text(selected_input_label_text_locator)

    def get_firmware_version_exists(self) -> bool:
        from dotenv import load_dotenv

        load_dotenv("Settings.env")
        firmware_version = os.getenv("FIRMWARE_VERSION")
        table_locator = (By.CSS_SELECTOR, ".el-table")

        return self.text_is_existed_within(table_locator, firmware_version)

    def get_config_default_option(self):
        CONFIG_DEFAULT_OPTION_LOCATOR = (
            By.CSS_SELECTOR,
            "#app > div > div > section > div > div > div.sx-section > fieldset > table:nth-child(3) > tr:nth-child(2) > td > select",
        )
        return self.find_selected_value_within(CONFIG_DEFAULT_OPTION_LOCATOR)

    def get_firmware_default_option(self):
        FIRMWARE_DEFAULT_OPTION_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(3) > tr:nth-child(3) > td:nth-child(1) > select:nth-child(1)")
        return self.find_selected_value_within(FIRMWARE_DEFAULT_OPTION_LOCATOR)

    def get_apply_button_element(self):
        APPLY_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#apply")
        return self.find_element_if_present(APPLY_BUTTON_LOCATOR)

    def get_apply_button_text(self):
        APPLY_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#apply")
        return self.find_input_value(APPLY_BUTTON_LOCATOR)

    def get_row_1_title_and_desc(self):
        TITLE_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(2) > td:nth-child(1)")
        DESC_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(2) > td:nth-child(2)")
        title = super().find_element_then_get_text(TITLE_LOCATOR)
        desc = super().find_element_then_get_text(DESC_LOCATOR)

        return title, desc

    def get_row_2_title_and_desc(self):
        TITLE_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(3) > td:nth-child(1)")
        DESC_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(3) > td:nth-child(2)")
        title = super().find_element_then_get_text(TITLE_LOCATOR)
        desc = super().find_element_then_get_text(DESC_LOCATOR)

        return title, desc

    def get_row_3_title_and_desc(self):
        TITLE_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(4) > td:nth-child(1)")
        DESC_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(4) > td:nth-child(2)")
        title = super().find_element_then_get_text(TITLE_LOCATOR)
        desc = super().find_element_then_get_text(DESC_LOCATOR)

        return title, desc

    def get_row_4_title_and_desc(self):
        TITLE_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(5) > td:nth-child(1)")
        DESC_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(5) > td:nth-child(2)")
        title = super().find_element_then_get_text(TITLE_LOCATOR)
        desc = super().find_element_then_get_text(DESC_LOCATOR)

        return title, desc

    def get_row_5_title_and_desc(self):
        TITLE_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(6) > td:nth-child(1)")
        DESC_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(6) > td:nth-child(2)")
        title = super().find_element_then_get_text(TITLE_LOCATOR)
        desc = super().find_element_then_get_text(DESC_LOCATOR)

        return title, desc

    def get_row_6_title_and_desc(self):
        TITLE_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(7) > td:nth-child(1)")
        DESC_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(7) > td:nth-child(2)")
        title = super().find_element_then_get_text(TITLE_LOCATOR)
        desc = super().find_element_then_get_text(DESC_LOCATOR)

        return title, desc

    def get_row_7_title_and_desc(self):
        TITLE_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(8) > td:nth-child(1)")
        DESC_LOCATOR = (By.CSS_SELECTOR, "table.sx-form:nth-child(4) > tr:nth-child(8) > td:nth-child(2)")
        title = super().find_element_then_get_text(TITLE_LOCATOR)
        desc = super().find_element_then_get_text(DESC_LOCATOR)

        return title, desc
