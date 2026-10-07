# pages/DeviceInformationPage.py

from selenium.webdriver.common.by import By

from webui.pages.BasePage import BasePage
from webui.utils.generate_screenshot_name import generate_screenshot_name


# Page Object Model
class DeviceInformationPage(BasePage):
    # Page element locators
    # device type
    DEVICE_TYPE_TITLE_LOCATE = (By.XPATH, "/html/body/div[1]/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[1]/td[1]/span")
    DEVICE_TYPE_LOCATE = (By.XPATH, "/html/body/div[1]/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[1]/td[2]/span")
    # system time
    SYSTEM_TIME_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[1]/td[3]/span")
    SYSTEM_TIME_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[1]/td[4]/span")
    # system name
    SYSTEM_NAME_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[2]/td[1]/span")
    SYSTEM_NAME_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[2]/td[2]/span")
    # system uptime
    SYSTEM_UP_TIME_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[2]/td[3]/span")
    SYSTEM_UP_TIME_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[2]/td[4]/span")
    # system location
    SYSTEM_LOCATION_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[3]/td[1]/span")
    SYSTEM_LOCATION_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[3]/td[2]/span")
    # mac address
    MAC_ADDRESS_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[3]/td[3]/span")
    MAC_ADDRESS_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[3]/td[4]/span")
    # system contact
    SYSTEM_CONTACT_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[4]/td[1]/span")
    SYSTEM_CONTACT_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[4]/td[2]/span")
    # ip address
    IP_ADDRESS_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[4]/td[3]/span")
    IP_ADDRESS_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[4]/td[4]/span")
    # boot version
    BOOT_VERSION_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[5]/td[1]/span")
    BOOT_VERSION_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[5]/td[2]/span")
    # subnet mask
    SUBNET_MASK_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[5]/td[3]/span")
    SUBNET_MASK_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[5]/td[4]/span")
    # firmware version
    FIRMWARE_VERSION_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[6]/td[1]/span")
    FIRMWARE_VERSION_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[6]/td[2]/span")
    # hardware version
    HARDWARE_VERSION_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[6]/td[3]/span")
    HARDWARE_VERSION_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[6]/td[4]/span")
    # default gateway
    DEFAULT_GATEWAY_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[7]/td[1]/span")
    DEFAULT_GATEWAY_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[7]/td[2]/span")
    # serial number
    SERIAL_NUMBER_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[7]/td[3]/span")
    SERIAL_NUMBER_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[7]/td[4]/span")
    # login timeout
    LOGIN_TIMEOUT_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[8]/td[1]/span")
    LOGIN_TIMEOUT_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[1]/fieldset/table/tr[8]/td[2]/span")
    # stp
    STP_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[1]/td[1]/span")
    STP_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[1]/td[2]/span")
    # snmp status
    SNMP_STATUS_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[1]/td[3]/span")
    SNMP_STATUS_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[1]/td[4]/span")
    # port mirroring
    PORT_MIRRORING_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[2]/td[1]/span")
    PORT_MIRRORING_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[2]/td[2]/span")
    # 802.1x status
    DOT1X_STATUS_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[2]/td[3]/span")
    DOT1X_STATUS_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[2]/td[4]/span")
    # igmp snooping
    IGMP_SNOOPING_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[3]/td[1]/span")
    IGMP_SNOOPING_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[3]/td[2]/span")
    # safeguard engine
    SAFEGUARD_ENGINE_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[3]/td[3]/span")
    SAFEGUARD_ENGINE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[3]/td[4]/span")
    # dhcp client
    DHCP_CLIENT_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[4]/td[1]/span")
    DHCP_CLIENT_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[4]/td[2]/span")
    # jumbo frame
    JUMBO_FRAME_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[4]/td[3]/span")
    JUMBO_FRAME_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[4]/td[4]/span")
    # power saving
    POWER_SAVING_TITLE_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[5]/td[1]/span")
    POWER_SAVING_LOCATE = (By.XPATH, "/html/body/div/div/div/section/div/div/div[2]/div[2]/fieldset/table/tr[5]/td[2]/span")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = f"{base_url}"

    def get_title_and_value_from_locators(self, title_locator, value_locator):
        """
        return value form locators
        :param title_locator:
        :param value_locator:
        :return:
        """
        title_text = self.driver.find_element(*title_locator)

        value_text = self.driver.find_element(*value_locator)

        return title_text.text, value_text.text

    def get_device_type(self):
        title_text = self.find_element_then_get_text(self.DEVICE_TYPE_TITLE_LOCATE)

        device_type_text = self.find_element_then_get_text(self.DEVICE_TYPE_LOCATE)

        self.take_screenshot(generate_screenshot_name("get_device_type"))

        return title_text, device_type_text

    def get_system_time(self):
        system_time_title_text = self.find_element_then_get_text(self.SYSTEM_TIME_TITLE_LOCATE)

        system_time_text = self.find_element_then_get_text(self.SYSTEM_TIME_LOCATE)

        return system_time_title_text, system_time_text

    def get_system_name(self):
        return self.get_title_and_value_from_locators(self.SYSTEM_NAME_TITLE_LOCATE, self.SYSTEM_NAME_LOCATE)

    def get_system_up_time(self):
        return self.get_title_and_value_from_locators(self.SYSTEM_UP_TIME_TITLE_LOCATE, self.SYSTEM_UP_TIME_LOCATE)

    def get_system_location(self):
        return self.get_title_and_value_from_locators(self.SYSTEM_LOCATION_TITLE_LOCATE, self.SYSTEM_LOCATION_LOCATE)

    def get_mac_address(self):
        return self.get_title_and_value_from_locators(self.MAC_ADDRESS_TITLE_LOCATE, self.MAC_ADDRESS_LOCATE)

    def get_system_contact(self):
        return self.get_title_and_value_from_locators(self.SYSTEM_CONTACT_TITLE_LOCATE, self.SYSTEM_CONTACT_LOCATE)

    def get_ip_address(self):
        return self.get_title_and_value_from_locators(self.IP_ADDRESS_TITLE_LOCATE, self.IP_ADDRESS_LOCATE)

    def get_boot_version(self):
        return self.get_title_and_value_from_locators(self.BOOT_VERSION_TITLE_LOCATE, self.BOOT_VERSION_LOCATE)

    def get_subnet_mask(self):
        return self.get_title_and_value_from_locators(self.SUBNET_MASK_TITLE_LOCATE, self.SUBNET_MASK_LOCATE)

    def get_firmware_version(self):
        return self.get_title_and_value_from_locators(self.FIRMWARE_VERSION_TITLE_LOCATE, self.FIRMWARE_VERSION_LOCATE)

    def get_hardware_version(self):
        return self.get_title_and_value_from_locators(self.HARDWARE_VERSION_TITLE_LOCATE, self.HARDWARE_VERSION_LOCATE)

    def get_default_gateway(self):
        return self.get_title_and_value_from_locators(self.DEFAULT_GATEWAY_TITLE_LOCATE, self.DEFAULT_GATEWAY_LOCATE)

    def get_serial_number(self):
        return self.get_title_and_value_from_locators(self.SERIAL_NUMBER_TITLE_LOCATE, self.SERIAL_NUMBER_LOCATE)

    def get_login_timeout(self):
        return self.get_title_and_value_from_locators(self.LOGIN_TIMEOUT_TITLE_LOCATE, self.LOGIN_TIMEOUT_LOCATE)

    def get_stp(self):
        return self.get_title_and_value_from_locators(self.STP_TITLE_LOCATE, self.STP_LOCATE)

    def get_snmp_status(self):
        return self.get_title_and_value_from_locators(self.SNMP_STATUS_TITLE_LOCATE, self.SNMP_STATUS_LOCATE)

    def get_port_mirroring(self):
        return self.get_title_and_value_from_locators(self.PORT_MIRRORING_TITLE_LOCATE, self.PORT_MIRRORING_LOCATE)

    def get_dot1x_status(self):
        return self.get_title_and_value_from_locators(self.DOT1X_STATUS_TITLE_LOCATE, self.DOT1X_STATUS_LOCATE)

    def get_igmp_snooping(self):
        return self.get_title_and_value_from_locators(self.IGMP_SNOOPING_TITLE_LOCATE, self.IGMP_SNOOPING_LOCATE)

    def get_safeguard_engine(self):
        return self.get_title_and_value_from_locators(self.SAFEGUARD_ENGINE_TITLE_LOCATE, self.SAFEGUARD_ENGINE_LOCATE)

    def get_dhcp_client(self):
        return self.get_title_and_value_from_locators(self.DHCP_CLIENT_TITLE_LOCATE, self.DHCP_CLIENT_LOCATE)

    def get_jumbo_frame(self):
        return self.get_title_and_value_from_locators(self.JUMBO_FRAME_TITLE_LOCATE, self.JUMBO_FRAME_LOCATE)

    def get_power_saving(self):
        return self.get_title_and_value_from_locators(self.POWER_SAVING_TITLE_LOCATE, self.POWER_SAVING_LOCATE)
