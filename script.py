from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

from selenium.webdriver.common.action_chains import ActionChains
# Ruta al controlador de ChromeDriver (asegúrate de haberlo descargado y configurado correctamente)
chrome_driver_path = r"C:\Users\Armando\Desktop\scripts\selenium\driver\chromedriver"

# Inicializar el servicio del controlador de ChromeDriver
service = Service(chrome_driver_path)

# Inicializar el navegador Chrome
driver = webdriver.Chrome(service=service)

url = "https://www.flashscore.pe/?rd=mismarcadores.com"

# Abrir la página en el navegador
driver.get(url)

# Esperar a que la página se cargue completamente (puedes ajustar el tiempo de espera según tus necesidades)
driver.implicitly_wait(10)

# Encontrar los elementos que contienen los datos de los partidos del día
elementos_partidos = driver.find_elements(By.CSS_SELECTOR, "div.event__match.event__match--twoLine")

# Iterar sobre los elementos y extraer los datos que deseas
for n,elemento in enumerate(elementos_partidos):
    # Extraer los datos de cada partido según su estructura HTML
    # y realizar el procesamiento que necesites
    print(n)
    # Ejemplo de extracción de datos de los equipos
    equipo_local = elemento.find_elements(By.CSS_SELECTOR, "div.event__participant.event__participant--home")[0]
    # equipo_visitante = elemento.find_elements(By.CSS_SELECTOR, "div.event__participant.event__participant--away").text
 
    
    # Ejemplo de extracción de datos del marcador
    # marcador_local = elemento.find_element(By.CSS_SELECTOR, "div.event__score.event__score--home").text
    # marcador_visitante = elemento.find_element(By.CSS_SELECTOR, "div.event__score.event__score--away").text
    
    # Ejemplo de extracción de datos de la hora del partido
    #hora_partido = elemento.find_element(By.CSS_SELECTOR, "div.event__time").text
    
    # Realizar el procesamiento adicional y almacenamiento de los datos extraídos
    
    
    # print('Equipo local {}\
    #       Equipo visitante{} {}-{}'.format(equipo_local,equipo_visitante,marcador_local,marcador_visitante))
    print('Equipo local {} '.format(equipo_local.text ))
    
    #Hacemos click en el evento
    actions = ActionChains(driver)
    actions.move_to_element(elemento).click().perform()
    
    # elemento.click()
    
    
    # wait = WebDriverWait(driver, 5)
    driver.implicitly_wait(10)
    # wait.until(EC.new_window_is_opened(driver.window_handles))
    # wait.until(EC.number_of_windows_to_be(2))
    
    
    #cambiamos el control a la ventana emergente
 
    driver.switch_to.window(driver.window_handles[-1])
    driver.implicitly_wait(5)

    #Extraemos datos de las páginas hijas 

    enlace_alineaciones = driver.find_element(By.CSS_SELECTOR,'a[href*="alineaciones"]')
    enlace_estadisticas = driver.find_element(By.CSS_SELECTOR,'a[href*="estadisticas-del-partido"]')
    enlace_cuotas       = driver.find_element(By.CSS_SELECTOR,'a[href*="comparacion-cuotas"]')

    enlace_alineaciones.click()

    #driver.close()
    time.sleep(5)
    
    driver.switch_to.window(driver.window_handles[0])
    
    
    
# Cerrar el navegador



time.sleep(20)
driver.quit()