# Selenium Testing Suite for Book Store MERN Project

## Overview
This testing suite provides comprehensive automated testing for your Book Store MERN (MongoDB, Express, React, Node.js) application. It includes step-by-step validation with detailed alert messages and test reports, with each test running for at least 2 minutes.

## Files Included

1. **test_selenium_script.py** - Basic Selenium testing suite with 10 core test cases
2. **test_selenium_advanced.py** - Advanced testing suite with 15 extended test cases and detailed logging
3. **SELENIUM_TEST_README.md** - This comprehensive guide

## Features

✅ **Multiple Test Suites:**
- Basic Suite: 10 comprehensive tests
- Advanced Suite: 15 extended tests with detailed metrics

✅ **Test Coverage:**
- Homepage load and performance
- Navigation bar functionality
- Footer verification
- Book browsing and display
- Cart functionality
- Login and Register pages
- Page transitions and links
- Responsive design checking
- Image loading verification
- Form validation
- Dynamic content loading
- Performance metrics

✅ **User-Friendly Output:**
- Real-time status messages with timestamps
- Color-coded test results (✓ = Pass, ✗ = Fail)
- Progress indicators
- Detailed error reporting
- Execution time tracking
- Final summary report

---

## Prerequisites

### 1. Python Installation
Make sure Python 3.7+ is installed:
```bash
python --version
```

