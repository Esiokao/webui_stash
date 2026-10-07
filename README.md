### Prerequisites
* Python 3.10+
* Poetry
* Google Chrome & matching ChromeDriver

### 1. Installation
```bash
# Clone the repository
git clone https://github.com/esiokao/webui.git
cd webui

# Install dependencies using Poetry
poetry install
```

### 2. Environment Configuration
Edit `.env` or `Settings.env` according to your testbed environment:
```ini
TEST_BASE_URL="http://10.90.90.90"
COM_PORT="COM3"
BAUD_RATE="115200"
HEADLESS="false"
USE_MOCK="false"   # Set to 'false' when connecting to a physical switch
```

# Run the dual-channel verification suite
poetry run pytest tests/test_99_advanced_dual_verification.py -v

# Run with Allure report generation
poetry run pytest tests/ --alluredir=allure-results
allure serve allure-results
```

#### Run with Physical Testbed
```bash
# Disable mock mode and connect directly to switch WebUI & Serial port
USE_MOCK=false HEADLESS=false poetry run pytest tests/ -v
```
