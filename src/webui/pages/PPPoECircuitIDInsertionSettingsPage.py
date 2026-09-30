# pages/PPPoECircuitIDInsertionSettingsPage.py
from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class PPPoECircuitIDInsertionSettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 PPPoECircuitIDInsertionSettingsPage
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
        PPPOE_CIRCUIT_ID_INSERTION_SETTINGS_MENU_LOCATOR = (By.CSS_SELECTOR, ".is-opened > .el-menu > .menu-wrapper:nth-child(15) span")

        self.find_element_if_present(system_menu_locator).click()
        self.find_element_if_present(PPPOE_CIRCUIT_ID_INSERTION_SETTINGS_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        page_header_locator = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")

        return self.find_element_then_get_text(page_header_locator)
    
    def get_pppoe_circuit_id_insertion_settings_tier2_header_text(self):
        pppoe_circuit_id_insertion_settings_tier2_header_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(pppoe_circuit_id_insertion_settings_tier2_header_locator)
    
    def get_pppoe_circuit_id_insertion_state_title_text(self):
        pppoe_circuit_id_insertion_state_title_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td > span")
        return self.find_element_then_get_text(pppoe_circuit_id_insertion_state_title_locator)
    
    def get_pppoe_circuit_id_insertion_state_option_one_text(self):
        pppoe_circuit_id_insertion_state_option_one_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span > label")
        return self.find_element_then_get_text(pppoe_circuit_id_insertion_state_option_one_locator)
    
    def get_pppoe_circuit_id_insertion_state_option_two_text(self):
        pppoe_circuit_id_insertion_state_option_two_locator = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div > span:nth-child(2) > label")
        return self.find_element_then_get_text(pppoe_circuit_id_insertion_state_option_two_locator)
    
    def get_checked_pppoe_circuit_id_insertion_state_option(self):
        pppoe_circuit_id_insertion_state_option_div = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td:nth-child(2) > div")
        target_div = self.find_element_if_present(pppoe_circuit_id_insertion_state_option_div)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)
        return text
    
    def get_pppoe_circuit_id_insertion_state_button_text(self):
        pppoe_circuit_id_insertion_state_button_locator = (By.XPATH, "/html/body/div[1]/div/div/section/div/div/div[2]/fieldset/table/tr/td[3]/input")
        return self.find_input_value(pppoe_circuit_id_insertion_state_button_locator)
    
    def get_pppoe_circuit_id_insertion_port_header_text(self):
        pppoe_circuit_id_insertion_port_header_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > legend")
        return self.find_element_then_get_text(pppoe_circuit_id_insertion_port_header_locator)
    
    def get_from_port_title_and_value(self):
        from_port_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td")
        from_port_value_locator = (By.CSS_SELECTOR, "#fromPort")
        title = self.find_element_then_get_text(from_port_title_locator)
        value = self.find_selected_value_within(from_port_value_locator)
        return title, value

    def get_to_port_title_and_value(self):
        to_port_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td:nth-child(2)")
        to_port_value_locator = (By.CSS_SELECTOR, "#toPort")
        title = self.find_element_then_get_text(to_port_title_locator)
        value = self.find_selected_value_within(to_port_value_locator)
        return title, value
    
    def get_state_title_and_value(self):
        state_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr > td:nth-child(3)")
        state_value_locator = (By.CSS_SELECTOR, "#State")
        title = self.find_element_then_get_text(state_title_locator)
        value = self.find_selected_value_within(state_value_locator)
        return title, value
    
    def get_circuit_id_title_and_value(self):
        circuit_id_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr:nth-child(3) > td")
        circuit_id_value_locator = (By.CSS_SELECTOR, "#CircuitID")
        circuit_id_value_locator2 = (By.CSS_SELECTOR, "#circuitIdInput")
        title = self.find_element_then_get_text(circuit_id_title_locator)
        value1 = self.find_selected_value_within(circuit_id_value_locator)
        value2 = self.find_input_value(circuit_id_value_locator2)
        return title, value1, value2

    def get_remote_id_title_and_value(self):
        remote_id_title_locator = (By.CSS_SELECTOR, "div:nth-child(3) > fieldset > table > tr:nth-child(3) > td:nth-child(2)")
        remote_id_value_locator = (By.CSS_SELECTOR, "#RemoteID")
        remote_id_value_locator2 = (By.CSS_SELECTOR, "#remoteIdInput")
        title = self.find_element_then_get_text(remote_id_title_locator)
        value1 = self.find_selected_value_within(remote_id_value_locator)
        value2 = self.find_input_value(remote_id_value_locator2)
        return title, value1, value2

    def get_pppoe_circuit_id_insertion_port_settings_button_text(self):
        pppoe_circuit_id_insertion_port_settings_button_locator = (By.XPATH, "/html/body/div[1]/div/div/section/div/div/div[3]/fieldset/table/tr[5]/td/input")
        return self.find_input_value(pppoe_circuit_id_insertion_port_settings_button_locator)

    def get_table_title(self):
        table_title_locator = (By.CSS_SELECTOR, ".has-gutter")
        cells_class_name = "cell"
        return self.find_cells_value_within(table_title_locator, cells_class_name)

    def get_table_value(self):
        table_value_locator = (By.CSS_SELECTOR, ".el-table__row")
        cells_class_name = "cell"
        return self.find_cells_value_within(table_value_locator, cells_class_name)

