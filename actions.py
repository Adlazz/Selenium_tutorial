import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, by, value, timeout=10):
    """Espera hasta que un elemento esté presente en la página."""
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

def human_like_typing(element, text):
    """Simula escritura humana en un campo de texto."""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))  # Simula tiempo entre teclas

def human_like_click(driver, element):
    """Mueve el cursor al elemento y lo hace clic después de un pequeño retraso."""
    actions = ActionChains(driver)
    actions.move_to_element(element).pause(random.uniform(1, 2)).click().perform()

def scroll_page(driver, direction="down", amount=500):
    """Simula un desplazamiento suave en la página."""
    scroll_script = f"window.scrollBy(0, {amount});" if direction == "down" else f"window.scrollBy(0, -{amount});"
    driver.execute_script(scroll_script)
    time.sleep(random.uniform(1, 2))  # Simula tiempo de reacción
