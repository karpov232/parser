from urllib.request import urlopen

"""
Этот проект как и проект как и проект website делал для мессенджера и он позволяет взаимодействовать с вэб частью приложения
"""

ss = "" #вставляем ссылку на наш сайт

def new_db():
    url = f'{ss}/new_db'

    html = str(urlopen(url).read(), 'utf-8')

    return html

def pr_num(phone_number: int):
    url = f'{ss}/pr_pols/phone_number={phone_number}'

    html = str(urlopen(url).read(), 'utf-8')

    return html

def pr_nik(nik: str):
    url = f'{ss}/pr_nik/nik={nik}'

    html = str(urlopen(url).read(), 'utf-8')

    return html

def new_pols_db(phone_number: int):
    url = f'{ss}/create_db/phone_number={phone_number}'

    html = str(urlopen(url).read(), 'utf-8')

    return html

def create_pols(name: str, phone_number: int, nik: str):
    url = f"{ss}/create_pols/name={name}/phone_number={phone_number}/nik={nik}"

    html = str(urlopen(url).read(), 'utf-8')
    # html = {True, your_ss, f"Пользователь {name} ({phone_number}) добавлен успешно."}

    return html
  
