import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains

from Locators.Locators import testLocators

class TC_13():

    def __init__(self, driver):
        self.driver = driver
        self.name_username = testLocators.name_username
        self.name_password = testLocators.name_password
        self.xpath_languajeMenu = testLocators.xpath_languajeMenu
        self.xpath_languajeEnglish = testLocators.xpath_languajeEnglish
        self.xpath_languajeSpanish = testLocators.xpath_languajeSpanish        
        self.xpath_loginButtonEnglish = testLocators.xpath_loginButtonEnglish
        self.xpath_loginButtonSpanish = testLocators.xpath_loginButtonSpanish
        self.xpath_textInicio = testLocators.xpath_textInicio
        self.xpath_filterTree = testLocators.xpath_filterTree
        self.xpath_typeOfSearch = testLocators.xpath_typeOfSearch
        self.xpath_typeOfSearchButton = testLocators.xpath_typeOfSearchButton
        self.xpath_Warehouse_400 = testLocators.xpath_Warehouse_400
        self.xpath_collapseButton  = testLocators.xpath_collapseButton 
        self.xpath_oversellingAmountTextbox = testLocators.xpath_oversellingAmountTextbox

    def start(self):
        # Browser.
        self.driver.get("https://backoffice.cuh2n5y6vm-mabesadec1-s1-public.model-t.cc.commerce.ondemand.com/backoffice/login.zul")
        self.driver.maximize_window() # For maximizing window
        self.driver.implicitly_wait(10)

        # Usuario.
        self.driver.find_element("name", self.name_username).send_keys("sapTestingCloud")

        # Password.
        self.driver.find_element("name", self.name_password).send_keys("mabe2022")

        # Idioma.
        str_Languaje = "English"
        if (str_Languaje == "Español"):
            # Click en Boton Login.
            self.driver.find_element(By.XPATH, self.xpath_loginButtonSpanish).click()
        elif (str_Languaje == "English"):
            self.driver.find_element(By.XPATH, self.xpath_languajeMenu).click()
            self.driver.implicitly_wait(3) 
            self.driver.find_element(By.XPATH, self.xpath_languajeEnglish).click() 
            self.driver.implicitly_wait(3)
            # Click en Boton Login.
            self.driver.find_element(By.XPATH, self.xpath_loginButtonEnglish).click()

        # Validación de Texto Inicio - Home.
        try:
            textInicio = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, self.xpath_textInicio))
            )
        except:
            raise Exception("Nunca se Ingreso a la Aplicacion.")
        
        # Click en Buscar.
        self.driver.find_element(By.XPATH, self.xpath_filterTree).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.xpath_filterTree).send_keys("Stock Level")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'"+"Stock Level"+"')] ").click()
        time.sleep(1)
        
        # Click en Tipo de Busqueda.
        self.driver.find_element(By.XPATH, self.xpath_typeOfSearch).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.xpath_typeOfSearch).send_keys("RMB520IBMRX0")
        self.driver.find_element(By.XPATH, self.xpath_typeOfSearchButton).click()
        time.sleep(10)

        # Validación del Número 004. 
        try:
            number_Warehouse = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.xpath_Warehouse_400))
            )
            print("400 Founded.")
            number_Warehouse.click()
        except:
            raise Exception("Nunca se Encontro el Warehouse 400.")
        time.sleep(1)

        # Click el Menu Collapse.
        self.driver.find_element(By.XPATH, self.xpath_collapseButton).click()      
        time.sleep(1) 

        # Obtenemos el Valor del Overselling Amount Textbox.
        int_oversellingAmount = self.driver.find_element(By.XPATH, self.xpath_oversellingAmountTextbox).get_attribute('value')
        print("Overselling Amount: ", int_oversellingAmount)