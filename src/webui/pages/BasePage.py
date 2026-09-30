# pages/BasePage.py
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from dotenv import load_dotenv
load_dotenv("Settings.env")


class BasePage:
    def __init__(self, driver, base_url):
        """
        Initialize BasePage
        :param driver: WebDriver instance
        :param base_url: Base URL
        """
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(self.driver, os.getenv("WEBDRIVER_TIMEOUT"))

    def take_screenshot(self, name):
        """
        Take a screenshot and save it to the screenshots folder
        :param name: Screenshot file name
        """
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = os.path.join("screenshots", f"{name}.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

    def find_element_if_present(self, locator):
        """
        Find an element and ensure it exists
        :param locator: Element locator (By, value)
        :return: Located element or None
        """
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            print(f"Error finding element {locator}: {e}")
            return None

    def click_element_by_js(self, locator):
        """
        Click an element using JavaScript
        :param locator: Element locator (By, value)
        :return: None
        """
        try:
            element = self.find_element_if_present(locator)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print(f"Error clicking element with js {locator}: {e}")
            return None

    def find_element_if_visible(self, locator):
        """
        Find an element and ensure it is visible
        :param locator: Element locator (By, value)
        :return: Located element or None
        """
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print(f"Error finding element {locator}: {e}")
            return None

    def find_element_then_get_text(self, locator):
        """
        Find an element and get its text
        :param locator: Element locator (By, value)
        :return: Element text or None
        """
        try:
            element = self.find_element_if_visible(locator)
            return element.text if element else None
        except Exception as e:
            print(f"Error getting text from element {locator}: {e}")
            return None

    def find_element_by_text(self, parent, text):
        """
        Helper method to find an element containing the specified text within the parent element
        :param parent: The parent element to search within
        :param text: The text to search for
        :return: The found element or None
        """
        try:
            return parent.find_element(By.XPATH, f".//*[contains(text(), '{text}')]")
        except Exception:
            return None

    def find_element_by_text_within(self, parent_locator, text):
        """
        Find element in specified section
        :param parent_locator: Locator for the parent element
        :param text: The text to search for within the parent element
        :return: The found element or None
        """
        try:
            parent = self.driver.find_element(*parent_locator)
            return self.find_element_by_text(parent, text)
        except Exception:
            return None

    def text_is_existed_within(self, parent_locator, text):
        """
        Check if text exists in specified section
        :param parent_locator: Locator for the parent element
        :param text: The text to search for within the parent element
        :return: True if the text is found, False otherwise
        """
        try:
            parent = self.driver.find_element(*parent_locator)
            el = self.find_element_by_text(parent, text)
            return el is not None
        except Exception:
            return False

    def click_element(self, locator):
        """
        Click an element
        :param locator: Element locator (By, value)
        """
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            print(f"Clicked element {locator}")
        except Exception as e:
            print(f"Error clicking element {locator}: {e}")

    def input_text(self, locator, text):
        """
        Input text into an element
        :param locator: Element locator (By, value)
        :param text: Text to input
        """
        try:
            element = self.find_element_if_visible(locator)
            if element:
                element.clear()
                element.send_keys(text)
                print(f"Input text '{text}' into element {locator}")
        except Exception as e:
            print(f"Error inputting text into element {locator}: {e}")

    def find_input_value(self, locator):
        """
        Get input element's value
        :param locator: Element locator
        :return: String or None
        """
        try:
            element = self.find_element_if_visible(locator)
            if element:
                return element.get_attribute("value")
            # logging.warning(f"Element {locator} not found or not visible.")
        except Exception as e:
            # logging.error(f"Error getting value from element {locator}: {e}", exc_info=True)
            return None

    def find_checked_radio_within(self, parent_element):
        """
        Retrieve the one and only selected input inside the target div
        """
        inputs = parent_element.find_elements(By.CSS_SELECTOR, "input:checked")
        return inputs[0] if inputs else None

    # select box
    def find_selected_value_within(self, locator):
        """
        Get selected value within specified select box
        :param locator: Element locator
        :return: Selected option text
        """
        element = self.find_element_if_present(locator)
        select_box = Select(element)
        selected_option = select_box.first_selected_option
        text = selected_option.text
        return text

    def find_selected_input_label_text(self, selected_input):
        """
        Get the label text associated with the selected input
        :param selected_input: The selected input element
        :return: Label text or None
        """
        try:
            label = self.driver.find_element(By.CSS_SELECTOR, f'label[for="{selected_input.get_attribute("id")}"]')
            return label.text.strip() if label else None
        except Exception as e:
            print(f"Error getting label text: {e}")
            return None
        
    def find_selected_value(self, locator: tuple[str, str]) -> str:
        """
        根據傳入的 locator 取得 select 元素中被選取的 value。
        
        :param driver: Selenium 的 WebDriver 實例
        :param locator: 例如 ("id", "mySelect") 或 ("xpath", "//select[@name='abc']")
        :return: 被選取的 option 的 value
        """
        select_element = self.driver.find_element(*locator)
        select = Select(select_element)
        return select.first_selected_option.get_attribute("value")

    # table
    def find_cells_value_within(self, locator, cells_cls_name, timeout=5):
        """
        Find all child elements matching `cells_cls_name` within the specified parent element and return their text content
        :param locator: Parent element locator (By, value)
        :param cells_cls_name: Class name of target cells
        :param timeout: Time to wait for elements to appear (seconds)
        :return: List of text content from matching cells
        """
        try:
            # Wait for the parent element to appear
            parent_element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )

            # Find all child elements
            cells = parent_element.find_elements(By.CLASS_NAME, cells_cls_name)
            # Filter visible cells and extract their text
            return [cell.text for cell in cells if cell.is_displayed()]
        except Exception as e:
            print(f"Error for element {locator} to find cells: {e}")
            return []

    

    def wait_for_element_to_disappear(self, locator):
        """
        Wait for an element to disappear
        :param locator: Element locator (By, value)
        :return: True if successful, False otherwise
        """
        try:
            return self.wait.until(EC.invisibility_of_element_located(locator))
        except Exception as e:
            print(f"Error waiting for element {locator} to disappear: {e}")
            return False

    # browser manipulation
    def navigate_to(self, path=""):
        """
        Navigate to the specified URL
        :param path: Relative path of the URL
        """
        try:
            full_url = f"{self.base_url.rstrip('/')}/{path.lstrip('/')}"
            self.driver.get(full_url)
            print(f"Navigated to {full_url}")
        except Exception as e:
            print(f"Error navigating to {path}: {e}")

    def refresh(self):
        """
        Refresh the page
        :return: None
        """

        try:
            self.driver.refresh()
        except Exception as e:
            print(f"Error refreshing page: {e}")

    def find_checkbox_checked(self, locator):
        """
        檢查指定定位器所定位的複選框是否被選中
        :param locator: 複選框的定位器
        :return: 如果複選框被選中則返回 True，否則返回 False
        """
        try:
            # 使用顯式等待確保元素可見
            checkbox = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            # 檢查 checkbox 是否被選中
            return checkbox.is_selected()
        except Exception as e:
            print(f"Error finding checkbox {locator}: {e}")
            return False

    def find_unchecked_checkboxes_text(self, locator, get_text_func):
        """
        通用方法：取得父元素下所有未勾選且可見的 checkbox 對應的文字。
        可依據不同 HTML 結構，傳入自訂的 get_text_func 來取得對應文字。

        :param locator: 父元素的定位器 (tuple, 例如 (By.CSS_SELECTOR, "tbody"))
        :param get_text_func: 傳入一個函式，接收 checkbox 元素，回傳對應的文字
        :return: 未勾選且可見的 checkbox 對應文字列表
        """
        parent_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        checkboxes = parent_element.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        unchecked_texts = []
        for checkbox in checkboxes:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
            # 檢查 checkbox 是否可見且「未勾選」
            if checkbox.is_displayed() and not checkbox.is_selected():
                text = get_text_func(checkbox)
                if text is not None:
                    unchecked_texts.append(text.strip())
        return unchecked_texts

    def find_checked_checkboxes_text(self, locator, get_text_func):
        """
        通用方法：取得父元素下所有被勾選且可見的 checkbox 對應的文字。
        可依據不同 HTML 結構，傳入自訂的 get_text_func 來取得對應文字。
        
        :param locator: 父元素的定位器 (tuple, 例如 (By.CSS_SELECTOR, "tbody"))
        :param get_text_func: 傳入一個函式，接收 checkbox 元素，回傳對應的文字
        :return: 被勾選且可見的 checkbox 對應文字列表
        """
        parent_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        checkboxes = parent_element.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        selected_texts = []
        for checkbox in checkboxes:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
            # 檢查 checkbox 是否可見且被勾選
            if checkbox.is_displayed() and checkbox.is_selected():
                # 透過自訂函式取得對應文字
                text = get_text_func(checkbox)
                if text is not None:
                    selected_texts.append(text.strip())
        return selected_texts

    # 針對「數字在 .head > span」的結構
    def get_head_span_text(self, checkbox):
        """
        取得同一個 <td> 下 .head > span 的文字
        """
        try:
            td = checkbox.find_element(By.XPATH, "./ancestor::td[1]")
            head_span = td.find_element(By.CSS_SELECTOR, ".head > span")
            return head_span.text
        except Exception:
            return None

    # 針對「checkbox 旁邊有文字」的結構
    def get_sibling_text(self, checkbox):
        """
        取得 checkbox 父 <span> 內 &nbsp; 後面的文字
        """
        try:
            parent_span = checkbox.find_element(By.XPATH, "./ancestor::span[1]")
            text = parent_span.text
            if '\xa0' in text:
                return text.split('\xa0', 1)[1]
            return text
        except Exception:
            return None

    # 使用方式說明：
    # locator = (By.CSS_SELECTOR, "tbody")
    # checked_texts = self.find_checked_checkboxes_text(locator, self.get_head_span_text)
    # locator2 = (By.CSS_SELECTOR, "td[colspan='6']")
    # checked_texts2 = self.find_checked_checkboxes_text(locator2, self.get_sibling_text)