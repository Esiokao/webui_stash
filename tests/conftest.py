# conftest.py
import sys
from dotenv import load_dotenv
import os

load_dotenv("Settings.env")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest


@pytest.fixture(scope="session")
def config():
    """Global test configuration"""
    return {
        "base_url": os.getenv("TEST_BASE_URL", "http://10.90.90.90"),
        "implicit_wait": int(os.getenv("TEST_IMPLICIT_WAIT", "10")),
        "screenshot_dir": "screenshots",
        "model_name": "DGS-1210-10XS",
        "screen_width": "1920",
        "screen_height": "1080",
        "device_information": {
            "device_type": {
                "type": "string",
                "title": "Device Type",
                # "expected_value": "DGS-1210-52X/ME Management Switch"
                "expected_value": os.getenv("DEVICE_TYPE"),
            },
            "system_time": {"type": "regexp", "title": "System Time", "expected_value": r"(\d{2}):(\d{2}):(\d{2}) (\d{2}) (\d{2}) (\d{4})"},
            "system_name": {
                "type": "string",
                "title": "System Name",
                # "expected_value": "DGS-1210-52X/ME"
                "expected_value": os.getenv("SYSTEM_NAME"),
            },
            "system_up_time": {
                "type": "regexp",
                "title": "System Up Time",
                "expected_value": r"^(\d+)\s*days,\s*(\d{0,2})\s*hours,\s*(\d{0,2})\s*mins,\s*(\d{0,2})\s*seconds$",
            },
            "system_location": {"type": "string", "title": "System Location", "expected_value": ""},
            "mac_address": {"type": "regexp", "title": "MAC Address", "expected_value": r"^([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}$"},
            "system_contact": {"type": "string", "title": "System Contact", "expected_value": ""},
            "ip_address": {"type": "string", "title": "IP Address", "expected_value": os.getenv("SWITCH_IP_ADDRESS")},
            "boot_version": {"type": "string", "title": "Boot Version", "expected_value": os.getenv("BOOT_VERSION", "1.00.006")},
            "subnet_mask": {"type": "string", "title": "Subnet Mask", "expected_value": os.getenv("SUBNET_MASK", "255.0.0.0")},
            "firmware_version": {"type": "string", "title": "Firmware Version", "expected_value": os.getenv("FIRMWARE_VERSION")},
            "hardware_version": {"type": "string", "title": "Hardware Version", "expected_value": os.getenv("HARDWARE_VERSION")},
            "default_gateway": {"type": "string", "title": "Default Gateway", "expected_value": "0.0.0.0"},
            "serial_number": {"type": "string", "title": "Serial Number", "expected_value": os.getenv("SERIAL_NUMBER", "QQDMS12345600")},
            "login_timeout": {"type": "string", "title": " Login Timeout  (minutes)", "expected_value": os.getenv("LOGIN_TIMEOUT", "3")},
            "stp": {"type": "string", "title": "STP", "expected_value": "Disabled"},
            "snmp_status": {"type": "string", "title": "SNMP Status", "expected_value": "Disabled"},
            "port_mirroring": {"type": "string", "title": "Port Mirroring", "expected_value": "Disabled"},
            "dot1x_status": {"type": "string", "title": "802.1X Status", "expected_value": "Disabled"},
            "igmp_snooping": {"type": "string", "title": "IGMP Snooping", "expected_value": "Disabled"},
            "safeguard_engine": {"type": "string", "title": "Safeguard Engine", "expected_value": " Enabled"},
            "dhcp_client": {"type": "string", "title": "DHCP Client", "expected_value": "Disabled"},
            "jumbo_frame": {"type": "string", "title": "Jumbo Frame", "expected_value": "Disabled"},
            "power_saving": {"type": "string", "title": "Power Saving", "expected_value": "Disabled"},
        },
        "username": "admin",  # login username
        "password": "admin",  # login password
    }


