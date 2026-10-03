import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#comunicación con el navegador para todos los test
@pytest.fixture(scope="module")
def driver():
    service = Service (ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
        
    yield driver
    
    driver.quit()
    
    
    #login: usr&password + btn
def test_01_login(driver):
      driver.get("https://www.saucedemo.com/")
      
      driver.find_element(By.ID,"user-name").send_keys("standard_user")
      driver.find_element(By.ID,"password").send_keys("secret_sauce")
      driver.find_element(By.ID,"login-button").click()
      
      assert "/inventory.html" in driver.current_url,"ERROR: No se redirigió a/inventory.html"
      
      
   #validación titulo pag/ventana correcta   
def test_02_verificar_inventario(driver):
    page_title=driver.title
    section_title=driver.find_element(By.CLASS_NAME,"title").text
    
          
    assert page_title=="Swag Labs", f'ERROR:Titulo de ventana esperada "Swag Labs", Obtenido{page_title}'
     
    assert section_title=="Products", f'ERROR:Titulo de la sección esperada "Swag Labs", Obtenido{section_title}'
    
    
    
   #Validación : existencia de al menos un producto 
    #[]len() para ver que tan largo es una lista 
  
    
def test_03_productos_visibles(driver):
   
    inventory_item=driver.find_elements(By.CLASS_NAME,'inventory_item')
    
    assert len(inventory_item)>0, f'ERROR:no se encontraron productos visibles'
    
    
def test_04_validar_interfaz(driver):
    menu_button=driver.find_element(By.ID,'react-burger-menu-btn')
    filtro=driver.find_element(By.CLASS_NAME,'product_sort_container')
    
    
    assert menu_button.is_displayed(),f'ERROR:menú no está visible'
    assert filtro.is_displayed(), f'ERROR:filtro no está visible'
    
    
def test_05_añadir_producto_al_carrito(driver):
    first_item=driver.find_elements(By.CLASS_NAME,'inventory_item')[0]
    
    boton_agregar=first_item.find_element(By.TAG_NAME,'button')
    boton_agregar.click()
    boton_remove=first_item.find_element(By.TAG_NAME,"button")
    
    #assert boton_agregar.text=='Remove', 'ERROR:el botón no cambió a "Remove"'
    assert boton_remove.text=='Remove', 'ERROR:el botón no cambió a "Remove"'
    
    
def test_06_verificar_contador_carrito(driver):
    contador_carrito=driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text
    
    assert contador_carrito=="1",f'ERROR:se esperaba 1, obtuvo {contador_carrito}'
    
    
def test_07_navegar_carrito(driver):
   
    driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    assert "/cart.html" in driver.current_url, "ERROR:no se redirigió a /cart.html"
    
def test_08_comprobar_producto_en_el_carrrito(driver):
    producto_nombre_en_carrito=driver.find_element(By.CLASS_NAME,'inventory_item_name').text
 
    assert producto_nombre_en_carrito=='Sauce Labs Backpack', f'ERROR: no es el mismo nombre'
    
    
    
  
    
    

    
    
    