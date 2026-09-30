# pages/SNMPEngineIDPage.py
from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class SNMPEngineIDPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 SNMPEngineIDPage
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
        SNMP_ENGINE_ID_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(11) > li > ul > div:nth-child(7) > a > li > span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_SETTINGS_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_ENGINE_ID_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)
    
    def get_snmp_engine_id_tier2_header_text(self):
        SNMP_ENGINE_ID_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(SNMP_ENGINE_ID_TIER2_HEADER_LOCATOR)
    
    def get_engine_id_title_and_value(self):
        ENGINE_ID_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        ENGINE_ID_VALUE_LOCATOR = (By.CSS_SELECTOR, "#EngineID")
        title = self.find_element_then_get_text(ENGINE_ID_TITLE_LOCATOR)
        value = self.find_input_value(ENGINE_ID_VALUE_LOCATOR)
        return title, value
    
    def get_button1_text(self):
        BUTTON1_TEXT_LOCATOR = (By.CSS_SELECTOR, "#Apply")
        return self.find_input_value(BUTTON1_TEXT_LOCATOR)
    
    def get_button2_text(self):
        BUTTON2_TEXT_LOCATOR = (By.CSS_SELECTOR, "#Default")
        return self.find_input_value(BUTTON2_TEXT_LOCATOR)
    
    def get_note_text(self):
        NOTE_TEXT_LOCATOR = (By.CSS_SELECTOR, "tr:nth-child(3) > td > span")
        NOTE_TEXT_LOCATOR2 = (By.CSS_SELECTOR, "tr:nth-child(3) > td > span:nth-child(2)")
        value1 = self.find_element_then_get_text(NOTE_TEXT_LOCATOR)
        value2 = self.find_element_then_get_text(NOTE_TEXT_LOCATOR2)
        return value1, value2
