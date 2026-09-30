from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    """初始化 WebDriver"""
    options = Options()
    options.add_argument("--headless")  # 無頭模式
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=options)