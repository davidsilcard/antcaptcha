# api_key = 'f89f8380c361f21a88986b608ea7334b'
# "D:\Projetos\PycharmProjects\virtualenv\SituacaoCadastral\Codigo\captcha_ms.jpeg"

# https://anti-captcha.com/mainpage

from python3_anticaptcha import ImageToTextTask
# Введите ключ от сервиса AntiCaptcha, из своего аккаунта. Anticaptcha service key.
ANTICAPTCHA_KEY = ""
# Ссылка на изображения для расшифровки. Link to captcha image.
image_link = "gerarCaptcha.png"
# Возвращается строка-расшифровка капчи. Get string for solve captcha, and some other info.
user_answer = ImageToTextTask.ImageToTextTask(anticaptcha_key = ANTICAPTCHA_KEY).\
                captcha_handler(captcha_file=image_link)

print(user_answer)

