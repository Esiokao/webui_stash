# tests/fixtures/driver_fixture.py
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="session")
def driver(config):
    """WebDriver fixture supporting multi-browser selection via BROWSER env (default: chrome)."""
    browser_name = os.getenv("BROWSER", "chrome").lower().strip()
    is_headless = os.getenv("HEADLESS", "false").lower() in ("true", "1", "yes")

    print(f"\n\n initializing webdriver for browser: {browser_name} (headless={is_headless})")

    if browser_name == "firefox":
        options = FirefoxOptions()
        if is_headless:
            options.add_argument("-headless")
        options.add_argument(f"--width={config['screen_width']}")
        options.add_argument(f"--height={config['screen_height']}")
        driver = webdriver.Firefox(options=options)

    elif browser_name in ("edge", "msedge"):
        options = EdgeOptions()
        if is_headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--window-size={config['screen_width']},{config['screen_height']}")
        driver = webdriver.Edge(options=options)

    else:
        # Default to Chrome
        options = ChromeOptions()
        if is_headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument(f"--window-size={config['screen_width']},{config['screen_height']}")
        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(config["implicit_wait"])

    yield driver

    print(f"\n\n tearing down webdriver ({browser_name})")
    driver.quit()
