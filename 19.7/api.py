import json
import base64

import requests

from requests_toolbelt import MultipartEncoder

class PetFriends:
    """библиотека с API для Pet Friends"""
    def __init__(self):
        #записываю url сайта, куда будут направляться запросы
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self, email, password):
        """метод направляет запрос к API сервера и возвращает ответ в формале json,
        в котором указан ключ пользователя по логину и паролю"""
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        """метод направляет запрос к API сервера и возвращает ответ в формате json,
        в котором будет список всех животных. Если поставить фильтр "my_pets", то
        вернется список животных пользователя"""
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

#POST запрос на добавление нвого питомца без фото
    def post_new_pet_no_photo(self, auth_key, name, animal_type, age):
        """"метод отправляет данные о новом питомце на сервер и возвращает статус запроста в формате json,
        где описаны данные о новом питомце"""
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age
            })#заголовки для того чтобы сервер понял что ему обработать
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

#POST запрос на добавление нвого питомца с фото
    def post_new_pet_with_photo(self, auth_key, name, animal_type, age, pet_photo):
        """в данном методе усложнвется передача инф-ии. Теперь здесь есть доп. файл"""
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                #указываю имя файла, говорю что его надо открыть с параметром read в бинарной системе.
                #так программа понимает что это картинка, а не текст
                'pet_photo': ('salem.jpg', open('images/salem.jpg', 'rb'), 'image/jpeg')
            })

        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

#DELETE запрос на удаление питомца
    """"метод делает запрос на удаление пета по его ID и возвращает json, где написано,
    что пет удален"""
    def delete_pet(self, auth_key, pet_id):
        headers = {
            'auth_key': auth_key['key']
        }
        #посмотреть что значат заголовки
        #rest api testing pytest гуглить
        #смотреть как другие решают такие же задачи
        res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            #из-за того что в result приходит пустая строка, показывал ошибку, поэтому сразу
            #записала в txt файл.
            result = res.text
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

#PUT запрос на обновление информации о питомце
    def update_info_pet(self, auth_key, pet_id, name, animal_type, age):
        """"отправляю запрос с обновленной информацией - получаю json, где написано,
        что данные обновились"""
        headers = {
            'auth_key': auth_key['key']
        }
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

#POST запрос на добавление фотографии для пета
    def add_photo_to_pet(self, auth_key, pet_id, pet_photo):
        data = MultipartEncoder(
            fields={
                'pet_photo': ('salem.jpg', open('images/salem.jpg', 'rb'), 'image/jpeg')

        })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

#POST запрос на добавление нвого питомца с неправильным форматом фото
    def post_new_pet_with_bad_photo(self, auth_key, name, animal_type, age, pet_photo):
        """в данном методе усложнвется передача инф-ии. Теперь здесь есть доп. файл"""
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': ('text_S.txt', open('images/text_S.txt', 'rb'), 'text/plain')
            })

        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result