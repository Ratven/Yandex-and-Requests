import unittest
import requests
import file_1


class TestOfAPI(unittest.TestCase):

    def setUp(self):
        API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        params = {
            'key': API_KEY,
            'text': 'привет',
            'lang': 'ru-en',
        }
        response = requests.get(URL, params=params)
        self.json_ = response.json()

    def test_of_translating(self):
        self.assertIn(self.json_['code'], range(200, 400), )
        self.assertEqual(self.json_['text'], ['hi'])

    def test_negative_case(self):
        """
        в случае неверного ключа возвращает код 400 или больше
        """
        API_KEY_FALSE = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe3327f7ce9a9f0'
        URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        params = {
            'key': API_KEY_FALSE,
            'text': 'привет',
            'lang': 'ru-en',
        }
        response = requests.get(URL, params=params)
        self.json_ = response.json()
        # print(self.json_)
        self.assertGreaterEqual(self.json_['code'], 400)


if __name__ == '__main__':
    unittest.main()