# pytest hooks
def pytest_runtest_setup(item):
    if "reboot_required" in item.keywords:
        from webui.pages.LoginPage import LoginPage

        LoginPage.set_login_status(False)


# serial port env
@pytest.fixture(scope="session")
def serial_env():
    """Serial Port Environment"""
    from webui.command.serial_env import SerialEnv

    com_port = os.getenv("COM_PORT", "COM3")
    baud_rate = int(os.getenv("BAUD_RATE", "115200"))

    print("\n\n initializing serial env")

    serial_env = SerialEnv.SerialEnv(baudrate=baud_rate, port=com_port, use_mock=False)

    yield serial_env

    if serial_env.running:
        serial_env.close()

    print("\n\n tearing down serial env")


@pytest.fixture(scope="session")
def driver(config):
    """WebDriver fixture for test"""

    # printing information to console

    print("\n\n initializing webdriver")

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    driver.set_window_size(config["screen_width"], config["screen_height"])
    driver.implicitly_wait(config["implicit_wait"])

    yield driver

    # printing tear down information to console

    print("\n\n tearing down webdriver")

    driver.quit()


@pytest.fixture(scope="class")
def login_page(driver, config):
    """Login page fixture"""
    print("\n\n initializing login page")

    from webui.pages.LoginPage import LoginPage

    yield LoginPage(driver, config["base_url"])

    print("\n\n tearing down login page")


@pytest.fixture(scope="class")
def logged_driver(driver, config, request):
    from webui.pages.LoginPage import LoginPage

    print("\n\n initializing logged_driver")

    login_page = LoginPage(driver, config["base_url"])
    login_page.do_login(config["username"], config["password"])

    yield driver
    print("\n\n tearing down logged_driver")


@pytest.fixture(scope="class")
def device_information_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing device info page")
    from webui.pages.DeviceInformationPage import DeviceInformationPage

    yield DeviceInformationPage(logged_driver, config["base_url"])
    print("\n\n tearing down device info page")


@pytest.fixture(scope="class")
def system_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing system settings page")
    from webui.pages.SystemSettingsPage import SystemSettingsPage

    __system_setting_page = SystemSettingsPage(logged_driver, config["base_url"])
    __system_setting_page.collapse_system_menu_then_click_system_settings()
    yield __system_setting_page
    print("\n\n tearing down system settings page")


# 4
@pytest.fixture(scope="class")
def firmware_information_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing firmware information page")
    from webui.pages.FirmwareInformationPage import FirmwareInformationPage

    __firmware_information_page = FirmwareInformationPage(logged_driver, config["base_url"])
    yield __firmware_information_page
    print("\n\n tearing down firmware information page")


# 5
@pytest.fixture(scope="class")
def serial_port_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing serial port settings page")
    from webui.pages.SerialPortSettingsPage import SerialPortSettingsPage

    __page = SerialPortSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down serial port settings page")


# 6
@pytest.fixture(scope="class")
def ip_interface_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing ip_interface_page")
    from webui.pages.IPInterfacePage import IPInterfacePage

    __page = IPInterfacePage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down ip_interface_page")


# 7
@pytest.fixture(scope="class")
def ipv6_system_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing ipv6_system_settings_page")
    from webui.pages.IPv6SystemSettingsPage import IPv6SystemSettingsPage

    __page = IPv6SystemSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down ipv6_system_settings_page")


# 8
@pytest.fixture(scope="class")
def access_profile_list_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing access_profile_list_page")
    from webui.pages.AccessProfileListPage import AccessProfileListPage

    __page = AccessProfileListPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down access_profile_list_page")


# 9
@pytest.fixture(scope="class")
def ipv6_neighbor_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing ipv6_neighbor_settings_page")
    from webui.pages.IPv6NeighborSettingsPage import IPv6NeighborSettingsPage

    __page = IPv6NeighborSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down ipv6_neighbor_settings_page")


