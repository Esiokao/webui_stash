# pages/PingTestPage.py
from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class PingTestPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 PingTestPage
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
        PING_TEST_menu_locator = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(19) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(PING_TEST_menu_locator).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div.sx-title1")

        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)
    
    def get_ping_test_tier2_header_text(self):
        PING_TEST_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")

        return self.find_element_then_get_text(PING_TEST_TIER2_HEADER_LOCATOR)
    
    def get_target_ip_address_title_and_v4_value_v6_value(self):
        title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        ipv6_locator = (By.CSS_SELECTOR, "#IPv6 > input")
        title = self.find_element_then_get_text(title_locator)
        ipv6_addr = self.find_input_value(ipv6_locator)
        ipv4_octets = [
            self.find_input_value(locator)
            for locator in [
                (By.CSS_SELECTOR, "#IPv4 > span > input[type=text]:nth-child(1)"),
                (By.CSS_SELECTOR, "#IPv4 > span > input[type=text]:nth-child(3)"),
                (By.CSS_SELECTOR, "#IPv4 > span > input[type=text]:nth-child(5)"),
                (By.CSS_SELECTOR, "#IPv4 > span > input[type=text]:nth-child(7)"),
            ]
        ]

        ipv4_addr = ".".join(ipv4_octets)

        return title, ipv4_addr, ipv6_addr
    
    def get_v4_mode_option_text(self):
        v4_mode_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2)")

        return self.find_element_then_get_text(v4_mode_locator)

    def get_v6_mode_option_text(self):
        v6_mode_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td:nth-child(2)")

        return self.find_element_then_get_text(v6_mode_locator)
        
    def get_checked_v4_mode_option(self):
        v4_mode_locator = (By.CSS_SELECTOR, "#IPv4Radio")

        return self.find_checkbox_checked(v4_mode_locator)

    def get_checked_v6_mode_option(self):
        v6_mode_locator = (By.CSS_SELECTOR, "#IPv6Radio")

        return self.find_checkbox_checked(v6_mode_locator)
    
    def get_repeat_pinging_for_title(self):
        title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td > span")

        return self.find_element_then_get_text(title_locator)
    
    def get_repeat_pinging_for_options1_and_text(self):
        REPEAT_PINGING_FOR_options1_locator = (By.XPATH, "/html/body/div[1]/div/div/section/div/div/div[2]/fieldset/table/tr[3]/td[2]")
        REPEAT_PINGING_FOR_options1_value_locator = (By.CSS_SELECTOR, "#timeRadio1")
        td_element = self.find_element_if_visible(REPEAT_PINGING_FOR_options1_locator)
        if td_element:
            title = self.driver.execute_script("""
                var td = arguments[0];
                var text = "";
                for (var i = 0; i < td.childNodes.length; i++) {
                    if (td.childNodes[i].nodeType === Node.TEXT_NODE) {
                        text += td.childNodes[i].textContent;
                    }
                }
                return text.trim();
            """, td_element)
        else:
            title = None
        value = self.find_checkbox_checked(REPEAT_PINGING_FOR_options1_value_locator)

        return value, title
    
    def get_repeat_pinging_for_options2_and_value(self):
        REPEAT_PINGING_FOR_options2_locator = (By.CSS_SELECTOR, "#timeRadio2")
        REPEAT_PINGING_FOR_options2_value_locator = (By.CSS_SELECTOR, "#times")

        title = self.find_checkbox_checked(REPEAT_PINGING_FOR_options2_locator)
        value = self.find_input_value(REPEAT_PINGING_FOR_options2_value_locator)

        return title, value

    def get_timeout_title_and_value(self):
        timeout_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(5) > td > span")
        timeout_value_locator = (By.CSS_SELECTOR, "#Timeout")

        title = self.find_element_then_get_text(timeout_locator)
        value = self.find_input_value(timeout_value_locator)

        return title, value

    def get_button_text(self):
        BUTTON_TEXT_LOCATOR = (By.CSS_SELECTOR, "#Start")

        return self.find_input_value(BUTTON_TEXT_LOCATOR)

