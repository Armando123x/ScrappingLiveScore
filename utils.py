from selenium.webdriver.common.by import By
from keys import *
import numpy 

def extract_children(driver):

    enlace_resumen      = driver.find_element(By.CSS_SELECTOR,TAG_RESUMEN_PARTIDO)
    enlace_alineaciones = driver.find_element(By.CSS_SELECTOR,TAG_ALINEACIONES)
    enlace_estadisticas = driver.find_element(By.CSS_SELECTOR,TAG_ESTADISTICAS)
    enlace_cuotas       = driver.find_element(By.CSS_SELECTOR,TAG_CUOTAS)


    ##################################
    # I will ensure be on resumen

    enlace_resumen.click()

    elements_home = driver.find_element(By.CSS_SELECTOR,TAG_EVENT_RESUME_HOME)

    elements_away = driver.find_element(By.CSS_SELECTOR,TAG_EVENT_RESUME_AWAY)

    total = len(elements_home)+ len(elements_away)   



    struct = {'type_event':None,'minute_event':None,'player':None}
    
    
    if total>0:
        count=0
        buffer = numpy.empty(total,dtype='object')
        buffer.fill(struct)
        for element in elements_home:
            
            
        
    
    