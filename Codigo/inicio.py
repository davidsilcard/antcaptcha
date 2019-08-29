from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from imagetyperzapi3.imagetyperzapi import ImageTyperzAPI


def resolveCaptcha(img):
    access_token = '9057BFA6CAAB4EACB6540F53C5948CE1'
    ita = ImageTyperzAPI(access_token)
    balance = ita.account_balance()
    print('Balance: {}'.format(balance))
    return ita.solve_captcha(img, case_sensitive=False)

def main():
    driver = webdriver.Chrome(executable_path=r"D:\Projetos\PycharmProjects\virtualenv\chromedriver_win32\chromedriver.exe")
    driver.get('https://www.receita.fazenda.gov.br/PessoaJuridica/CNPJ/cnpjreva/cnpjreva_solicitacao2.asp')
    wait = WebDriverWait(driver, 5)

    btnCaptcha = wait.until(EC.presence_of_element_located((By.ID, 'captchaSonoro')))
    btnCaptcha.click()

    with open('captcha.png', 'wb') as file:
        file.write(wait.until(EC.presence_of_element_located((By.ID, 'imgCaptcha'))).screenshot_as_png)
    textCaptcha = resolveCaptcha('captcha.png')

    insereCnpj = wait.until(EC.presence_of_element_located((By.ID, 'cnpj')))
    driver.execute_script("arguments[0].value = '{0}';".format('47508411000156'), insereCnpj)

    insereCaptcha = wait.until(EC.presence_of_element_located((By.ID, 'txtTexto_captcha_serpro_gov_br')))
    driver.execute_script("arguments[0].value = '{0}';".format(textCaptcha), insereCaptcha)

    btnConsultar = wait.until(EC.presence_of_element_located((By.ID, 'submit1')))
    btnConsultar.click()

    driver.close()


if __name__ == '__main__':
    main()