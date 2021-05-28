# Web scraping com selenium                  |
# Necessário: ter o chromedriver instalado   | \
# Necessário: instalar o selenium                 by: lucas-Dk || Whatsapp +5531986802198
# pip install -r requirements.txt            | /
# Façam bom uso!                             |

try:
	import os
	from time import sleep as esperar
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.chrome.options import Options
except:
	print("Comando: pip install -r requirements.txt")
	print("Instale o chromedriver para rodar esse script!")
else:
	segundo_plano = Options()
	segundo_plano.add_argument("--headless")

	driver = webdriver.Chrome(options=segundo_plano)
	driver.get("https://www.mercadolivre.com.br/")
	esperar(2)

	os.system("clear")
	busca = str(input("[+] O que você deseja buscar no site: "))
	cookies = driver.find_element_by_xpath('//button[@class="nav-cookie-disclaimer__button"]')
	cookies.send_keys(Keys.RETURN)

	barra_pesquisa = driver.find_element_by_xpath('//input[@class="nav-search-input"]')
	barra_pesquisa.send_keys(busca)
	barra_pesquisa.send_keys(Keys.RETURN)
	esperar(2)

	titulo_pesquisa = driver.find_elements_by_xpath('//h2[@class="ui-search-item__title"]')
	precos_produtos = driver.find_elements_by_xpath('//span[@class="price-tag-fraction"]')

	os.system("clear")
	print("[+] RESULTADO DOS NOMES DOS PRODUTOS:\n")
	cont = 0
	for item in titulo_pesquisa:
		if item != None:
			print("{}: R$:{}".format(titulo_pesquisa[cont].text,precos_produtos[cont].text))
			cont += 1
#FIM
