import requests
#from pprint import pprint

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
YA_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
YA_PATH = 'thenewfilebyalexander3.txt'

def translate_it(file_from, file_to, lang_from,  lang_to='ru'):
    text = ''
    with open(file_from) as source_file:
        for line in source_file:
            text += f'{line}\n'

    params = {
        'key': API_KEY,
        'text': text,
        'lang': f'{lang_from}-{lang_to}',
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    with open(file_to, "w", encoding='windows-1251') as target_file:
        target_file.write(''.join(json_['text']))
    print('Translating success')

def put_it_to_yandex(anyfile):
    text = ''
    params = {'path': YA_PATH,}

    response_get = requests.get(YA_URL,
                                params=params,
                                headers={'Authorization': 'OAuth AgAAAAAUIEb0AADLWzkiAN-IF0gBvP5xG8eVRKo'}
                                )
    if response_get.status_code >= 400:
        print(response_get.status_code)
        raise RuntimeError("Ошибка")
    json_ = response_get.json()
    #pprint(f'GET-JSON:\n{json_}')
    with open(anyfile, encoding='iso-8859-1') as f:
        for line in f:
            text += f'{line}\n'
    response_put = requests.put(json_['href'], data=text,)
    print('STATUS CODE: ', response_put.status_code)
    #pprint(f'PUT-JSON:\n{response_put.json()}')

if __name__ == '__main__':
    translate_it('DE.txt', 'RU.txt', 'de')
    put_it_to_yandex('RU.txt')