from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)  #modo oculto. Se quiser ver a automação acontecendo só passar headless=false
    pagina = navegador.new_page()
    pagina.goto("https://pato.academy/") #Abrir a página
    #Preencher Formulário
    pagina.locator('xpath=/html/body/main/a').click()  #clicar em algo
    pagina.fill('xpath=//*[@id="E-mail"]', 'DIGITAR E-MAIL') #Preencher algo
    pagina.fill('xpath=//*[@id="Senha"]', 'DIGITAR A SENHA')
    pagina.locator('xpath=//*[@id="root"]/div/section/div[2]/form/button').click()
    time.sleep(20) #Tempo que o navegador fica aberto

    
    

    