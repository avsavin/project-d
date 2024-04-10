import requests

if __name__ == '__main__':
    # Отправляем запрос на сервер с набором данных
    r = requests.post('http://localhost:8000/test', json=['TN'
              ,99800
              ,36
              ,37216
              ,1450
              ,'SingleFamily'
              ,78.61
              ,3
              ,'Sale'
              ,13
              ,1
              ,8590
              ,20000
              ])
    
    print('Статус сервера:', r.status_code)
    
    # Получаем предсказание
    if r.status_code == 200:
        print('Рассчитанное значение:', r.json()['estimation'])
    else:
        print('Server response:', r.text)