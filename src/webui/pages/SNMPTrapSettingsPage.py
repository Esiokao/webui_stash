# pages/SNMPTrapSettingsPage.py
from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage

from webui.utils.generate_screenshot_name import generate_screenshot_name


class SNMPTrapSettingsPage(BasePage):
    def __init__(self, driver, base_url):
        """
        初始化 SNMPTrapSettingsPage
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
        SNMP_TRAP_SETTINGS_MENU_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > li > ul > div:nth-child(11) > li > ul > div:nth-child(8) > a > li > span")
        self.find_element_if_present(SYSTEM_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_SETTINGS_MENU_LOCATOR).click()
        self.find_element_if_present(SNMP_TRAP_SETTINGS_MENU_LOCATOR).click()

        return True

    def get_page_header_text(self):
        PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div")
        return self.find_element_then_get_text(PAGE_HEADER_LOCATOR)
    
    def get_snmp_trap_settings_tier2_header_text(self):
        SNMP_TRAP_SETTINGS_TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
        return self.find_element_then_get_text(SNMP_TRAP_SETTINGS_TIER2_HEADER_LOCATOR)

    def get_snmp_authentication_traps_title_and_value(self):
        SNMP_AUTHENTICATION_TRAPS_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr > td")
        SNMP_AUTHENTICATION_TRAPS_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpTrapSNMPAuthentication")
        title = self.find_element_then_get_text(SNMP_AUTHENTICATION_TRAPS_TITLE_LOCATOR)
        value = self.find_checkbox_checked(SNMP_AUTHENTICATION_TRAPS_VALUE_LOCATOR)
        return title, value

    def get_system_coldstart_traps_title_and_value(self):
        SYSTEM_COLDSTART_TRAPS_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(2) > td")
        SYSTEM_COLDSTART_TRAPS_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpTrapColdStart")
        title = self.find_element_then_get_text(SYSTEM_COLDSTART_TRAPS_TITLE_LOCATOR)
        value = self.find_checkbox_checked(SYSTEM_COLDSTART_TRAPS_VALUE_LOCATOR)
        return title, value

    def get_system_warmstart_traps_title_and_value(self):
        SYSTEM_WARMSTART_TRAPS_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(3) > td")
        SYSTEM_WARMSTART_TRAPS_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpTrapWarmStart")
        title = self.find_element_then_get_text(SYSTEM_WARMSTART_TRAPS_TITLE_LOCATOR)
        value = self.find_checkbox_checked(SYSTEM_WARMSTART_TRAPS_VALUE_LOCATOR)
        return title, value

    def get_port_link_up_and_link_down_title_and_value(self):
        PORT_LINK_UP_AND_LINK_DOWN_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(4) > td")
        PORT_LINK_UP_AND_LINK_DOWN_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpTrapPortLinkUpDown")
        title = self.find_element_then_get_text(PORT_LINK_UP_AND_LINK_DOWN_TITLE_LOCATOR)
        value = self.find_checkbox_checked(PORT_LINK_UP_AND_LINK_DOWN_VALUE_LOCATOR)
        return title, value

    def get_rstp_port_state_change_title_and_value(self):
        RSTP_PORT_STATE_CHANGE_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(5) > td")
        RSTP_PORT_STATE_CHANGE_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpRstpportChangeTrapsEnable")
        title = self.find_element_then_get_text(RSTP_PORT_STATE_CHANGE_TITLE_LOCATOR)
        value = self.find_checkbox_checked(RSTP_PORT_STATE_CHANGE_VALUE_LOCATOR)
        return title, value

    def get_firmware_upgrade_state_title_and_value(self):
        FIRMWARE_UPGRADE_STATE_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(6) > td")
        FIRMWARE_UPGRADE_STATE_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpFirmwareUpgradeTrapsEnable")
        title = self.find_element_then_get_text(FIRMWARE_UPGRADE_STATE_TITLE_LOCATOR)
        value = self.find_checkbox_checked(FIRMWARE_UPGRADE_STATE_VALUE_LOCATOR)
        return title, value

    def get_port_security_violation_state_title_and_value(self):
        PORT_SECURITY_VIOLATION_STATE_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(7) > td")
        PORT_SECURITY_VIOLATION_STATE_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpPortSecurityTrapState")
        title = self.find_element_then_get_text(PORT_SECURITY_VIOLATION_STATE_TITLE_LOCATOR)
        value = self.find_checkbox_checked(PORT_SECURITY_VIOLATION_STATE_VALUE_LOCATOR)
        return title, value

    def get_impb_violation_state_title_and_value(self):
        IMPB_VIOLATION_STATE_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(8) > td")
        IMPB_VIOLATION_STATE_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpImpbViolationTrapsEnable")
        title = self.find_element_then_get_text(IMPB_VIOLATION_STATE_TITLE_LOCATOR)
        value = self.find_checkbox_checked(IMPB_VIOLATION_STATE_VALUE_LOCATOR)
        return title, value

    def get_loopback_detection_occuring_and_recovery_title_and_value(self):
        LOOPBACK_DETECTION_OCCURING_AND_RECOVERY_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(9) > td")
        LOOPBACK_DETECTION_OCCURING_AND_RECOVERY_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpTrapLBDState")
        title = self.find_element_then_get_text(LOOPBACK_DETECTION_OCCURING_AND_RECOVERY_TITLE_LOCATOR)
        value = self.find_checkbox_checked(LOOPBACK_DETECTION_OCCURING_AND_RECOVERY_VALUE_LOCATOR)
        return title, value

    def get_dhcp_server_screening_title_and_value(self):
        DHCP_SERVER_SCREENING_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(10) > td")
        DHCP_SERVER_SCREENING_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpTrapDhcpServerScreenState")
        title = self.find_element_then_get_text(DHCP_SERVER_SCREENING_TITLE_LOCATOR)
        value = self.find_checkbox_checked(DHCP_SERVER_SCREENING_VALUE_LOCATOR)
        return title, value

    def get_duplicate_ip_detected_title_and_value(self):
        DUPLICATE_IP_DETECTED_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(11) > td")
        DUPLICATE_IP_DETECTED_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpTrapDuplicateIPDetected")
        title = self.find_element_then_get_text(DUPLICATE_IP_DETECTED_TITLE_LOCATOR)
        value = self.find_checkbox_checked(DUPLICATE_IP_DETECTED_VALUE_LOCATOR)
        return title, value

    def get_dhcpv6_server_screening_title_and_value(self):
        DHCPV6_SERVER_SCREENING_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(12) > td")
        DHCPV6_SERVER_SCREENING_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpTrapDhcpv6ServerScreenState")
        title = self.find_element_then_get_text(DHCPV6_SERVER_SCREENING_TITLE_LOCATOR)
        value = self.find_checkbox_checked(DHCPV6_SERVER_SCREENING_VALUE_LOCATOR)
        return title, value

    def get_icmpv6_ra_all_node_filter_title_and_value(self):
        ICMPV6_RA_ALL_NODE_FILTER_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(13) > td")
        ICMPV6_RA_ALL_NODE_FILTER_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpTrapIcmpv6RaNodeFilterState")
        title = self.find_element_then_get_text(ICMPV6_RA_ALL_NODE_FILTER_TITLE_LOCATOR)
        value = self.find_checkbox_checked(ICMPV6_RA_ALL_NODE_FILTER_VALUE_LOCATOR)
        return title, value

    def get_login_and_logout_title_and_value(self):
        LOGIN_AND_LOGOUT_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(14) > td")
        LOGIN_AND_LOGOUT_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpLoginLogoutTrapsEnable")
        title = self.find_element_then_get_text(LOGIN_AND_LOGOUT_TITLE_LOCATOR)
        value = self.find_checkbox_checked(LOGIN_AND_LOGOUT_VALUE_LOCATOR)
        return title, value

    def get_duld_traps_title_and_value(self):
        DULD_TRAPS_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(15) > td")
        DULD_TRAPS_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpTrapDULD")
        title = self.find_element_then_get_text(DULD_TRAPS_TITLE_LOCATOR)
        value = self.find_checkbox_checked(DULD_TRAPS_VALUE_LOCATOR)
        return title, value

    def get_rps_traps_title_and_value(self):
        RPS_TRAPS_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(16) > td")
        RPS_TRAPS_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpTrapRpsState")
        title = self.find_element_then_get_text(RPS_TRAPS_TITLE_LOCATOR)
        value = self.find_checkbox_checked(RPS_TRAPS_VALUE_LOCATOR)
        return title, value

    def get_dying_gasp_traps_title_and_value(self):
        DYING_GASP_TRAPS_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(17) > td")
        DYING_GASP_TRAPS_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpTrapDyingGasp")
        title = self.find_element_then_get_text(DYING_GASP_TRAPS_TITLE_LOCATOR)
        value = self.find_checkbox_checked(DYING_GASP_TRAPS_VALUE_LOCATOR)
        return title, value

    def get_802_1x_traps_title_and_value(self):
        EIGHTY_TWO_POINT_ONE_X_TRAPS_TITLE_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > table > tr:nth-child(18) > td")
        EIGHTY_TWO_POINT_ONE_X_TRAPS_VALUE_LOCATOR = (By.CSS_SELECTOR, "#checkbox-snmpTrapPnacAuth")
        title = self.find_element_then_get_text(EIGHTY_TWO_POINT_ONE_X_TRAPS_TITLE_LOCATOR)
        value = self.find_checkbox_checked(EIGHTY_TWO_POINT_ONE_X_TRAPS_VALUE_LOCATOR)
        return title, value

    def get_dying_gasp_traps_types_title_and_value(self):
        DYING_GASP_TRAPS_TYPES_TITLE_LOCATOR = (By.XPATH, "/html/body/div/div/div/section/div/section/div/div[2]/fieldset/table/tr[19]/td")
        DYING_GASP_TRAPS_TYPES_VALUE_LOCATOR = (By.CSS_SELECTOR, "#dyingGaspTrapsTypes")
        td_element = self.find_element_if_visible(DYING_GASP_TRAPS_TYPES_TITLE_LOCATOR)
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
        value = self.find_selected_value_within(DYING_GASP_TRAPS_TYPES_VALUE_LOCATOR)
        return title, value

    def get_trap_settings_button_text(self):
        TRAP_SETTINGS_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#Apply")
        return self.find_input_value(TRAP_SETTINGS_BUTTON_LOCATOR)

    def get_snmp_link_change_trap_port_table_header(self):
        SNMP_LINK_CHANGE_TRAP_PORT_TABLE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > section > div > div:nth-child(3) > fieldset > legend")
        return self.find_element_then_get_text(SNMP_LINK_CHANGE_TRAP_PORT_TABLE_HEADER_LOCATOR)

    def get_linkchange_trap_port_select_all_button_text(self):
        LINKCHANGE_TRAP_PORT_SELECT_ALL_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#LinkselectAll")
        return self.find_input_value(LINKCHANGE_TRAP_PORT_SELECT_ALL_BUTTON_LOCATOR)

    def get_linkchange_trap_port_clear_button_text(self):
        LINKCHANGE_TRAP_PORT_CLEAR_BUTTON_LOCATOR = (By.XPATH, "/html/body/div/div/div/section/div/section/div/div[3]/fieldset/table/tr/td/input[2]")
        return self.find_input_value(LINKCHANGE_TRAP_PORT_CLEAR_BUTTON_LOCATOR)

    def get_linkchange_trap_port_apply_button_text(self):
        LINKCHANGE_TRAP_PORT_APPLY_BUTTON_LOCATOR = (By.XPATH, "/html/body/div/div/div/section/div/section/div/div[3]/fieldset/table/tr/td/input[3]")
        return self.find_input_value(LINKCHANGE_TRAP_PORT_APPLY_BUTTON_LOCATOR)

    def get_linkchange_port_num_title(self):
        LINKCHANGE_PORT_NUM_TITLE_LOCATOR = (By.CSS_SELECTOR, "#table_box > table > tbody")
        cells_class_name = "head"
        return self.find_cells_value_within(LINKCHANGE_PORT_NUM_TITLE_LOCATOR, cells_class_name)

    def get_linkchange_port_default_status(self):
        locator = (By.XPATH, "/html/body/div[1]/div/div/section/div/section/div/div[3]/fieldset/div/div/table/tbody")
        checked_numbers = self.find_unchecked_checkboxes_text(locator, self.get_head_span_text)
        return checked_numbers

    def get_snmp_sending_trap_port_table_header(self):
        SNMP_SENDING_TRAP_PORT_TABLE_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(4) > fieldset > legend")
        return self.find_element_then_get_text(SNMP_SENDING_TRAP_PORT_TABLE_HEADER_LOCATOR)

    def get_snmp_sending_trap_port_select_all_button_text(self):
        SNMP_SENDING_TRAP_PORT_SELECT_ALL_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#TrapselectAll")
        
        element = self.driver.find_element(*SNMP_SENDING_TRAP_PORT_SELECT_ALL_BUTTON_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        return self.find_input_value(SNMP_SENDING_TRAP_PORT_SELECT_ALL_BUTTON_LOCATOR)

    def get_snmp_sending_trap_port_clear_button_text(self):
        SNMP_SENDING_TRAP_PORT_CLEAR_BUTTON_LOCATOR = (By.XPATH, "/html/body/div/div/div/section/div/section/div/div[4]/fieldset/table/tr/td/input[2]")
        return self.find_input_value(SNMP_SENDING_TRAP_PORT_CLEAR_BUTTON_LOCATOR)

    def get_snmp_sending_trap_port_apply_button_text(self):
        SNMP_SENDING_TRAP_PORT_APPLY_BUTTON_LOCATOR = (By.XPATH, "/html/body/div/div/div/section/div/section/div/div[4]/fieldset/table/tr/td/input[3]")
        return self.find_input_value(SNMP_SENDING_TRAP_PORT_APPLY_BUTTON_LOCATOR)

    def get_snmp_sending_trap_port_num_title(self):
        SNMP_SENDING_TRAP_PORT_NUM_TITLE_LOCATOR = (By.XPATH, "/html/body/div/div/div/section/div/section/div/div[4]/fieldset/div/div/table/tbody")
        cells_class_name = "head"
        return self.find_cells_value_within(SNMP_SENDING_TRAP_PORT_NUM_TITLE_LOCATOR, cells_class_name)

    def get_snmp_sending_trap_port_default_status(self):
        locator = (By.XPATH, "/html/body/div[1]/div/div/section/div/section/div/div[4]/fieldset/div/div/table/tbody")
        checked_numbers = self.find_checked_checkboxes_text(locator, self.get_head_span_text)
        return checked_numbers


