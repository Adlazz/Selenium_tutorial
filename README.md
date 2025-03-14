# 🚀 Automatización Web con Python y Selenium 2025

Bienvenido a este repositorio donde aprenderás a automatizar tareas web con **Selenium y Python** de manera eficiente, evitando bloqueos y simulando interacciones humanas.

## 📌 Características
✅ Instalación fácil y rápida
✅ Configuración avanzada para evitar detección de bots
✅ Simulación de comportamiento humano (clics, escritura, scroll)
✅ Código modular y escalable

---
## 🔧 Instalación
### 1️⃣ Clona el repositorio
```bash
git clone https://github.com/tu-usuario/selenium-automation.git
cd selenium-automation
```

### 2️⃣ Instala las dependencias
```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecuta el script principal
```bash
python main.py
```

---
## 📂 Estructura del Proyecto
```
📁 selenium_automation/
│── main.py                # Archivo principal
│── config_driver.py        # Configuración del navegador
│── selenium_actions.py     # Acciones personalizadas
│── requirements.txt        # Librerías necesarias
│── README.md               # Documentación
```

---
## 🚀 Uso y Ejemplo
### 🖥 Abrir Google y buscar en la barra de búsqueda
```python
from config_driver import open_page
from selenium_actions import wait_for_element, human_like_typing
from selenium.webdriver.common.by import By

# Abre Google
driver, wait = open_page("https://www.google.com")

# Encuentra el campo de búsqueda
search_box = wait_for_element(driver, By.NAME, "q")

# Escribe simulando una persona
human_like_typing(search_box, "Selenium Python")
search_box.send_keys("\n")
```

---
## 🔥 Evitando Detección de Bots
Para evitar bloqueos, hemos implementado:
✅ **User-Agent aleatorio** para evitar que los sitios detecten Selenium
✅ **Deshabilitar navigator.webdriver** para que el navegador parezca humano
✅ **Tiempo aleatorio entre acciones** (evita patrones repetitivos)

---
## 🛠 Tecnologías Utilizadas
- Python 3.x
- Selenium
- WebDriver Manager

---
## 🤝 Contribuciones
¡Toda ayuda es bienvenida! Si quieres contribuir, haz un **fork** y envía un **pull request**.

📩 **Contacto:** adrianlazzarini@gmail.com

⭐ **Si te fue útil este repositorio, dale una estrella!**

