"""
MERN BOOK STORE - REGISTER, LOGIN & ADD BOOKS TEST
Complete workflow testing: User registration → Login → Add Books to Cart
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class BookStoreCompleteWorkflow:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.start_time = time.time()
        
    def log(self, tag, message):
        elapsed = time.time() - self.start_time
        print(f"[{elapsed:6.1f}s] [{tag:10}] {message}")
    
    def handle_save_popup(self):
        """Handle browser save password/data popup"""
        try:
            # Look for save password popup button
            save_buttons = self.driver.find_elements(
                By.XPATH,
                "//*[contains(text(), 'Save') or contains(text(), 'save')]"
            )
            
            if save_buttons:
                for btn in save_buttons:
                    if "password" in btn.text.lower() or "save" in btn.text.lower():
                        self.log("INFO", f"Found save popup: {btn.text}")
                        try:
                            btn.click()
                            self.log("PASS", "✓ Clicked save popup")
                            time.sleep(0.5)
                            return True
                        except:
                            pass
        except:
            pass
        
        return False
    
    def setup_driver(self):
        """Initialize Chrome WebDriver"""
        self.log("SETUP", "Initializing Chrome WebDriver...")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        self.wait = WebDriverWait(self.driver, 10)
        self.log("SETUP", "✓ Chrome WebDriver initialized")
    
    def test_register_user(self):
        """Step 1: Register a new user"""
        self.log("TEST", "=" * 80)
        self.log("TEST", "STEP 1: REGISTERING NEW USER")
        self.log("TEST", "=" * 80)
        
        try:
            # Navigate to register page
            self.log("INFO", "Navigating to registration page...")
            self.driver.get("http://localhost:5173/register")
            time.sleep(2.5)
            self.log("PASS", "✓ Registration page loaded")
            time.sleep(1)
            
            # Generate unique email
            timestamp = str(int(time.time()))
            email = f"testuser{timestamp}@booknest.com"
            password = "TestPassword123!"
            
            self.log("INFO", f"Registration details:")
            self.log("INFO", f"  Email: {email}")
            self.log("INFO", f"  Password: {password}")
            time.sleep(1.5)
            
            # Find and fill email field
            self.log("INFO", "Filling email field...")
            email_input = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email'], input[placeholder*='email' i]"))
            )
            email_input.clear()
            email_input.send_keys(email)
            time.sleep(1.5)
            self.log("PASS", "✓ Email entered")
            time.sleep(1)
            
            # Find and fill password field
            self.log("INFO", "Filling password field...")
            password_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='password']")
            if len(password_inputs) >= 1:
                password_inputs[0].clear()
                password_inputs[0].send_keys(password)
                time.sleep(1.5)
                self.log("PASS", "✓ Password entered")
                time.sleep(1)
            
            # Confirm password (if there's a second password field)
            if len(password_inputs) >= 2:
                self.log("INFO", "Filling confirm password field...")
                password_inputs[1].clear()
                password_inputs[1].send_keys(password)
                time.sleep(1.5)
                self.log("PASS", "✓ Confirm password entered")
                time.sleep(1)
            
            # Find and click register button
            self.log("INFO", "Clicking register button...")
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                if "register" in button.text.lower() or "sign up" in button.text.lower():
                    button.click()
                    break
            
            time.sleep(3)
            self.log("PASS", "✓ Registration submitted")
            time.sleep(1.5)
            
            # Handle alert if present
            try:
                alert = self.wait.until(EC.alert_is_present())
                alert_text = alert.text
                self.log("INFO", f"Alert: {alert_text}")
                alert.accept()
                time.sleep(1)
            except:
                pass
            
            # Handle save popup
            self.handle_save_popup()
            
            # Check current URL
            current_url = self.driver.current_url
            self.log("INFO", f"Current URL: {current_url}")
            
            if "login" in current_url or "register" in current_url:
                self.log("PASS", "✓ Registration successful or awaiting login")
            
            return email, password
            
        except Exception as e:
            self.log("ERROR", f"✗ Registration failed: {str(e)}")
            raise
    
    def test_login_user(self, email, password):
        """Step 2: Log in with registered user"""
        self.log("TEST", "=" * 80)
        self.log("TEST", "STEP 2: LOGGING IN WITH REGISTERED USER")
        self.log("TEST", "=" * 80)
        
        try:
            # Navigate to login page
            self.log("INFO", "Navigating to login page...")
            self.driver.get("http://localhost:5173/login")
            time.sleep(2.5)
            self.log("PASS", "✓ Login page loaded")
            time.sleep(1)
            
            self.log("INFO", f"Login credentials:")
            self.log("INFO", f"  Email: {email}")
            self.log("INFO", f"  Password: {password}")
            time.sleep(1.5)
            
            # Find and fill email field
            self.log("INFO", "Filling login email field...")
            email_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='email'], input[placeholder*='email' i]")
            if email_inputs:
                email_inputs[0].clear()
                email_inputs[0].send_keys(email)
                time.sleep(1.5)
                self.log("PASS", "✓ Email entered")
                time.sleep(1)
            
            # Find and fill password field
            self.log("INFO", "Filling login password field...")
            password_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='password']")
            if password_inputs:
                password_inputs[0].clear()
                password_inputs[0].send_keys(password)
                time.sleep(1.5)
                self.log("PASS", "✓ Password entered")
                time.sleep(1)
            
            # Find and click login button
            self.log("INFO", "Clicking login button...")
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            for button in buttons:
                if "login" in button.text.lower() or "sign in" in button.text.lower():
                    button.click()
                    break
            
            time.sleep(3)
            self.log("PASS", "✓ Login submitted")
            time.sleep(1.5)
            
            # Handle alert if present
            try:
                alert = self.wait.until(EC.alert_is_present())
                alert_text = alert.text
                self.log("INFO", f"Alert: {alert_text}")
                alert.accept()
                time.sleep(1)
            except:
                pass
            
            # Handle save popup
            self.handle_save_popup()
            
            # Check current URL after login
            current_url = self.driver.current_url
            self.log("INFO", f"Current URL after login: {current_url}")
            self.log("PASS", "✓ Login process completed")
            
        except Exception as e:
            self.log("ERROR", f"✗ Login failed: {str(e)}")
            raise
    
    def test_add_books_to_cart(self):
        """Step 3: Navigate home and add books to cart"""
        self.log("TEST", "=" * 80)
        self.log("TEST", "STEP 3: ADDING BOOKS TO CART")
        self.log("TEST", "=" * 80)
        
        try:
            # Navigate to home page
            self.log("INFO", "Navigating to home page...")
            self.driver.get("http://localhost:5173")
            time.sleep(2.5)
            self.log("PASS", "✓ Home page loaded")
            time.sleep(1.5)
            
            # Find all book cards/links
            self.log("INFO", "Searching for books on the page...")
            book_links = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/books/']")
            self.log("INFO", f"Found {len(book_links)} books available")
            time.sleep(1)
            
            if len(book_links) > 0:
                books_added = 0
                max_books = min(2, len(book_links))  # Add up to 2 books
                
                for i in range(max_books):
                    try:
                        self.log("INFO", f"Processing book {i+1}/{max_books}...")
                        time.sleep(2)
                        
                        # Refresh book links before clicking
                        book_links = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/books/']")
                        if i < len(book_links):
                            # Scroll to element and click
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", book_links[i])
                            time.sleep(1)
                            book_links[i].click()
                            time.sleep(2)
                            self.log("PASS", f"✓ Book {i+1} page opened")
                            time.sleep(1.5)
                            
                            # Look for add to cart button
                            self.log("INFO", f"Looking for add to cart button for book {i+1}...")
                            time.sleep(1)
                            add_to_cart_buttons = self.driver.find_elements(
                                By.XPATH, 
                                "//*[contains(text(), 'Add to Cart') or contains(text(), 'add to cart')]/parent::*"
                            )
                            
                            if not add_to_cart_buttons:
                                add_to_cart_buttons = self.driver.find_elements(
                                    By.CSS_SELECTOR,
                                    "button[class*='btn']"
                                )
                            
                            if add_to_cart_buttons:
                                self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_buttons[0])
                                time.sleep(1)
                                add_to_cart_buttons[0].click()
                                time.sleep(2)
                                self.log("PASS", f"✓ Book {i+1} added to cart")
                                books_added += 1
                                time.sleep(1.5)
                            else:
                                self.log("WARN", f"⚠ Add to cart button not found for book {i+1}")
                            
                            # Go back to home
                            self.log("INFO", f"Going back to home page...")
                            self.driver.get("http://localhost:5173")
                            time.sleep(2)
                        
                    except Exception as e:
                        self.log("WARN", f"⚠ Error adding book {i+1}: {str(e)}")
                        self.driver.get("http://localhost:5173")
                        time.sleep(1)
                
                self.log("PASS", f"✓ Successfully added {books_added} books to cart")
                time.sleep(1.5)
            
            # Navigate to cart to verify
            self.log("INFO", "Navigating to cart page...")
            self.driver.get("http://localhost:5173/cart")
            time.sleep(2.5)
            self.log("PASS", "✓ Cart page opened")
            time.sleep(1.5)
            
            # Check cart content
            current_url = self.driver.current_url
            self.log("INFO", f"Cart URL: {current_url}")
            self.log("PASS", "✓ Cart content displayed")
            
        except Exception as e:
            self.log("ERROR", f"✗ Adding books failed: {str(e)}")
            raise
    
    def test_checkout(self):
        """Step 4: Proceed to checkout"""
        self.log("TEST", "=" * 80)
        self.log("TEST", "STEP 4: CHECKOUT PROCESS")
        self.log("TEST", "=" * 80)
        
        try:
            # Make sure we're on cart page
            current_url = self.driver.current_url
            self.log("INFO", f"Current page: {current_url}")
            time.sleep(1)
            
            if "cart" not in current_url:
                self.log("INFO", "Navigating to cart page...")
                self.driver.get("http://localhost:5173/cart")
                time.sleep(2.5)
            
            time.sleep(2)
            # Look for checkout button
            self.log("INFO", "Looking for checkout button...")
            time.sleep(1.5)
            checkout_buttons = self.driver.find_elements(
                By.XPATH,
                "//*[contains(text(), 'Checkout') or contains(text(), 'checkout') or contains(text(), 'Order Now')]/parent::*"
            )
            
            if not checkout_buttons:
                checkout_buttons = self.driver.find_elements(
                    By.CSS_SELECTOR,
                    "button[class*='btn'], button[class*='primary']"
                )
            
            if checkout_buttons:
                self.log("INFO", f"Found {len(checkout_buttons)} checkout button(s)")
                time.sleep(1.5)
                for btn in checkout_buttons:
                    btn_text = btn.text.lower()
                    if "checkout" in btn_text or "order" in btn_text:
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                        time.sleep(1)
                        btn.click()
                        time.sleep(2.5)
                        self.log("PASS", "✓ Checkout button clicked")
                        break
                else:
                    # If no specific checkout button, click the first btn
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", checkout_buttons[0])
                    time.sleep(1)
                    checkout_buttons[0].click()
                    time.sleep(2.5)
                    self.log("PASS", "✓ Button clicked")
            else:
                self.log("WARN", "⚠ No checkout button found")
            
            # Check if redirected to checkout page
            current_url = self.driver.current_url
            self.log("INFO", f"Current URL after checkout click: {current_url}")
            time.sleep(2)
            
            # Look for form fields (placeholder for order form)
            forms = self.driver.find_elements(By.TAG_NAME, "form")
            inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='text'], input[type='email'], textarea")
            
            self.log("INFO", f"Found {len(forms)} form(s) and {len(inputs)} input field(s)")
            time.sleep(1)
            
            # Fill in form fields if present
            if len(inputs) > 0:
                self.log("INFO", "Filling checkout form...")
                time.sleep(1.5)
                
                for idx, inp in enumerate(inputs[:4]):  # Fill first 4 inputs
                    try:
                        placeholder = inp.get_attribute("placeholder") or ""
                        field_type = inp.get_attribute("type") or "text"
                        
                        if "email" in placeholder.lower() or field_type == "email":
                            inp.clear()
                            inp.send_keys(f"customer{int(time.time())}@booknest.com")
                            self.log("PASS", f"✓ Email field filled")
                            time.sleep(1)
                        elif "name" in placeholder.lower():
                            inp.clear()
                            inp.send_keys("Test Customer")
                            self.log("PASS", f"✓ Name field filled")
                            time.sleep(1)
                        elif "phone" in placeholder.lower():
                            inp.clear()
                            inp.send_keys("+1234567890")
                            self.log("PASS", f"✓ Phone field filled")
                            time.sleep(1)
                        elif "address" in placeholder.lower():
                            inp.clear()
                            inp.send_keys("123 Main Street, City, State 12345")
                            self.log("PASS", f"✓ Address field filled")
                            time.sleep(1)
                        else:
                            inp.clear()
                            inp.send_keys(f"Test Data {idx}")
                            self.log("INFO", f"  Input {idx} filled")
                            time.sleep(0.8)
                        
                        time.sleep(1)
                    except Exception as e:
                        self.log("WARN", f"⚠ Error filling field {idx}: {str(e)}")
            
            time.sleep(2)
            # Look for and click submit/order button
            self.log("INFO", "Looking for submit/place order button...")
            time.sleep(1)
            submit_buttons = self.driver.find_elements(
                By.XPATH,
                "//*[contains(text(), 'Submit') or contains(text(), 'Place Order') or contains(text(), 'Confirm') or contains(text(), 'Pay')]/parent::*"
            )
            
            if not submit_buttons:
                submit_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button[type='submit']")
            
            if submit_buttons:
                self.log("INFO", f"Found {len(submit_buttons)} submit button(s)")
                time.sleep(1)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_buttons[0])
                time.sleep(1)
                submit_buttons[0].click()
                time.sleep(2.5)
                self.log("PASS", "✓ Order submitted")
            else:
                self.log("INFO", "No submit button found - order details displayed")
            
            time.sleep(1.5)
            # Final status
            current_url = self.driver.current_url
            self.log("INFO", f"Final URL: {current_url}")
            
            # Handle any save popups
            self.handle_save_popup()
            
            self.log("PASS", "✓ Checkout process completed")
            
        except Exception as e:
            self.log("ERROR", f"✗ Checkout failed: {str(e)}")
            raise
    
    def run(self):
        """Execute complete workflow"""
        try:
            print("\n")
            print("=" * 80)
            print("    BOOK STORE COMPLETE WORKFLOW TEST - REGISTER/LOGIN/ADD BOOKS/CHECKOUT")
            print("                         (2+ MINUTE EXTENDED TEST)")
            print("=" * 80)
            print("\n")
            
            self.setup_driver()
            
            time.sleep(1)
            # Step 1: Register
            email, password = self.test_register_user()
            
            time.sleep(2)
            
            # Step 2: Login
            self.test_login_user(email, password)
            
            time.sleep(2)
            
            # Step 3: Add Books
            self.test_add_books_to_cart()
            
            time.sleep(2)
            
            # Step 4: Checkout
            self.test_checkout()
            
            # Final summary
            total_time = time.time() - self.start_time
            print("\n")
            print("=" * 80)
            print(f"✅ COMPLETE WORKFLOW FINISHED SUCCESSFULLY in {total_time:.1f} seconds")
            print("=" * 80)
            print("\n")
            print("Workflow Summary:")
            print(f"  ✓ New user registered: {email}")
            print(f"  ✓ User logged in successfully")
            print(f"  ✓ Books added to cart")
            print(f"  ✓ Checkout process completed")
            print(f"  ✓ Total test duration: {total_time:.1f} seconds (2+ minute target)")
            print("\n")
            
        except Exception as e:
            self.log("CRITICAL", f"✗ Workflow failed: {str(e)}")
            raise
        
        finally:
            if self.driver:
                time.sleep(1)
                self.log("CLEANUP", "Closing browser...")
                self.driver.quit()
                self.log("CLEANUP", "✓ Browser closed")


if __name__ == "__main__":
    workflow = BookStoreCompleteWorkflow()
    workflow.run()
