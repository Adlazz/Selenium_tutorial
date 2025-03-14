from config_driver import open_page
from actions import wait_for_element, human_like_typing, human_like_click, scroll_page
from selenium.webdriver.common.by import By
import time
import random

driver, wait = open_page("http://google.com")

# Esperar el campo de búsqueda
search_box = wait_for_element(driver, By.NAME, "q")

# Mover el cursor antes de hacer clic

human_like_click(driver, search_box)

# Escribir en el campo de búsqueda de forma natural
human_like_typing(search_box, "Selenium Python")

# Simular presionar ENTER
search_box.send_keys("\n")

# Esperar resultados
wait_for_element(driver, By.ID, "search")

# Desplazar la página un poco
scroll_page(driver, "down", 300)

# Cerrar navegador después de unos segundos
time.sleep(5)
driver.quit()




driver.quit()
