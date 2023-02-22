import time
from datetime import date, timedelta
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#Pegando a semana anterior
week_after = date.today() - timedelta(days=7)
dt_today = date.today().strftime("%d/%m/%Y")
dt_week = week_after.strftime("%d/%m/%Y")

#Instanciando o webdriver do Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())

#Conectando com o site
driver.get('https://dejt.jt.jus.br/dejt/f/n/diariocon')
time.sleep(3)

#Clicando na primeira data e preenchendo a mesma
driver.find_element(By.XPATH, "//*[@id='corpo:formulario:dataIni']").click()
driver.find_element(By.XPATH, "//*[@id='corpo:formulario:dataIni']").send_keys(dt_week)
time.sleep(1)

#Clicando na segunda data e preenchendo a mesma
driver.find_element(By.XPATH, "//*[@id='corpo:formulario:dataFim']").click()
driver.find_element(By.XPATH, "//*[@id='corpo:formulario:dataFim']").send_keys(dt_today)
time.sleep(2)

#Encontrando a tabela da página
driver.find_element(By.XPATH, "//*[@id='corpo:formulario:botaoAcaoPesquisar']/table/tbody/tr/td[2]/div").click()
time.sleep(3)

#Clicando no botao de paginamento
driver.find_element(By.XPATH, "//*[@id='diarioNav']/table/tbody/tr/td[1]/button[1]").click()
time.sleep(2)

#Lógica de enquanto existir o botao na posiçao 3 (de paginaçao) ele manter o click
while driver.find_element(By.XPATH, "//*[@id='diarioNav']/table/tbody/tr/td[1]/button[3]"):
    table_xpath = driver.find_element(By.XPATH, "//*[@id='diarioCon']/fieldset/table")

    #Percorrendo cada tr da tabela
    rows = table_xpath.find_elements(By.TAG_NAME, "tr")

    #Baixando o primeiro pdf (teste, só consegui até aqui) e aguarda 5s para o dowload
    pdf_download = driver.find_element(By.XPATH, "//*[@id='diarioCon']/fieldset/table/tbody/tr[2]/td[3]/button").click()
    time.sleep(5)
    for row in rows:
        #Percorrendo cada td da posiçao 2 da tabela para extrair a data
        if row.text.split( )[2] != "Disponibilização":
            print(row.text.split( )[0] + " " + row.text.split( )[2])

    #Clicando no botao de posiçao 3 para paginar
    driver.find_element(By.XPATH, "//*[@id='diarioNav']/table/tbody/tr/td[1]/button[3]").click()
    time.sleep(2)

driver.close()

#Criar tabelas com as datas
#Criar executavel
#Criar relatorio