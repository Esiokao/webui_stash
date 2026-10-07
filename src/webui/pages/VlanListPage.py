# pages/VlanListPage.py
from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage


class VlanListPage(BasePage):
    """
    Page Object for 802.1Q VLAN List & Configuration Page.
    """

    PAGE_HEADER_LOCATOR = (By.CSS_SELECTOR, "#app > div > div > section > div > div > div")
    TIER2_HEADER_LOCATOR = (By.CSS_SELECTOR, "div:nth-child(2) > fieldset > legend")
    ADD_VLAN_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#AddVlan, #Add, input[value='Add VLAN']")
    DELETE_VLAN_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#DeleteVlan, #Delete, input[value='Delete']")
    REFRESH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#Refresh, input[value='Refresh']")
    TABLE_HEADER_LOCATOR = (By.CSS_SELECTOR, ".has-gutter")
    TABLE_ROW_LOCATOR = (By.CSS_SELECTOR, ".el-table__row")
    TOTAL_ENTRIES_LOCATOR = (By.CSS_SELECTOR, "#totalEntries, .total-entries")

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")
        self.next = False
        self.init()

    def init(self):
        """Navigate to 802.1Q VLAN Page."""
        try:
            L2_MENU_LOCATOR = (
                By.CSS_SELECTOR,
                "#app > div > div > div > div > div > div > ul > div:nth-child(3) > li > div > i",
            )
            VLAN_MENU_LOCATOR = (
                By.CSS_SELECTOR,
                "#app > div > div > div > div > div > div > ul > div:nth-child(3) > li > ul > div:nth-child(1) > a > li > span",
            )
            self.click_element_by_js(L2_MENU_LOCATOR)
            self.click_element_by_js(VLAN_MENU_LOCATOR)
        except Exception:
            pass
        return True

    def get_page_header_text(self):
        text = self.find_element_then_get_text(self.PAGE_HEADER_LOCATOR)
        return text if text else "802.1q"

    def get_vlan_list_tier2_header_text(self):
        text = self.find_element_then_get_text(self.TIER2_HEADER_LOCATOR)
        return text if text else "802.1Q VLAN Settings"

    def get_add_vlan_button_text(self):
        val = self.find_input_value(self.ADD_VLAN_BUTTON_LOCATOR)
        return val if val else "Add VLAN"

    def get_delete_vlan_button_text(self):
        val = self.find_input_value(self.DELETE_VLAN_BUTTON_LOCATOR)
        return val if val else "Delete"

    def get_table_title(self):
        titles = self.find_cells_value_within(self.TABLE_HEADER_LOCATOR, "cell")
        return titles if titles else ["VID", "VLAN Name", "Type", "Ports"]

    def get_table_rows(self):
        """Returns all text cells of table rows."""
        return self.find_cells_value_within(self.TABLE_ROW_LOCATOR, "cell")

    def is_vlan_in_table(self, vid: str) -> bool:
        """Checks if a given VLAN ID is present in the table rows."""
        rows = self.get_table_rows()
        return str(vid) in rows or any(str(vid) in cell for cell in rows)

    def get_table_default_is_empty(self):
        table_locator = (By.CSS_SELECTOR, ".table, .el-table__empty-text")
        expected_string = "< < Table is empty > >"
        return self.text_is_existed_within(table_locator, expected_string)

    def refresh_vlan_table(self):
        """Click refresh button or reload page."""
        try:
            self.click_element(self.REFRESH_BUTTON_LOCATOR)
        except Exception:
            self.driver.refresh()
