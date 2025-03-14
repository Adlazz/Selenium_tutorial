import random
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

def get_random_user_agent():
    """Devuelve un User-Agent aleatorio para evitar detección automatizada."""
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15'
    ]
    return random.choice(user_agents)

def create_driver():
    """Configura y devuelve una instancia del navegador con opciones personalizadas."""
    options = webdriver.ChromeOptions()
    user_agent = get_random_user_agent()
    
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return driver

def open_page(url):
    """Abre una página en un navegador configurado con Selenium."""
    driver = create_driver()
    time.sleep(random.uniform(1, 3))  # Simula comportamiento humano
    
    driver.get(url)
    wait = WebDriverWait(driver, 50)

    return driver, wait  # Devuelve el driver y el objeto WebDriverWait
