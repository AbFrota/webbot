from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.portaldoholanda.com.br/bizarro/jovem-morre-engasgada-com-pedaco-de-carne-apos-entrevista-de-empreg'

# Open the Website
x = 1
while True:
    browser.get(url)
    browser.execute_script("window.open('url');")
    browser.execute_script("window.open('url');")
    browser.execute_script("window.open('url');")
    browser.execute_script("window.open('url');")
    browser.execute_script("window.open('url');")

    x +=1
