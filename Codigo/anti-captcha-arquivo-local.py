# api_key = 'f89f8380c361f21a88986b608ea7334b'
# "D:\Projetos\PycharmProjects\virtualenv\SituacaoCadastral\Codigo\captcha_ms.jpeg"

# https://anti-captcha.com/mainpage

from python3_anticaptcha import ImageToTextTask

ANTICAPTCHA_KEY = ""
image_link = "gerarCaptcha.png"
user_answer = ImageToTextTask.ImageToTextTask(anticaptcha_key = ANTICAPTCHA_KEY).\
                captcha_handler(captcha_file=image_link)

print(user_answer)

