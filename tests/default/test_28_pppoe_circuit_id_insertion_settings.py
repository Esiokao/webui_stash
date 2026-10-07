# test_28_pppoe_circuit_id_insertion_settings.py


import allure


@allure.title("PPPoE_Circuit_ID_Insertion_Settings.PPPoE_Circuit_ID_Insertion_State_Settings")
class TestPPPoECircuitIdInsertionSettings:
    def test_check_header(self, pppoe_circuit_id_insertion_settings_page):
        result = pppoe_circuit_id_insertion_settings_page.get_page_header_text()
        expected_val = "PPPoE Circuit ID Insertion Settings"

        assert expected_val == result

    def test_check_pppoe_circuit_id_insertion_settings_tier2_header(self, pppoe_circuit_id_insertion_settings_page):
        result = pppoe_circuit_id_insertion_settings_page.get_pppoe_circuit_id_insertion_settings_tier2_header_text()
        expected_val = "PPPoE Circuit ID Insertion State Settings"

        assert expected_val == result

    def test_check_pppoe_circuit_id_insertion_state_title(self, pppoe_circuit_id_insertion_settings_page):
        result = pppoe_circuit_id_insertion_settings_page.get_pppoe_circuit_id_insertion_state_title_text()
        expected_val = "PPPoE Circuit ID Insertion State"

        assert expected_val == result

    def test_check_pppoe_circuit_id_insertion_state_option_one_text(self, pppoe_circuit_id_insertion_settings_page):
        result = pppoe_circuit_id_insertion_settings_page.get_pppoe_circuit_id_insertion_state_option_one_text()
        expected_val = "Enabled"

        assert expected_val == result

    def test_check_pppoe_circuit_id_insertion_state_option_two_text(self, pppoe_circuit_id_insertion_settings_page):
        result = pppoe_circuit_id_insertion_settings_page.get_pppoe_circuit_id_insertion_state_option_two_text()
        expected_val = "Disabled"

        assert expected_val == result

    def test_default_pppoe_circuit_id_insertion_state_is_disabled(self, pppoe_circuit_id_insertion_settings_page):
        opt = pppoe_circuit_id_insertion_settings_page.get_checked_pppoe_circuit_id_insertion_state_option()
        expected_val = "Disabled"

        assert opt == expected_val, "default pppoe circuit id insertion state is not Disabled"

    def test_check_pppoe_circuit_id_insertion_state_button(self, pppoe_circuit_id_insertion_settings_page):
        result = pppoe_circuit_id_insertion_settings_page.get_pppoe_circuit_id_insertion_state_button_text()
        expected_val = "Apply"

        assert expected_val == result


@allure.title("PPPoE_Circuit_ID_Insertion_Settings.PPPoE_Circuit_ID_Insertion_Port_Settings")
class TestPPPoECircuitIDInsertionPortSettings:
    def test_check_pppoe_circuit_id_insertion_port_header(self, pppoe_circuit_id_insertion_settings_page):
        result = pppoe_circuit_id_insertion_settings_page.get_pppoe_circuit_id_insertion_port_header_text()
        expected_val = "PPPoE Circuit ID Insertion Port Settings"

        assert expected_val == result

    def test_check_from_port_title_and_value(self, pppoe_circuit_id_insertion_settings_page):
        title, value = pppoe_circuit_id_insertion_settings_page.get_from_port_title_and_value()
        expected_title = "From Port"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

    def test_check_to_port_title_and_value(self, pppoe_circuit_id_insertion_settings_page):
        title, value = pppoe_circuit_id_insertion_settings_page.get_to_port_title_and_value()
        expected_title = "To Port"
        expected_val = "1"

        assert expected_title == title
        assert expected_val == value

    def test_check_state_title_and_value(self, pppoe_circuit_id_insertion_settings_page):
        title, value = pppoe_circuit_id_insertion_settings_page.get_state_title_and_value()
        expected_title = "State"
        expected_val = "Enabled"

        assert expected_title == title
        assert expected_val == value

    def test_check_circuit_id_title_and_value(self, pppoe_circuit_id_insertion_settings_page):
        title, value1, value2 = pppoe_circuit_id_insertion_settings_page.get_circuit_id_title_and_value()
        expected_title = "Circuit ID"
        expected_val1 = "Switch IP"
        expected_val2 = ""

        assert expected_title == title
        assert expected_val1 == value1
        assert expected_val2 == value2

    def test_check_remote_id_title_and_value(self, pppoe_circuit_id_insertion_settings_page):
        title, value1, value2 = pppoe_circuit_id_insertion_settings_page.get_remote_id_title_and_value()
        expected_title = "Remote ID"
        expected_val1 = "Default"
        expected_val2 = ""

        assert expected_title == title
        assert expected_val1 == value1
        assert expected_val2 == value2

    def test_check_pppoe_circuit_id_insertion_port_settings_button(self, pppoe_circuit_id_insertion_settings_page):
        result = pppoe_circuit_id_insertion_settings_page.get_pppoe_circuit_id_insertion_port_settings_button_text()
        expected_val = "Apply"

        assert expected_val == result

    def test_check_table_title(self, pppoe_circuit_id_insertion_settings_page):
        result = pppoe_circuit_id_insertion_settings_page.get_table_title()
        expected_val = ["Port", "State", "Circuit ID", "Remote ID"]

        assert expected_val == result

    def test_check_table_value(self, pppoe_circuit_id_insertion_settings_page):
        result = pppoe_circuit_id_insertion_settings_page.get_table_value()
        expected_val = ["1", "Disabled", "Switch IP", "Default"]

        assert expected_val == result
