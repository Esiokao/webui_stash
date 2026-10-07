# test_20_snmp_view_table.py


import allure


@allure.title("snmp_view_table")
class TestSNMPViewTable:
    def test_check_header(self, snmp_view_table_page):
        result = snmp_view_table_page.get_page_header_text()
        expected_val = "SNMP View Table Configuration"

        assert expected_val == result

    def test_check_snmp_view_table_tier2_header(self, snmp_view_table_page):
        result = snmp_view_table_page.get_snmp_view_table_tier2_header_text()
        expected_val = "SNMP View Table Configuration"

        assert expected_val == result

    def test_check_view_name_title_and_value(self, snmp_view_table_page):
        title, value = snmp_view_table_page.get_view_name_title_and_value()
        expected_title = "View Name"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_subtree_oid_title_and_value(self, snmp_view_table_page):
        title, value = snmp_view_table_page.get_subtree_oid_title_and_value()
        expected_title = "Subtree OID"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_oid_mask_title_and_value(self, snmp_view_table_page):
        title, value = snmp_view_table_page.get_oid_mask_title_and_value()
        expected_title = "OID Mask"
        expected_val = ""

        assert expected_title == title
        assert expected_val == value

    def test_check_view_type_title_and_value(self, snmp_view_table_page):
        title, value = snmp_view_table_page.get_view_type_title_and_value()
        expected_title = "View Type"
        expected_val = "Included"

        assert expected_title == title
        assert expected_val == value

    def test_check_button_text(self, snmp_view_table_page):
        result = snmp_view_table_page.get_button_text()
        expected_val = "Apply"

        assert expected_val == result

    def test_check_total_entries_title(self, snmp_view_table_page):
        result = snmp_view_table_page.get_total_entries_title()
        expected_val = "Total Entries : 2"

        assert expected_val == result

    def test_check_table_title(self, snmp_view_table_page):
        result = snmp_view_table_page.get_table_title()
        expected_val = ["View Name", "Subtree OID", "OID Mask", "View Type", "Delete"]

        assert expected_val == result

    def test_check_readonly_table_value(self, snmp_view_table_page):
        result = snmp_view_table_page.get_readonly_table_value()
        expected_val = ["ReadOnly", "1", "1", "Included", ""]

        assert expected_val == result

    def test_check_readonly_table_button_text(self, snmp_view_table_page):
        result = snmp_view_table_page.get_readonly_table_button_text()
        expected_val = "Delete"

        assert expected_val == result

    def test_check_read_write_table_value(self, snmp_view_table_page):
        result = snmp_view_table_page.get_read_write_table_value()
        expected_val = ["ReadWrite", "1", "1", "Included", ""]

        assert expected_val == result

    def test_check_read_write_table_button_text(self, snmp_view_table_page):
        result = snmp_view_table_page.get_read_write_table_button_text()
        expected_val = "Delete"

        assert expected_val == result

    def test_check_view_table_page_text(self, snmp_view_table_page):
        result = snmp_view_table_page.get_view_table_page_text()
        expected_val = "1 / 1"

        assert expected_val == result

    def test_check_view_table_page_button1_text(self, snmp_view_table_page):
        result = snmp_view_table_page.get_view_table_page_button1_text()
        expected_val = "|<"

        assert expected_val == result

    def test_check_view_table_page_button2_text(self, snmp_view_table_page):
        result = snmp_view_table_page.get_view_table_page_button2_text()
        expected_val = "<"

        assert expected_val == result

    def test_check_view_table_page_button3_text(self, snmp_view_table_page):
        result = snmp_view_table_page.get_view_table_page_button3_text()
        expected_val = "1"

        assert expected_val == result

    def test_check_view_table_page_button4_text(self, snmp_view_table_page):
        result = snmp_view_table_page.get_view_table_page_button4_text()
        expected_val = ">"

        assert expected_val == result

    def test_check_view_table_page_button5_text(self, snmp_view_table_page):
        result = snmp_view_table_page.get_view_table_page_button5_text()
        expected_val = ">|"

        assert expected_val == result

    def test_check_view_table_page_value(self, snmp_view_table_page):
        result = snmp_view_table_page.get_view_table_page_value()
        expected_val = ""

        assert expected_val == result

    def test_check_view_table_page_button6_text(self, snmp_view_table_page):
        result = snmp_view_table_page.get_view_table_page_button6_text()
        expected_val = "Go"

        assert expected_val == result
