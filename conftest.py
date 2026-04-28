import os
import json
import urllib.parse
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def setup_page(request):
    """
    Fixture to set up the Playwright browser page.
    Handles both local execution and LambdaTest cloud execution based on environment variables.
    """
    execution_env = os.environ.get("EXECUTION_ENV", "local").lower()
    
    with sync_playwright() as playwright:
        if execution_env == "lambdatest":
            # Connect to LambdaTest Cloud
            username = os.environ.get("LT_USERNAME", "your_username")
            access_key = os.environ.get("LT_ACCESS_KEY", "your_access_key")
            
            capabilities = {
                "browserName": "Chrome",
                "browserVersion": "latest",
                "LT:Options": {
                    "platform": "Windows 11",
                    "build": "Amazon Playwright Parallel Build",
                    "name": request.node.name,
                    "user": username,
                    "accessKey": access_key,
                    "network": True,
                    "video": True,
                    "console": True,
                }
            }
            
            # Convert capabilities to URL encoded JSON string
            caps_json = json.dumps(capabilities)
            ws_endpoint = f"wss://cdp.lambdatest.com/playwright?capabilities={urllib.parse.quote(caps_json)}"
            
            # Connect to the remote LambdaTest browser
            browser = playwright.chromium.connect(ws_endpoint)
            context = browser.new_context(
                viewport={"width": 1920, "height": 1080}
            )
            page = context.new_page()
            
            yield page
            
            # Teardown
            page.close()
            context.close()
            browser.close()
        else:
            # Run locally
            headless = os.environ.get("HEADLESS", "false").lower() == "true"
            browser = playwright.chromium.launch(headless=headless)
            context = browser.new_context(
                viewport={"width": 1920, "height": 1080}
            )
            page = context.new_page()
            
            yield page
            
            # Teardown
            page.close()
            context.close()
            browser.close()
