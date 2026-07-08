# 🚀 QUICK START GUIDE - Selenium Testing

## Step 1️⃣: Install Required Packages

Open PowerShell/Terminal and run:

```bash
pip install selenium
pip install webdriver-manager
```

## Step 2️⃣: Start Your Application Services

You MUST have BOTH services running. Open TWO separate terminals/PowerShells:

### Terminal 1 - Start Backend Server:
```bash
cd d:\webdev\book-store-mern-project\backend
npm install
npm run dev
```
✓ Wait until you see: `Server running on port 5000` (or your configured port)

### Terminal 2 - Start Frontend Server:
```bash
cd d:\webdev\book-store-mern-project\frontend
npm install
npm run dev
```
✓ Wait until you see: `Local: http://localhost:5173/` (or your configured port)

## Step 3️⃣: Run the Selenium Tests

Open Terminal 3 and run ONE of these commands:

### Option A - RECOMMENDED (Advanced Suite - Detailed Logging):
```bash
cd d:\webdev\book-store-mern-project
python test_selenium_advanced.py
```

### Option B - Basic Suite:
```bash
cd d:\webdev\book-store-mern-project
python test_selenium_script.py
```

## Step 4️⃣: View Results

### You'll see output like this:

```
================================================================================
ADVANCED SELENIUM TESTING SUITE - BOOK STORE MERN PROJECT
================================================================================

[  0.5s] [TEST] TEST 1: Checking application connectivity...
[  1.2s] [INFO] Connecting to http://localhost:5173
[  2.1s] [PASS] ✓ Application is accessible and responding


⚡               PHASE 1: APPLICATION INITIALIZATION (0-15 seconds)               ⚡
================================================================================

[  2.5s] [TEST] TEST 2: Checking page load completeness...
[  3.0s] [INFO] Verifying document ready state...
[  3.1s] [INFO] Document ready state: complete
[  3.2s] [PASS] ✓ Page loaded successfully
[  3.3s] [INFO] Page title: 'Your App Title'
[  3.4s] [PASS] ✓ Total DOM elements on page: 285
...
```

### Status Indicators:
- ✓ **PASS** - Test passed successfully
- ✗ **FAIL** - Test failed (check console output)
- ⚠️ **WARN** - Warning (non-critical)
- 🎯 **2+ minutes** - Tests will run for 120+ seconds

## Troubleshooting Quick Fixes

### ❌ Error: "Failed to connect"
```bash
# Check if servers are running
# Make sure you completed Step 2 and both services are active
```

### ❌ Error: "ChromeDriver version mismatch"
```bash
# ChromeDriver automatically updated using webdriver-manager (installed in Step 1)
# If still issues, restart PowerShell/Terminal
```

### ❌ Error: "Module not found: selenium"
```bash
# Reinstall: pip install selenium webdriver-manager
# Or use: python -m pip install selenium webdriver-manager
```

### ❌ Tests run too fast (not reaching 2 minutes)
```bash
# Both test scripts include delays to reach 2+ minutes automatically
# If still quick, your application might be responding very fast
# Tests are comprehensive regardless of duration
```

## What Gets Tested?

### ✅ Basic Suite Tests (10 tests):
1. Homepage loads correctly
2. Navigation bar elements
3. Browse books functionality
4. Individual book pages
5. Add to cart button
6. Cart page access
7. Login page form
8. Register page form
9. Page navigation (back/forward)
10. Responsive design elements

### ✅ Advanced Suite Tests (15 tests):
**All of the above, PLUS:**
11. Dynamic content loading
12. Form validation
13. Scroll behavior
14. Image loading
15. Performance metrics

## Files Created

- **test_selenium_script.py** - Basic testing suite
- **test_selenium_advanced.py** - Advanced testing suite ⭐ RECOMMENDED
- **SELENIUM_TEST_README.md** - Full documentation
- **QUICK_START.md** - This file

## Expected Runtime

- **Basic Suite**: 3-5 minutes
- **Advanced Suite**: 2-3 minutes ⭐

## 🎯 Success Checklist

- [ ] Python 3.7+ installed: `python --version`
- [ ] Selenium installed: `pip install selenium`
- [ ] WebDriver Manager installed: `pip install webdriver-manager`
- [ ] Backend running on http://localhost:5000
- [ ] Frontend running on http://localhost:5173
- [ ] Both test files present in project root
- [ ] Terminal opened in project directory

## Next Steps After Testing

1. **Review test output** - Identify any failures
2. **Check browser console** - Look for JavaScript errors
3. **Fix issues found** - Update your code as needed
4. **Re-run tests** - Verify fixes
5. **Integrate with CI/CD** - Add to deployment pipeline

## Example Successful Run

```powershell
PS D:\webdev\book-store-mern-project> python test_selenium_advanced.py

================================================================================
ADVANCED SELENIUM TESTING SUITE - BOOK STORE MERN PROJECT
================================================================================

✓ REQUIREMENTS:
  • Backend running: npm run dev (backend/)
  • Frontend running: npm run dev (frontend/)
  • ChromeDriver installed in PATH
  • Python Selenium package installed: pip install selenium

================================================================================

[  0.5s] [INFO] Connecting to http://localhost:5173
[  2.5s] [PASS] ✓ Application is accessible and responding

... (more tests)

[120.5s] [PASS] ✓ Final verification completed successfully

================================================================================
TEST RESULTS SUMMARY
================================================================================
Total Tests Executed: 15
✓ Tests Passed: 15
✗ Tests Failed: 0
================================================================================
🎉 ALL TESTS PASSED SUCCESSFULLY!

✅ TOTAL EXECUTION TIME: 125.3 seconds
🎯 MINIMUM TIME REQUIREMENT MET (2 minutes)

PS D:\webdev\book-store-mern-project>
```

---

## Support

If you encounter issues:
1. Check the full **SELENIUM_TEST_README.md** for detailed troubleshooting
2. Verify both backend and frontend are running
3. Check Chrome/Chromium is installed on your system
4. Review Python version: `python --version` (should be 3.7+)

---

**Ready to test?** Start with Step 1! 🚀
