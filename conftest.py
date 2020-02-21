import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", 
                     help="Choose your browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en", 
                     help="Choose your language (en, fr, ru, ...)")
    
    
@pytest.fixture()
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    print(f"\nStart {browser_name} browser...")
    
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=firefox_profile)
    else:
        raise pytest.UsageError('--browser_name should be "chrome" or "firefox"')
        
    yield browser
    print(f"\nQuit {browser_name} browser...")
    browser.quit()
    
        
        
    
    































