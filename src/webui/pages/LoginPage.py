# pages/LoginPage.py
import time
from selenium.webdriver.common.by import By
from webui.pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    # Page element locators
    USERNAME_INPUT = (By.ID, "Username")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.ID, "Login")
    USERINFO_SPAN = (By.CLASS_NAME, "userInfo")
    MAIN_FRAME_ID = "iframemain"
    LOGIN_STATUS = False

    @classmethod
    def set_login_status(cls, status):
        """設置類屬性 LOGIN_STATUS"""
        print("set login status: ", status)
        cls.LOGIN_STATUS = status

    @classmethod
    def get_login_status(cls):
        """獲取類屬性 LOGIN_STATUS"""
        return cls.LOGIN_STATUS

    def __init__(self, driver, base_url):
        """
        初始化 LoginPage
        :param driver: WebDriver 實例
        :param base_url: 基本網址
        """
        super().__init__(driver, base_url)
        self.url = base_url.rstrip("/")  # 確保 base_url 沒有多餘的斜杠
        self.next = False
        self.open()
        self.switch_to_main_frame()

    def open(self):
        """
        打開登錄頁面
        :return: 當前頁面標題
        """
        self.navigate_to()  # 使用 BasePage 的方法導航到 base_url
        return self.driver.title

    def switch_to_main_frame(self):
        """
        切換到主框架
        :return: 切換成功返回 True
        """
        try:
            frame = self.find_element_if_visible((By.ID, self.MAIN_FRAME_ID))
            self.driver.switch_to.frame(frame)
            print("Switched to main frame")
            return True
        except Exception as e:
            raise RuntimeError(f"Failed to switch to main frame: {e}")

    def login(self, username, password):
        """
        執行登錄操作
        :param username: 用戶名
        :param password: 密碼
        :return: 登錄成功返回 True
        """
        try:
            self.input_text(self.USERNAME_INPUT, username)
            self.input_text(self.PASSWORD_INPUT, password)
            self.click_element(self.LOGIN_BUTTON)
            print("Login button clicked")
            return True
        except Exception as e:
            raise RuntimeError(f"Failed to login: {e}")

    def is_login_successful(self):
        """
        檢查登錄是否成功
        :return: 成功返回 True，否則返回 False
        """
        print("\n Checking Current Login Status: ", self.get_login_status())
        try:
            # 顯式等待元素顯示出來
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.USERINFO_SPAN))
            user_info_text = self.find_element_then_get_text(self.USERINFO_SPAN)
            if user_info_text and "logged in" in user_info_text.lower():
                print("Login successful")
                LoginPage.set_login_status(True)
                return True
            
            print("Login unsuccessful")
            LoginPage.set_login_status(False)
            return False
        except Exception:
            LoginPage.set_login_status(False)
            print("Error during login status check")
            return False


    def do_login(self, username, password, timeout=10):
        """
        登入函數，重試一次並加上 timeout 等待載入完成
        """

        count = 0
        max_retry = 1

        while count <= max_retry:
            print('Trying to Login')

            if self.get_login_status():
                self.open()
                self.switch_to_main_frame()
                return  # 已登入，結束
            WebDriverWait(self.driver, timeout).until(lambda d: d.execute_script("return document.readyState") == "complete")

            self.open()
            self.switch_to_main_frame()
            self.login(username, password)
            time.sleep(2.5) # force to wait iframe loading
            # 加入短暫等待，確認登入是否成功
            try:
                WebDriverWait(self.driver, timeout).until(lambda d: self.is_login_successful())
                self.set_login_status(True)
                return  # 登入成功，結束
            except Exception:
                count += 1  # 登入失敗，重試一次

            raise Exception("❌ Login failed after retry.")
