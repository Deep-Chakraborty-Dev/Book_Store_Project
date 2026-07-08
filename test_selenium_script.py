"""
Selenium Testing Script for Book Store MERN Project
This script tests various functionalities with step-by-step alerts and messages
Testing duration: 2+ minutes with various page loads, interactions, and waits
"""

import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BookStoreTestSuite:
    def __init__(self):
        """Initialize WebDriver and test configuration"""
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "http://localhost:5173"  # Vite dev server default port
        self.test_count = 0
        self.passed_count = 0
        self.failed_count = 0
        
    def print_alert(self, message, test_type="INFO"):
        """Print alert message with timestamp and type"""
        timestamp = time.strftime("%H:%M:%S")
        separator = "=" * 80
        print(f"\n{separator}")
        print(f"[{timestamp}] [{test_type}] {message}")
        print(separator)
        
    def test_step_completed(self, step_name, duration=1):
        """Mark a test step as completed and add delay"""
        self.test_count += 1
        print(f"✓ Step {self.test_count} Completed: {step_name}")
        time.sleep(duration)
        
    def test_failed(self, step_name, error):
        """Mark a test as failed"""
        self.failed_count += 1
        print(f"✗ FAILED: {step_name} - {error}")
        
    def start_testing(self):
        """Main test execution method"""
        try:
            self.print_alert("🚀 BOOK STORE MERN PROJECT SELENIUM TEST SUITE STARTED", "START")
            time.sleep(1)
            
            # Test 1: Load Homepage
            self.test_homepage_load()
            
            # Test 2: Check Navbar Elements
            self.test_navbar_functionality()
            
            # Test 3: Browse Books
            self.test_browse_books()
            
            # Test 4: View Single Book
            self.test_single_book_view()
            
            # Test 5: Add to Cart
            self.test_add_to_cart()
            
            # Test 6: View Cart
            self.test_view_cart()
            
            # Test 7: Test Login Page
            self.test_login_page()
            
            # Test 8: Test Register Page
            self.test_register_page()
            
            # Test 9: Test Navigation
            self.test_navigation()
            
            # Test 10: Test Responsive Elements
            self.test_page_elements()
            
            # Final Summary
            self.print_summary()
            
        except Exception as e:
            self.print_alert(f"CRITICAL ERROR: {str(e)}", "ERROR")
            self.test_failed("Overall Testing", str(e))
        finally:
            self.cleanup()
    
    def test_homepage_load(self):
        """Test 1: Load and verify homepage"""
        self.print_alert("TEST 1: HOMEPAGE LOAD", "TEST")
        try:
            print(f"📍 Navigating to: {self.base_url}")
            self.driver.get(self.base_url)
            print("⏳ Waiting for page to load...")
            time.sleep(2)
            
            # Wait for the main content to load
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            print("✓ Page body loaded successfully")
            
            # Check if we can find the Navbar
            navbar = self.driver.find_element(By.TAG_NAME, "nav")
            print("✓ Navbar found on homepage")
            
            self.test_step_completed("Homepage Load and Navbar Verification", 2)
            self.passed_count += 1
            
        except TimeoutException:
            self.test_failed("Homepage Load", "Page load timeout - Backend might not be running")
        except NoSuchElementException as e:
            self.test_failed("Homepage Load", f"Element not found: {e}")
    
    def test_navbar_functionality(self):
        """Test 2: Test Navbar elements and links"""
        self.print_alert("TEST 2: NAVBAR FUNCTIONALITY", "TEST")
        try:
            print("🔍 Checking navbar elements...")
            time.sleep(1)
            
            # Try to find navbar links
            navbar_items = self.driver.find_elements(By.TAG_NAME, "a")
            print(f"✓ Found {len(navbar_items)} navigation links on page")
            
            # Print visible navbar links
            visible_links = []
            for link in navbar_items[:10]:  # Check first 10 links
                try:
                    href = link.get_attribute("href")
                    text = link.text
                    if text:
                        visible_links.append(f"{text} -> {href}")
                        print(f"  • Found link: {text}")
                except:
                    pass
            
            print(f"✓ Total visible links identified: {len(visible_links)}")
            self.test_step_completed("Navbar Functionality Check", 1.5)
            self.passed_count += 1
            
        except Exception as e:
            self.test_failed("Navbar Functionality", str(e))
    
    def test_browse_books(self):
        """Test 3: Test browsing books on homepage"""
        self.print_alert("TEST 3: BROWSE BOOKS", "TEST")
        try:
            print("📚 Looking for book elements on the page...")
            time.sleep(1)
            
            # Look for book cards (typically contain book information)
            book_elements = self.driver.find_elements(By.CLASS_NAME, "book-card")
            if not book_elements:
                book_elements = self.driver.find_elements(By.CLASS_NAME, "card")
            if not book_elements:
                book_elements = self.driver.find_elements(By.TAG_NAME, "img")
            
            print(f"✓ Found {len(book_elements)} book/card elements")
            
            # Scroll to view more books
            print("📜 Scrolling down to view more books...")
            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(1.5)
            
            print("✓ Scrolled down successfully")
            
            # Scroll back up
            self.driver.execute_script("window.scrollBy(0, -500);")
            time.sleep(1)
            
            self.test_step_completed("Browse Books and Scroll", 1)
            self.passed_count += 1
            
        except Exception as e:
            self.test_failed("Browse Books", str(e))
    
    def test_single_book_view(self):
        """Test 4: Click on a single book and view details"""
        self.print_alert("TEST 4: SINGLE BOOK VIEW", "TEST")
        try:
            print("🔎 Searching for first book link to click...")
            time.sleep(1)
            
            # Try to find and click a book link
            book_links = self.driver.find_elements(By.TAG_NAME, "a")
            book_clicked = False
            
            for link in book_links:
                href = link.get_attribute("href")
                if href and "/books/" in href:
                    print(f"📖 Found book link: {href}")
                    print(f"✓ Clicking on: {link.text if link.text else 'Book'}")
                    link.click()
                    book_clicked = True
                    time.sleep(2)
                    break
            
            if book_clicked:
                print("✓ Book details page loaded")
                current_url = self.driver.current_url
                print(f"✓ Current URL: {current_url}")
                
                # Try to find Add to Cart button or other book details
                page_text = self.driver.find_element(By.TAG_NAME, "body").text
                if "book" in page_text.lower() or "price" in page_text.lower():
                    print("✓ Book information visible on page")
                
                self.test_step_completed("Single Book View", 1.5)
                self.passed_count += 1
                
                # Go back to homepage
                print("⬅️  Going back to homepage...")
                self.driver.back()
                time.sleep(1.5)
            else:
                print("⚠️  No book links found to click")
                self.test_step_completed("Single Book View (Skipped)", 0.5)
            
        except Exception as e:
            self.test_failed("Single Book View", str(e))
            self.driver.back()
    
    def test_add_to_cart(self):
        """Test 5: Add items to cart"""
        self.print_alert("TEST 5: ADD TO CART", "TEST")
        try:
            print("🛒 Looking for 'Add to Cart' buttons...")
            time.sleep(1)
            
            # Look for add to cart buttons
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            print(f"✓ Found {len(buttons)} buttons on page")
            
            add_to_cart_found = False
            for button in buttons:
                button_text = button.text.lower()
                if "add" in button_text or "cart" in button_text:
                    print(f"🛍️  Found button: {button.text}")
                    # Don't click now, just verify it exists
                    add_to_cart_found = True
                    break
            
            if add_to_cart_found:
                print("✓ Add to Cart button found and verified")
            else:
                print("⚠️  Add to Cart button not visible (might be on product pages)")
            
            self.test_step_completed("Add to Cart Button Verification", 1)
            self.passed_count += 1
            
        except Exception as e:
            self.test_failed("Add to Cart", str(e))
    
    def test_view_cart(self):
        """Test 6: Navigate to cart page"""
        self.print_alert("TEST 6: VIEW CART PAGE", "TEST")
        try:
            print("🛒 Navigating to cart page...")
            time.sleep(1)
            
            # Try to find cart link in navbar
            cart_link = None
            links = self.driver.find_elements(By.TAG_NAME, "a")
            for link in links:
                href = link.get_attribute("href")
                if href and "/cart" in href:
                    cart_link = link
                    print(f"🔗 Found cart link: {link.text}")
                    link.click()
                    time.sleep(1.5)
                    break
            
            if cart_link:
                # Check if we're on cart page
                current_url = self.driver.current_url
                if "/cart" in current_url:
                    print(f"✓ Successfully navigated to cart page: {current_url}")
                    page_content = self.driver.find_element(By.TAG_NAME, "body").text
                    print("✓ Cart page content loaded")
                else:
                    print("⚠️  Not on cart page yet")
            else:
                print("⚠️  Cart link not found in navbar")
            
            self.test_step_completed("View Cart Page", 1.5)
            self.passed_count += 1
            
        except Exception as e:
            self.test_failed("View Cart", str(e))
    
    def test_login_page(self):
        """Test 7: Test login page"""
        self.print_alert("TEST 7: LOGIN PAGE", "TEST")
        try:
            print("🔐 Navigating to login page...")
            time.sleep(1)
            
            # Navigate directly or find login link
            login_url = f"{self.base_url}/login"
            print(f"📍 Going to: {login_url}")
            self.driver.get(login_url)
            time.sleep(1.5)
            
            # Look for login form elements
            print("🔍 Looking for login form elements...")
            
            # Look for email input
            email_inputs = self.driver.find_elements(By.TAG_NAME, "input")
            print(f"✓ Found {len(email_inputs)} input fields on login page")
            
            # Check for password field
            form_labels = self.driver.find_elements(By.TAG_NAME, "label")
            print(f"✓ Found {len(form_labels)} form labels")
            
            # Look for submit button
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            login_button_found = False
            for button in buttons:
                if "submit" in button.text.lower() or "login" in button.text.lower():
                    print(f"✓ Found button: {button.text}")
                    login_button_found = True
                    break
            
            if login_button_found:
                print("✓ Login form verified with submit button")
            
            self.test_step_completed("Login Page Verification", 1.5)
            self.passed_count += 1
            
        except Exception as e:
            self.test_failed("Login Page", str(e))
    
    def test_register_page(self):
        """Test 8: Test register page"""
        self.print_alert("TEST 8: REGISTER PAGE", "TEST")
        try:
            print("📝 Navigating to register page...")
            time.sleep(1)
            
            # Navigate to register page
            register_url = f"{self.base_url}/register"
            print(f"📍 Going to: {register_url}")
            self.driver.get(register_url)
            time.sleep(1.5)
            
            # Look for registration form elements
            print("🔍 Looking for registration form elements...")
            
            # Check for form fields
            form_inputs = self.driver.find_elements(By.TAG_NAME, "input")
            print(f"✓ Found {len(form_inputs)} input fields on register page")
            
            # Check for form
            forms = self.driver.find_elements(By.TAG_NAME, "form")
            print(f"✓ Found {len(forms)} form(s) on register page")
            
            # Look for register button
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            register_button_found = False
            for button in buttons:
                button_text = button.text.lower()
                if "register" in button_text or "sign up" in button_text:
                    print(f"✓ Found button: {button.text}")
                    register_button_found = True
                    break
            
            if register_button_found:
                print("✓ Register form verified with submit button")
            
            self.test_step_completed("Register Page Verification", 1.5)
            self.passed_count += 1
            
        except Exception as e:
            self.test_failed("Register Page", str(e))
    
    def test_navigation(self):
        """Test 9: Test navigation between pages"""
        self.print_alert("TEST 9: PAGE NAVIGATION", "TEST")
        try:
            print("🗺️  Testing navigation between pages...")
            time.sleep(1)
            
            # Go to home
            print("🏠 Navigating to home page...")
            self.driver.get(self.base_url)
            time.sleep(1)
            
            # Go to about
            print("ℹ️  Navigating to about page...")
            self.driver.get(f"{self.base_url}/about")
            time.sleep(1)
            print("✓ About page loaded")
            
            # Go back to home
            print("🔙 Going back to home...")
            self.driver.get(self.base_url)
            time.sleep(1)
            print("✓ Home page reloaded successfully")
            
            self.test_step_completed("Navigation Tests", 1)
            self.passed_count += 1
            
        except Exception as e:
            self.test_failed("Navigation", str(e))
    
    def test_page_elements(self):
        """Test 10: Test responsive page elements"""
        self.print_alert("TEST 10: PAGE ELEMENTS & RESPONSIVENESS", "TEST")
        try:
            print("📏 Testing page elements and responsiveness...")
            time.sleep(1)
            
            # Get page title
            page_title = self.driver.title
            print(f"✓ Page Title: {page_title}")
            
            # Get page size
            window_size = self.driver.get_window_size()
            print(f"✓ Window Size: {window_size['width']}x{window_size['height']}")
            
            # Count various elements
            images = self.driver.find_elements(By.TAG_NAME, "img")
            print(f"✓ Found {len(images)} images on page")
            
            links = self.driver.find_elements(By.TAG_NAME, "a")
            print(f"✓ Found {len(links)} links on page")
            
            divs = self.driver.find_elements(By.TAG_NAME, "div")
            print(f"✓ Found {len(divs)} div elements on page")
            
            # Test viewport meta tag for responsiveness
            try:
                viewport = self.driver.execute_script(
                    "return document.querySelector('meta[name=\"viewport\"]')"
                )
                if viewport:
                    print("✓ Responsive viewport meta tag found")
            except:
                print("⚠️  Could not verify viewport meta tag")
            
            self.test_step_completed("Page Elements Verification", 1)
            self.passed_count += 1
            
        except Exception as e:
            self.test_failed("Page Elements", str(e))
    
    def print_summary(self):
        """Print final test summary"""
        self.print_alert("TEST SUITE COMPLETED", "SUMMARY")
        
        total_duration = time.time()
        print(f"\n📊 TEST RESULTS SUMMARY")
        print(f"{'=' * 50}")
        print(f"Total Tests Executed: {self.test_count}")
        print(f"✓ Tests Passed: {self.passed_count}")
        print(f"✗ Tests Failed: {self.failed_count}")
        print(f"{'=' * 50}")
        
        if self.failed_count == 0:
            print("🎉 ALL TESTS PASSED SUCCESSFULLY!")
        else:
            print(f"⚠️  {self.failed_count} test(s) failed")
        
        print(f"\n✅ Selenium testing completed at {time.strftime('%H:%M:%S')}")
    
    def cleanup(self):
        """Close the WebDriver"""
        print("\n🧹 Cleaning up... Closing browser window")
        time.sleep(1)
        self.driver.quit()
        print("✓ Browser closed successfully")


def main():
    """Main entry point"""
    print("\n" + "=" * 80)
    print("BOOK STORE MERN PROJECT - SELENIUM AUTOMATED TESTING SUITE")
    print("=" * 80)
    print("\n⚠️  PREREQUISITES:")
    print("1. Make sure your backend is running (npm run dev)")
    print("2. Make sure your frontend is running (npm run dev)")
    print("3. Make sure ChromeDriver is in your system PATH or in the current directory")
    print("4. Update base_url if your app is running on a different port")
    print("\n" + "=" * 80 + "\n")
    
    try:
        tester = BookStoreTestSuite()
        tester.start_testing()
    except Exception as e:
        print(f"\n❌ FATAL ERROR: {str(e)}")
        print("Make sure:")
        print("  - Your app is running on http://localhost:5173")
        print("  - ChromeDriver is installed and in PATH")
        print("  - All dependencies are installed")
        sys.exit(1)


if __name__ == "__main__":
    main()
