import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def get_driver():
    """初始化 WebDriver (支援 HEADLESS 設定，由 Selenium 4 原生管理)"""
    options = ChromeOptions()
    is_headless = os.getenv("HEADLESS", "true").lower() in ("true", "1", "yes")
    if is_headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)
