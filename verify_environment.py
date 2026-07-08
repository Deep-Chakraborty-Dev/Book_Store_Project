"""
Environment Verification Script for Selenium Testing
Run this script first to verify your setup is correct
"""

import sys
import subprocess
import socket
import time
from pathlib import Path

class EnvironmentChecker:
    def __init__(self):
        self.issues = []
        self.warnings = []
        self.successes = []
        self.critical_error = False
        
    def print_header(self):
        """Print header"""
        print("\n" + "=" * 80)
        print("🔍 SELENIUM TEST ENVIRONMENT VERIFICATION TOOL".center(80))
        print("=" * 80 + "\n")
    
    def print_section(self, title):
        """Print section header"""
        print(f"\n{'─' * 80}")
        print(f"📋 {title}")
        print(f"{'─' * 80}\n")
    
    def log_success(self, message):
        """Log successful check"""
        print(f"✓ {message}")
        self.successes.append(message)
    
    def log_warning(self, message):
        """Log warning"""
        print(f"⚠️  {message}")
        self.warnings.append(message)
    
    def log_error(self, message, critical=False):
        """Log error"""
        print(f"✗ {message}")
        self.issues.append(message)
        if critical:
            self.critical_error = True
    
    def check_python_version(self):
        """Check Python version"""
        self.print_section("PYTHON VERSION CHECK")
        
        version = sys.version_info
        python_version = f"{version.major}.{version.minor}.{version.micro}"
        print(f"Installed Python version: {python_version}")
        
        if version.major >= 3 and version.minor >= 7:
            self.log_success(f"Python {python_version} (3.7+ required)")
        else:
            self.log_error(
                f"Python {python_version} is too old. Python 3.7+ required.",
                critical=True
            )
    
    def check_selenium_package(self):
        """Check if Selenium is installed"""
        self.print_section("SELENIUM PACKAGE CHECK")
        
        try:
            import selenium
            selenium_version = selenium.__version__
            print(f"Selenium version: {selenium_version}")
            self.log_success(f"Selenium {selenium_version} is installed")
            
            from selenium import webdriver
            self.log_success("Selenium WebDriver available")
        except ImportError as e:
            self.log_error(
                "Selenium is not installed. Run: pip install selenium",
                critical=True
            )
    
    def check_webdriver_manager(self):
        """Check if webdriver-manager is installed"""
        self.print_section("WEBDRIVER MANAGER CHECK")
        
        try:
            import webdriver_manager
            version = webdriver_manager.__version__
            print(f"WebDriver Manager version: {version}")
            self.log_success("WebDriver Manager is installed")
            
            from webdriver_manager.chrome import ChromeDriverManager
            self.log_success("Chrome driver manager available")
        except ImportError:
            self.log_warning(
                "WebDriver Manager not installed (optional but recommended): "
                "pip install webdriver-manager"
            )
    
    def check_chromedriver(self):
        """Check if ChromeDriver exists"""
        self.print_section("CHROMEDRIVER CHECK")
        
        # Try to find chromedriver
        chromedriver_paths = [
            "chromedriver",
            "chromedriver.exe",
            Path(__file__).parent / "chromedriver.exe",
            Path(__file__).parent / "chromedriver",
        ]
        
        found = False
        for path in chromedriver_paths:
            try:
                result = subprocess.run(
                    [str(path), "--version"],
                    capture_output=True,
                    timeout=5
                )
                if result.returncode == 0:
                    version = result.stdout.decode().strip()
                    print(f"ChromeDriver found: {path}")
                    print(f"Version: {version}")
                    self.log_success(f"ChromeDriver available: {version}")
                    found = True
                    break
            except:
                continue
        
        if not found:
            self.log_warning(
                "ChromeDriver not found in PATH. "
                "install webdriver-manager for automatic management: "
                "pip install webdriver-manager"
            )
    
    def check_chrome_browser(self):
        """Check if Chrome/Chromium is installed"""
        self.print_section("CHROME BROWSER CHECK")
        
        chrome_paths = [
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
            Path.home() / "AppData\\Local\\Google\\Chrome\\Application\\chrome.exe",
        ]
        
        found = False
        for path in chrome_paths:
            if Path(path).exists():
                print(f"Chrome found: {path}")
                self.log_success("Chrome browser installed")
                found = True
                break
        
        if not found:
            self.log_error(
                "Chrome browser not found. Install Chrome from google.com/chrome",
                critical=True
            )
    
    def check_backend_running(self):
        """Check if backend server is running"""
        self.print_section("BACKEND SERVER CHECK")
        
        print("Checking if backend is running on localhost:5000...")
        try:
            socket.create_connection(("localhost", 5000), timeout=2)
            self.log_success("Backend server is running on http://localhost:5000")
        except (socket.timeout, ConnectionRefusedError):
            self.log_warning(
                "Backend server not running on localhost:5000. "
                "Start it with: cd backend && npm run dev"
            )
    
    def check_frontend_running(self):
        """Check if frontend server is running"""
        self.print_section("FRONTEND SERVER CHECK")
        
        print("Checking if frontend is running on localhost:5173...")
        try:
            socket.create_connection(("localhost", 5173), timeout=2)
            self.log_success("Frontend server is running on http://localhost:5173")
        except (socket.timeout, ConnectionRefusedError):
            self.log_warning(
                "Frontend server not running on localhost:5173. "
                "Start it with: cd frontend && npm run dev"
            )
    
    def check_node_npm(self):
        """Check if Node.js and npm are installed"""
        self.print_section("NODE.JS & NPM CHECK")
        
        try:
            # Check Node.js
            node_result = subprocess.run(
                ["node", "--version"],
                capture_output=True,
                timeout=5
            )
            if node_result.returncode == 0:
                node_version = node_result.stdout.decode().strip()
                print(f"Node.js: {node_version}")
                self.log_success(f"Node.js installed: {node_version}")
            
            # Check npm
            npm_result = subprocess.run(
                ["npm", "--version"],
                capture_output=True,
                timeout=5
            )
            if npm_result.returncode == 0:
                npm_version = npm_result.stdout.decode().strip()
                print(f"npm: {npm_version}")
                self.log_success(f"npm installed: {npm_version}")
        except FileNotFoundError:
            self.log_error(
                "Node.js or npm not found. Install from nodejs.org",
                critical=True
            )
    
    def check_project_files(self):
        """Check if test scripts exist"""
        self.print_section("PROJECT FILES CHECK")
        
        test_files = [
            "test_selenium_script.py",
            "test_selenium_advanced.py",
            "SELENIUM_TEST_README.md",
            "QUICK_START.md"
        ]
        
        for file in test_files:
            path = Path(file)
            if path.exists():
                self.log_success(f"Found: {file}")
            else:
                self.log_error(f"Missing: {file}")
    
    def print_summary(self):
        """Print final summary"""
        print("\n" + "=" * 80)
        print("📊 VERIFICATION SUMMARY".center(80))
        print("=" * 80 + "\n")
        
        print(f"✓ Successes: {len(self.successes)}")
        print(f"⚠️  Warnings: {len(self.warnings)}")
        print(f"✗ Errors: {len(self.issues)}")
        
        print("\n" + "─" * 80)
        print("NEXT STEPS:")
        print("─" * 80 + "\n")
        
        if self.critical_error:
            print("❌ CRITICAL ISSUES FOUND - Cannot proceed with testing")
            print("\nPlease fix these critical issues:")
            for i, issue in enumerate(self.issues, 1):
                print(f"  {i}. {issue}")
            print("\n" + "=" * 80)
            return False
        
        if self.warnings:
            print("⚠️  OPTIONAL FIXES RECOMMENDED:")
            for warning in self.warnings:
                print(f"  • {warning}")
            print()
        
        print("✅ READY TO RUN TESTS!")
        print("\n" + "─" * 80)
        print("TO START TESTING:")
        print("─" * 80 + "\n")
        print("1. Start Backend (Terminal 1):")
        print("   cd backend && npm run dev")
        print()
        print("2. Start Frontend (Terminal 2):")
        print("   cd frontend && npm run dev")
        print()
        print("3. Run Tests (Terminal 3):")
        print("   python test_selenium_advanced.py")
        print()
        print("   OR for basic tests:")
        print("   python test_selenium_script.py")
        print("\n" + "=" * 80 + "\n")
        return True
    
    def run_all_checks(self):
        """Run all environment checks"""
        self.print_header()
        
        try:
            self.check_python_version()
            self.check_node_npm()
            self.check_selenium_package()
            self.check_webdriver_manager()
            self.check_chromedriver()
            self.check_chrome_browser()
            self.check_project_files()
            self.check_backend_running()
            self.check_frontend_running()
        except Exception as e:
            print(f"\n❌ An error occurred during verification: {str(e)}")
            return False
        
        return self.print_summary()


def main():
    """Main entry point"""
    checker = EnvironmentChecker()
    success = checker.run_all_checks()
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
