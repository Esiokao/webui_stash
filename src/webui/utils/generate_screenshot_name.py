from datetime import datetime

def generate_screenshot_name(context):
    """Generate unique screenshot filename"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"login_{context}_{timestamp}"