from imagetyperzapi3.imagetyperzapi import ImageTyperzAPI
import time

access_token = '9057BFA6CAAB4EACB6540F53C5948CE1'
# get access token from: http://www.imagetyperz.com/Forms/ClientHome.aspx
ita = ImageTyperzAPI(access_token)  # init imagetyperz api obj

balance = ita.account_balance()  # get account balance
print('Balance: {}'.format(balance))

recaptcha_params = {
    'page_url': 'https://www.receita.fazenda.gov.br/PessoaJuridica/CNPJ/cnpjreva/cnpjreva_solicitacao2.asp',
    'sitekey': '6LcT2zQUAAAAABRp8qIQR2R0Y2LWYTafR0A8WFbr',
    'type': 2,  # optional, 1 - normal recaptcha, 2 - invisible recaptcha, 3 - v3 recaptcha, default: 1
    'v3_min_score': .3,  # optional
    'v3_action': 'homepage',  # optional
    'proxy': '126.45.34.53:345',  # or 126.45.34.53:123:joe:password
    'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'  # optional
}
captcha_id = ita.submit_recaptcha(recaptcha_params)
# print balance

# check if it's still in progress (waiting to be solved), every 10 seconds
while ita.in_progress():  # while it's still in progress
    time.sleep(10)  # sleep for 10 seconds and recheck

recaptcha_response = ita.retrieve_recaptcha(
    captcha_id)  # captcha_id is optional, if not given, will use last captcha id submited
print('Recaptcha response: {}'.format(recaptcha_response))  # print google response