# 10
@pytest.fixture(scope="class")
def dhcp_auto_configuration_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing dhcp_auto_configuration_page")
    from webui.pages.DHCPAutoConfigurationPage import DHCPAutoConfigurationPage

    __page = DHCPAutoConfigurationPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down dhcp_auto_configuration_page")


# 11
@pytest.fixture(scope="class")
def dhcp_auto_image_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing dhcp_auto_image_page")
    from webui.pages.DHCPAutoImagePage import DHCPAutoImagePage

    __page = DHCPAutoImagePage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down dhcp_auto_image_page")


# 12
@pytest.fixture(scope="class")
def peripheral_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing peripheral_settings_page")
    from webui.pages.PeripheralSettingsPage import PeripheralSettingsPage

    __page = PeripheralSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down peripheral_settings_page")


# 13
@pytest.fixture(scope="class")
def port_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing port_settings_page")
    from webui.pages.PortSettingsPage import PortSettingsPage

    __page = PortSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down port_settings_page")


# 14
@pytest.fixture(scope="class")
def port_description_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing port_description_page")
    from webui.pages.PortDescriptionPage import PortDescriptionPage

    __page = PortDescriptionPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down port_description_page")


# 15
@pytest.fixture(scope="class")
def port_error_disabled_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing port_error_disabled_page")
    from webui.pages.PortErrorDisabledPage import PortErrorDisabledPage

    __page = PortErrorDisabledPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down port_error_disabled_page")


# 16
@pytest.fixture(scope="class")
def port_media_type_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing port_media_type_page")
    from webui.pages.PortMediaTypePage import PortMediaTypePage

    __page = PortMediaTypePage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down port_media_type_page")


# 17
@pytest.fixture(scope="class")
def snmp_global_state_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing snmp_global_state_settings_page")
    from webui.pages.SNMPGlobalStateSettingsPage import SNMPGlobalStateSettingsPage

    __page = SNMPGlobalStateSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down snmp_global_state_settings_page")


# 18
@pytest.fixture(scope="class")
def snmp_user_table_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing snmp_user_table_page")
    from webui.pages.SNMPUserTablePage import SNMPUserTablePage

    __page = SNMPUserTablePage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down snmp_user_table_page")


# 19
@pytest.fixture(scope="class")
def snmp_group_table_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing snmp_group_table_page")
    from webui.pages.SNMPGroupTablePage import SNMPGroupTablePage

    __page = SNMPGroupTablePage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down snmp_group_table_page")


# 20
@pytest.fixture(scope="class")
def snmp_view_table_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing snmp_view_table_page")
    from webui.pages.SNMPViewTablePage import SNMPViewTablePage

    __page = SNMPViewTablePage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down snmp_view_table_page")


# 21
@pytest.fixture(scope="class")
def snmp_community_table_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing snmp_community_table_page")
    from webui.pages.SNMPCommunityTablePage import SNMPCommunityTablePage

    __page = SNMPCommunityTablePage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down snmp_community_table_page")


# 22
@pytest.fixture(scope="class")
def snmp_host_table_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing snmp_host_table_page")
    from webui.pages.SNMPHostTablePage import SNMPHostTablePage

    __page = SNMPHostTablePage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down snmp_host_table_page")


# 23
@pytest.fixture(scope="class")
def snmp_engine_id_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing snmp_engine_id_page")
    from webui.pages.SNMPEngineIDPage import SNMPEngineIDPage

    __page = SNMPEngineIDPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down snmp_engine_id_page")


# 24
@pytest.fixture(scope="class")
def snmp_trap_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing snmp_trap_settings_page")
    from webui.pages.SNMPTrapSettingsPage import SNMPTrapSettingsPage

    __page = SNMPTrapSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down snmp_trap_settings_page")


# 25
@pytest.fixture(scope="class")
def user_accounts_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing user_accounts_page")
    from webui.pages.UserAccountsPage import UserAccountsPage

    __page = UserAccountsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down user_accounts_page")


