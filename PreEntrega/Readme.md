Propósito: automatizar flujos básicos de navegación Web.

Web utilizada: saucedemo.com
usuario : "standard_user"
password: "secret_sauce"
Cuando el login es exitoso es redirigido a la pag de inventario.

Tecnologías utilizadas:
	- Python como lenguaje principal
	- Pytest para la estructura del testing
	- Selenium WebDriver para la automatización
	- Git y GitHub para el control de las versiones

Estructura: 
		/PreEntrega
			/Test
				test_saucedemo.py
			/utils
			
			Readme.md

Criterios minimos se detectan en test_saucedemo.py bajo los nombres de "test_01 a 08..."

Comando de ejecución : py -m pytest -v tests/test_saucedemo.py

Comando de generación de Reporte: py -m pytest tests/test_saucedemo.py -v --html=Reporte.html