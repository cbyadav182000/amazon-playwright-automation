# Amazon Playwright Automation Project

This is a comprehensive, production-ready QA automation framework designed to test Amazon's search and "Add to Cart" functionality. It is built using **Python**, **Playwright**, and **Pytest**, following industry best practices like the **Page Object Model (POM)** and **Parallel Execution**.

---

## ✨ Key Features

- **Page Object Model (POM)**: Separates page logic from test scripts for high maintainability.
- **Parallel Execution**: Uses `pytest-xdist` to run multiple tests simultaneously, significantly reducing execution time.
- **Robust Selectors**: Implements resilient selectors (like `a.a-link-normal` and `force=True` clicks) to handle Amazon's dynamic and complex DOM.
- **Cloud Ready**: Pre-configured for **LambdaTest** integration for cross-browser testing in the cloud.
- **Environment Management**: Easily switch between Local (Headful/Headless) and Remote execution using environment variables.

---

## 📂 Project Structure

- **`pages.py`**: The heart of the POM structure. Contains classes for `AmazonHomePage`, `AmazonSearchResultsPage`, and `AmazonProductPage`. It encapsulates all element locators and page-specific actions.
- **`test_amazon.py`**: Contains the actual test cases (iPhone and Galaxy scenarios). These scripts are clean and readable, focusing on the business logic of the test.
- **`conftest.py`**: The global configuration file for Pytest. It manages browser lifecycle (setup/teardown) and handles the logic for connecting to either a local browser or the LambdaTest grid.
- **`requirements.txt`**: List of all Python dependencies required to run the project.

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- **Python 3.8+**: Ensure Python is installed. You can check via `python3 --version`.
- **pip**: Python's package manager.

### 2. Install Dependencies
Clone the project and run the following command in your terminal:
```bash
pip3 install -r requirements.txt
```

### 3. Install Playwright Browsers
Playwright needs its own browser binaries to run. Install the Chromium browser using:
```bash
python3 -m playwright install chromium
```

---

## 🚀 Running the Tests

You can run the tests in two modes depending on your needs:

### A. Parallel Mode (Fastest)
Use this mode to run both iPhone and Galaxy tests at the same time in two separate browser windows.
```bash
python3 -m pytest test_amazon.py -n 2 -s
```
- `-n 2`: Run using 2 parallel workers.
- `-s`: Disables output capturing (needed to see `print` statements).

### B. Sequential Mode (Detailed View)
Use this mode if you want to see the execution in order and ensure all console outputs (like the **Device Price**) are clearly visible.
```bash
python3 -m pytest test_amazon.py -s
```

---

## ❓ Troubleshooting & FAQ

### 1. Why don't I see the Device Price in Parallel Mode?
When running with `-n 2` (parallel), `pytest-xdist` captures the output from different workers. Sometimes, it hides the `print()` statements of passed tests to keep the terminal clean. To see the price clearly, run the tests in **Sequential Mode** (without `-n 2`).

### 2. What if Amazon shows a Captcha?
Amazon sometimes detects automation and shows a "Type the characters" page. Since this is a headful test (browser is visible), you can manually solve the Captcha in the browser window, and the script will automatically continue once the search results load.

### 3. Click Timeout Errors
Amazon often has invisible overlays that intercept clicks. Our framework uses `force=True` in `pages.py` to bypass these overlays and ensure the "Add to Cart" and product links are clicked successfully.

---

## ☁️ LambdaTest Integration

To run these tests on the LambdaTest Cloud:

1. **Set Environment Variables**:
   ```bash
   export EXECUTION_ENV="lambdatest"
   export LT_USERNAME="your_username"
   export LT_ACCESS_KEY="your_access_key"
   ```
2. **Run Tests**:
   ```bash
   python3 -m pytest test_amazon.py -n 2 -s
   ```
You can view the live execution, video recordings, and console logs directly on your LambdaTest Web Automation Dashboard.

---

## 📊 Execution Demo (Example Output)

When you run the tests in **Sequential Mode** (`python3 -m pytest test_amazon.py -s`), you will see the console output like this:

```text
======================= test session starts =======================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.6.0
collected 2 items                                                                                                            

test_amazon.py 

[iPhone Test] The price of the first iPhone is: INR 4,612.37
.
[Galaxy Test] The price of the first Galaxy is: INR 122,368.06
.

======================= 2 passed in 28.85s =======================
admin@Admins-Mac-mini amazon_automation % git push -u origin main --force

Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 4 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 4.85 KiB | 1.21 MiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/cbyadav182000/amazon-playwright-automation.git
 + 9f2d22d...69eb02c main -> main (forced update)
branch 'main' set up to track 'origin/main'.
admin@Admins-Mac-mini amazon_automation % python3 -m pytest test_amazon.py -n 2 -s
=============================================== test session starts ================================================
platform darwin -- Python 3.11.7, pytest-8.1.1, pluggy-1.6.0
rootdir: /Users/admin/Desktop/TestMu AI/amazon_automation
plugins: langsmith-0.7.26, xdist-3.5.0, anyio-4.13.0
2 workers [2 items]     
..
================================================ 2 passed in 25.45s ================================================
admin@Admins-Mac-mini amazon_automation % 
```
*Note: Prices will vary based on current Amazon listings and currency.*