# 26
@pytest.fixture(scope="class")
def mac_address_aging_time_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing mac_address_aging_time_page")
    from webui.pages.MACAddressAgingTimePage import MACAddressAgingTimePage

    __page = MACAddressAgingTimePage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down mac_address_aging_time_page")


# 27
@pytest.fixture(scope="class")
def arp_aging_time_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing arp_aging_time_settings_page")
    from webui.pages.ARPAgingTimeSettingsPage import ARPAgingTimeSettingsPage

    __page = ARPAgingTimeSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down arp_aging_time_settings_page")


# 28
@pytest.fixture(scope="class")
def pppoe_circuit_id_insertion_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing pppoe_circuit_id_insertion_settings_page")
    from webui.pages.PPPoECircuitIDInsertionSettingsPage import PPPoECircuitIDInsertionSettingsPage

    __page = PPPoECircuitIDInsertionSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down pppoe_circuit_id_insertion_settings_page")


# 29
@pytest.fixture(scope="class")
def web_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing web_settings_page")
    from webui.pages.WebSettingsPage import WebSettingsPage

    __page = WebSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down web_settings_page")


# 30
@pytest.fixture(scope="class")
def telnet_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing telnet_settings_page")
    from webui.pages.TelnetSettingsPage import TelnetSettingsPage

    __page = TelnetSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down telnet_settings_page")


# 31
@pytest.fixture(scope="class")
def password_encryption_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing password_encryption_page")
    from webui.pages.PasswordEncryptionPage import PasswordEncryptionPage

    __page = PasswordEncryptionPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down password_encryption_page")


# 32
@pytest.fixture(scope="class")
def ping_test_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing ping_test_page")
    from webui.pages.PingTestPage import PingTestPage

    __page = PingTestPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down ping_test_page")


# 33
@pytest.fixture(scope="class")
def mac_notification_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing mac_notification_settings_page")
    from webui.pages.MACNotificationSettingsPage import MACNotificationSettingsPage

    __page = MACNotificationSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down mac_notification_settings_page")


# 34
@pytest.fixture(scope="class")
def mac_flapping_detection_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing mac_flapping_detection_page")
    from webui.pages.MACFlappingDetectionPage import MACFlappingDetectionPage

    __page = MACFlappingDetectionPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down mac_flapping_detection_page")


# 35
@pytest.fixture(scope="class")
def twamp_server_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing twamp_server_page")
    from webui.pages.TwampServerPage import TwampServerPage

    __page = TwampServerPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down twamp_server_page")


# 36
@pytest.fixture(scope="class")
def system_log_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing system_log_settings_page")
    from webui.pages.SystemLogSettingsPage import SystemLogSettingsPage

    __page = SystemLogSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down system_log_settings_page")


# 37
@pytest.fixture(scope="class")
def system_log_server_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing system_log_server_page")
    from webui.pages.SystemLogServerPage import SystemLogServerPage

    __page = SystemLogServerPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down system_log_server_page")


# 38
@pytest.fixture(scope="class")
def time_profile_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing time_profile_page")
    from webui.pages.TimeProfilePage import TimeProfilePage

    __page = TimeProfilePage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down time_profile_page")


# 39
@pytest.fixture(scope="class")
def power_saving_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing power_saving_page")
    from webui.pages.PowerSavingSettingsPage import PowerSavingSettingsPage

    __page = PowerSavingSettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down power_saving_page")


# 40
@pytest.fixture(scope="class")
def ieee802_3az_eee_settings_page(logged_driver, config):
    """
    receive logged_in driver
    :param logged_driver:
    :param config:
    :return:
    """
    print("\n\n initializing ieee802_3az_eee_settings_page")
    from webui.pages.IEEE8023azEEEsettingsPage import IEEE8023azEEEsettingsPage

    __page = IEEE8023azEEEsettingsPage(logged_driver, config["base_url"])
    yield __page
    print("\n\n tearing down ieee802_3az_eee_settings_page")