If not installed, download from [python.org](https://www.python.org/downloads/)

### 2. Install Selenium
```bash
pip install selenium
```

### 3. ChromeDriver Setup
The tests use Chrome browser. You have two options:

#### Option A: Using webdriver-manager (Recommended)
```bash
pip install webdriver-manager
```

Then modify the driver initialization in the script:
```python
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

#### Option B: Manual ChromeDriver Installation
1. Check your Chrome version: Settings → About Google Chrome
2. Download ChromeDriver matching your version from: https://chromedriver.chromium.org/
3. Place chromedriver.exe in one of these locations:
   - System PATH
   - Project root directory
   - Python Scripts folder

### 4. Verify Selenium Installation
```bash
python -c "from selenium import webdriver; print('Selenium installed successfully')"
```

---

## Application Setup

### Backend Setup
```bash
cd backend

# Install dependencies
npm install

# Start backend server (development mode)
npm run dev
# Server runs on: http://localhost:5000
```

### Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start frontend server (development mode)
npm run dev
# App runs on: http://localhost:5173
```

**⚠️ IMPORTANT:** Both backend and frontend MUST be running before executing tests.

---

## Running the Tests

### Run Basic Test Suite
```bash
cd d:\webdev\book-store-mern-project

python test_selenium_script.py
```

**Expected Output:**
```
================================================================================
BOOK STORE MERN PROJECT SELENIUM TEST SUITE STARTED
================================================================================

[HH:MM:SS] [START] 🚀 BOOK STORE MERN PROJECT SELENIUM TEST SUITE STARTED
================================================================================

[HH:MM:SS] [TEST] TEST 1: HOMEPAGE LOAD
...
```

### Run Advanced Test Suite (Recommended)
```bash
cd d:\webdev\book-store-mern-project

python test_selenium_advanced.py
```

**Expected Output:**
```
================================================================================
ADVANCED SELENIUM TESTING SUITE - BOOK STORE MERN PROJECT
================================================================================

[  0.5s] [TEST] TEST 1: Checking application connectivity...
[  1.2s] [INFO] Connecting to http://localhost:5173
[  2.1s] [PASS] ✓ Application is accessible and responding
...
```

### Run with Custom Base URL
If your app runs on a different port:

#### For basic suite, edit line ~38:
```python
self.base_url = "http://localhost:YOUR_PORT"
```

#### For advanced suite, run with parameter:
```python
# Edit line ~165 in the file and change:
def __init__(self, base_url="http://localhost:YOUR_PORT"):
```

---

## Test Cases Explained

### Basic Suite Tests (test_selenium_script.py)

| # | Test Name | Purpose |
|---|-----------|---------|
| 1 | Homepage Load | Verify homepage loads and navbar is present |
| 2 | Navbar Functionality | Check all navigation links and elements |
| 3 | Browse Books | Scroll and view book listings |
| 4 | Single Book View | Click and navigate to individual book pages |
| 5 | Add to Cart | Verify add-to-cart button availability |
| 6 | View Cart | Navigate to cart page |
| 7 | Login Page | Verify login form and fields |
| 8 | Register Page | Verify registration form and fields |
| 9 | Page Navigation | Test back/forward navigation |
| 10 | Page Elements | Verify responsive design and element count |

### Advanced Suite Tests (test_selenium_advanced.py)

**Phase 1: Initialization (0-15s)**
- Test application connectivity
- Verify page load completeness
- Check browser console status

**Phase 2: UI Elements (15-30s)**
- Navigation bar verification
- Footer detection and checking
- Responsive design validation

**Phase 3: Content (30-60s)**
- Homepage content analysis
- Scroll behavior testing
- Image loading verification

**Phase 4: User Flow (60-90s)**
- Book browsing functionality
- Page links enumeration
- Form page validation

**Phase 5: Extended Verification (90-120+s)**
- Dynamic content loading
- Page transitions
- Final system checks with performance metrics

---

## Understanding Test Output

### Status Indicators
- ✓ = Test Passed
- ✗ = Test Failed
- ⚠️ = Warning (non-critical issue)
- ℹ️ = Information/Debug message

### Log Levels
```
[INFO]   - Information message
[PASS]   - Test passed successfully
[FAIL]   - Test failed
[WARN]   - Warning (non-critical)
[TEST]   - Test case header
[ERROR]  - Critical error
[START]  - Suite started
[SUMMARY] - Final summary
```

### Timestamps
Each message includes:
- Elapsed time (in advanced suite): [6.2s]
- Message type: [INFO], [PASS], etc.
- Actual message

---

## Common Issues and Solutions

### Issue: "No such element: could not locate element"
**Solution:** 
- Ensure frontend is running on http://localhost:5173
- Check that all page elements load properly
- Wait time might be too short - check network latency

### Issue: "Connection refused" or "Failed to connect"
**Solution:**
```bash
# Make sure both servers are running
# Terminal 1 - Backend
cd backend
npm run dev

# Terminal 2 - Frontend  
cd frontend
npm run dev
```

### Issue: "ChromeDriver version mismatch"
**Solution:**
```bash
# Use webdriver-manager for automatic version sync
pip install webdriver-manager

# Update the script to use webdriver-manager
```

### Issue: "Permission denied: chromedriver"
**Solution (Windows):**
```bash
# Make sure chromedriver.exe has execution permissions
# Place it in the project root or Python Scripts folder
```

### Issue: "Tests timeout after 10 seconds"
**Solution:**
- Check network speed and application response time
- Increase wait timeout in scripts (default: 10 seconds)
- Verify backend is responsive with: `curl http://localhost:5000`

---

## Test Execution Timeline

### Basic Suite (~3-5 minutes)
```
0:00 - Application connectivity
0:30 - Navbar testing
1:00 - Book browsing
1:30 - Single book view
2:00 - Add to cart
2:30 - Cart page
3:00 - Login page
3:30 - Register page
4:00 - Navigation
4:30 - Page elements & summary
```

### Advanced Suite (~2-3 minutes)
```
0:00 - Phase 1: Initialization
0:15 - Phase 2: UI Elements
0:30 - Phase 3: Content
1:00 - Phase 4: User Flow
1:30 - Phase 5: Extended Verification
2:00+ - Report generation
```

---

## Customization

### Modify Test Cases
Edit the test methods in either script:

```python
def test_custom_feature(self):
    """Test your custom feature"""
    self.print_alert("TEST X: YOUR CUSTOM TEST", "TEST")
    try:
        # Your test code here
        self.test_step_completed("Your Feature Test", duration=1)
        self.passed_count += 1
    except Exception as e:
        self.test_failed("Your Feature Test", str(e))
```

### Add New Test Steps
```python
# In advanced suite
def test_your_feature(self):
    self.log("TEST X: Testing your feature...", "TEST")
    try:
        # Test implementation
        self.log("✓ Feature working correctly", "PASS")
    except Exception as e:
        self.log(f"✗ Feature test failed: {str(e)}", "FAIL")
```

### Change Wait Times
```python
# Default wait time (10 seconds)
self.wait = WebDriverWait(self.driver, 10)

# Change to 20 seconds for slower connections
self.wait = WebDriverWait(self.driver, 20)
```

---

## Performance Metrics

The advanced suite provides:
- **Page Load Time**: Time from navigation to complete load
- **DOM Ready Time**: Time until DOM content is fully loaded
- **Element Counts**: Total images, links, buttons detected
- **Scroll Performance**: Scrolling responsiveness
- **Navigation Performance**: Page transition speeds

---

## CI/CD Integration

### GitHub Actions Example
```yaml
name: Selenium Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install selenium webdriver-manager
      - run: npm ci --prefix backend
      - run: npm run dev --prefix backend &
      - run: npm ci --prefix frontend
      - run: npm run dev --prefix frontend &
      - run: sleep 5
      - run: python test_selenium_advanced.py
```

---

## Best Practices

1. **Always verify both servers are running** before executing tests
2. **Use the advanced suite** for comprehensive testing
3. **Check browser console** for JavaScript errors (tools included)
4. **Run tests on clean browser sessions** for consistent results
5. **Monitor network activity** to identify slow API calls
6. **Keep ChromeDriver updated** for compatibility
7. **Use explicit waits** instead of sleep() when possible (already done)
8. **Document custom tests** with clear descriptions

---

## Troubleshooting Script

Save as `verify_setup.py` to check your environment:

```python
#!/usr/bin/env python
"""Verify Selenium test environment"""

def check_selenium():
    try:
        from selenium import webdriver
        print("✓ Selenium installed")
    except:
        print("✗ Selenium not installed: pip install selenium")

def check_chromedriver():
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        print("✓ WebDriver Manager installed")
    except:
        print("ℹ Install: pip install webdriver-manager")

def check_python():
    import sys
    print(f"✓ Python {sys.version}")

def check_connectivity():
    import socket
    try:
        socket.create_connection(("localhost", 5173), timeout=2)
        print("✓ Frontend server accessible (localhost:5173)")
    except:
        print("✗ Frontend not running on localhost:5173")

if __name__ == "__main__":
    print("\n🔍 Selenium Test Environment Check\n")
    check_python()
    check_selenium()
    check_chromedriver()
    check_connectivity()
    print("\n✓ Setup check complete\n")
```

---

## Support & Documentation

- **Selenium Documentation**: https://www.selenium.dev/documentation/
- **Python Unittest**: https://docs.python.org/3/library/unittest.html
- **Chrome DevTools**: https://developer.chrome.com/docs/devtools/
- **Project Issues**: Check browser console for JavaScript errors

---

## License
These test scripts are provided for testing the Book Store MERN Project.

---

## Notes

- Tests run in headless mode can be enabled by adding `--headless` to the WebDriver initialization
- Screenshots on failure can be captured by adding `self.driver.save_screenshot()`
- Videos can be recorded by specifying a recording option in WebDriver
- Tests are non-destructive and don't modify database records (they verify, not create actual orders)

---

**Last Updated**: 2024
**Version**: 1.0
**Compatibility**: Python 3.7+, Selenium 4.0+, Chrome 90+
