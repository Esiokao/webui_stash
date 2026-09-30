# pages/SystemSettingsPage.py
import time

from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage


class SystemSettingsPage(BasePage):
    SYSTEM_MENU_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/div/div/div/div/ul/div[2]/li/div/i")

    SYSTEM_SETTINGS_MENU_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/div/div/div/div/ul/div[2]/li/ul/div[1]/a")

    IP_INFORMATION_CONFIG_OPTION_ONE_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[2]/td/div/span[1]/label")

    IP_INFORMATION_CONFIG_OPTION_TWO_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[2]/td/div/span[2]/label")

    IP_CONFIG_PARENT_DIV_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[2]/td/div")

    INTERFACE_NAME_TITLE_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[3]/td[1]/span")

    INTERFACE_NAME_INPUT_LOCATOR = (
        By.ID, "InterfaceName"
    )

    VLAN_NAME_TITLE_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[4]/td[1]/span"
    )

    VLAN_NAME_INPUT_LOCATOR = (
        By.ID, "VlanName"
    )

    IP_ADDRESS_TITLE_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[5]/td[1]/span"
    )

    IP_ADDRESS_OCTET_ONE_INPUT_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[5]/td[2]/div/span/input[1]"
    )

    IP_ADDRESS_OCTET_TWO_INPUT_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[5]/td[2]/div/span/input[2]"
    )

    IP_ADDRESS_OCTET_THREE_INPUT_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[5]/td[2]/div/span/input[3]"
    )

    IP_ADDRESS_OCTET_FOUR_INPUT_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[5]/td[2]/div/span/input[4]"
    )

    SUBNET_MASK_TITLE_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[6]/td[1]/span"
    )

    SUBNET_MASK_OCTET_ONE_INPUT_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[6]/td[2]/div/span/input[1]"
    )

    SUBNET_MASK_OCTET_TWO_INPUT_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[6]/td[2]/div/span/input[2]"
    )

    SUBNET_MASK_OCTET_THREE_INPUT_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[6]/td[2]/div/span/input[3]"
    )

    SUBNET_MASK_OCTET_FOUR_INPUT_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[6]/td[2]/div/span/input[4]"
    )

    GATEWAY_TITLE_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[7]/td[1]/span"
    )

    GATEWAY_OCTET_ONE_INPUT_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[7]/td[2]/div/span/input[1]"
    )

    GATEWAY_OCTET_TWO_INPUT_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[7]/td[2]/div/span/input[2]"
    )

    GATEWAY_OCTET_THREE_INPUT_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[7]/td[2]/div/span/input[3]"
    )

    GATEWAY_OCTET_FOUR_INPUT_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[7]/td[2]/div/span/input[4]"
    )

    DHCP_OPTION_12_STATE_TITLE_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[8]/td[1]/span"
    )

    DHCP_OPTION_12_STATE_SELECT_BOX_LOCATOR = (
        By.ID, "DHCPOption12State"
    )

    DHCP_OPTION_12_STATE_HOST_NAME_TITLE_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[1]/tr[9]/td[1]/span"
    )

    DHCP_OPTION_12_STATE_HOST_NAME_INPUT_LOCATOR = (
        By.ID, "DHCPOption12HostName"
    )

    DHCP_OPTION_77_TITLE_LOCATOR = (
        By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/fieldset/table[2]/tr[1]/td[1]/span"
    )

    DHCP_OPTION_77_INPUT_LOCATOR = (
        By.ID, "DhcpOption77"
    )

    DHCP_OPTION_77_TABLE_TITLE_LOCATOR = (
        By.CLASS_NAME, "has-gutter"
    )

    DHCP_OPTION_77_TABLE_LOCATOR = (
        By.CLASS_NAME, "table"
    )

    SYSTEM_NAME_TITLE_LOCATOR = (
    By.XPATH, "/html/body/div/div/div/section/div/div/div[3]/fieldset/table/tr[1]/td[1]/span")

    SYSTEM_NAME_INPUT_LOCATOR = (By.ID, "SystemName")

    SYSTEM_LOCATION_TITLE_LOCATOR = (
    By.XPATH, "/html/body/div/div/div/section/div/div/div[3]/fieldset/table/tr[2]/td[1]/span")

    SYSTEM_LOCATION_INPUT_LOCATOR = (By.ID, "SystemLocation")

    SYSTEM_CONTACT_TITLE_LOCATOR = (

    By.XPATH, "/html/body/div/div/div/section/div/div/div[3]/fieldset/table/tr[3]/td[1]/span")
    SYSTEM_CONTACT_INPUT_LOCATOR = (By.ID, "SystemContact")

    LOGIN_TIMEOUT_TITLE_LOCATOR = (
    By.XPATH, "/html/body/div/div/div/section/div/div/div[3]/fieldset/table/tr[4]/td[1]/span")

    LOGIN_TIMEOUT_INPUT_LOCATOR = (By.ID, "LoginTimeout")

    def __init__(self, driver, base_url):
        """
        初始化 SystemSettingsPage
        :param driver: WebDriver instance
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False

    def collapse_system_menu_then_click_system_settings(self):
        self.click_element_by_js(self.SYSTEM_MENU_LOCATOR)
        self.click_element_by_js(self.SYSTEM_SETTINGS_MENU_LOCATOR)

    def get_ip_config_option_one_text(self):
        return self.find_element_then_get_text(self.IP_INFORMATION_CONFIG_OPTION_ONE_LOCATOR)

    def get_ip_config_option_two_text(self):
        return self.find_element_then_get_text(self.IP_INFORMATION_CONFIG_OPTION_TWO_LOCATOR)

    def get_selected_ip_config_mode(self):
        target_div = self.find_element_if_present(self.IP_CONFIG_PARENT_DIV_LOCATOR)
        selected_input = self.find_checked_radio_within(target_div)
        text = self.find_selected_input_label_text(selected_input)
        return text

    def get_interface_name_title_and_value(self):
        # retrieve title text
        title = self.find_element_then_get_text(self.INTERFACE_NAME_TITLE_LOCATOR)
        value = self.find_input_value(self.INTERFACE_NAME_INPUT_LOCATOR)
        return title, value

    def get_vlan_name_title_and_value(self):
        # retrieve vlan name
        title = self.find_element_then_get_text(self.VLAN_NAME_TITLE_LOCATOR)
        value = self.find_input_value(self.VLAN_NAME_INPUT_LOCATOR)
        return title, value

    def get_ip_address_title_and_value(self):
        """Retrieve the IP address title and value."""
        title = self.find_element_then_get_text(self.IP_ADDRESS_TITLE_LOCATOR)

        ip_octets = [
            self.find_input_value(locator)
            for locator in [
                self.IP_ADDRESS_OCTET_ONE_INPUT_LOCATOR,
                self.IP_ADDRESS_OCTET_TWO_INPUT_LOCATOR,
                self.IP_ADDRESS_OCTET_THREE_INPUT_LOCATOR,
                self.IP_ADDRESS_OCTET_FOUR_INPUT_LOCATOR,
            ]
        ]

        ip_addr = ".".join(ip_octets)
        return title, ip_addr

    # Subnet Mask

    def get_subnet_mask_title_and_value(self):
        """Retrieve the subnet mask title and value."""
        title = self.find_element_then_get_text(self.SUBNET_MASK_TITLE_LOCATOR)

        subnet_octets = [
            self.find_input_value(locator)
            for locator in [
                self.SUBNET_MASK_OCTET_ONE_INPUT_LOCATOR,
                self.SUBNET_MASK_OCTET_TWO_INPUT_LOCATOR,
                self.SUBNET_MASK_OCTET_THREE_INPUT_LOCATOR,
                self.SUBNET_MASK_OCTET_FOUR_INPUT_LOCATOR,
            ]
        ]

        subnet_mask = ".".join(subnet_octets)
        return title, subnet_mask

    def get_gateway_title_and_value(self):
        """Retrieve the gateway title and value."""
        title = self.find_element_then_get_text(self.GATEWAY_TITLE_LOCATOR)

        gateway_octets = [
            self.find_input_value(locator)
            for locator in [
                self.GATEWAY_OCTET_ONE_INPUT_LOCATOR,
                self.GATEWAY_OCTET_TWO_INPUT_LOCATOR,
                self.GATEWAY_OCTET_THREE_INPUT_LOCATOR,
                self.GATEWAY_OCTET_FOUR_INPUT_LOCATOR,
            ]
        ]

        gateway = ".".join(gateway_octets)
        return title, gateway

    # D12
    def get_dhcp_option_12_state_title_and_value(self):
        title = self.find_element_then_get_text(self.DHCP_OPTION_12_STATE_TITLE_LOCATOR)
        value = self.find_selected_value_within(self.DHCP_OPTION_12_STATE_SELECT_BOX_LOCATOR)

        return title, value

    # Dhcp Option 77 table
    def get_dhcp_option_77_title_and_value(self):
        title = self.find_element_then_get_text(self.DHCP_OPTION_77_TITLE_LOCATOR)
        value = self.find_input_value(self.DHCP_OPTION_77_INPUT_LOCATOR)

        return title, value

    def get_dhcp_option_77_table_title_columns(self):
        cells_class_name = "cell"
        return self.find_cells_value_within(self.DHCP_OPTION_77_TABLE_TITLE_LOCATOR, cells_class_name)

    def check_if_dhcp_option_77_table_is_empty(self):
        empty_message = "< < Table is empty > >"
        return self.text_is_existed_within(self.DHCP_OPTION_77_TABLE_LOCATOR, empty_message)

    # System Name
    def get_system_name_title_and_value(self):
        title = self.find_element_then_get_text(self.SYSTEM_NAME_TITLE_LOCATOR)
        value = self.find_input_value(self.SYSTEM_NAME_INPUT_LOCATOR)
        return title, value

    # System Location
    def get_system_location_title_and_value(self):
        title = self.find_element_then_get_text(self.SYSTEM_LOCATION_TITLE_LOCATOR)
        value = self.find_input_value(self.SYSTEM_LOCATION_INPUT_LOCATOR)
        return title, value

    # System Contact
    def get_system_contact_title_and_value(self):
        title = self.find_element_then_get_text(self.SYSTEM_CONTACT_TITLE_LOCATOR)
        value = self.find_input_value(self.SYSTEM_CONTACT_INPUT_LOCATOR)
        return title, value

    # Login Timeout
    def get_login_timeout_title_and_value(self):
        title = self.find_element_then_get_text(self.LOGIN_TIMEOUT_TITLE_LOCATOR)
        value = self.find_input_value(self.LOGIN_TIMEOUT_INPUT_LOCATOR)
        return title, value


