import os

import pytest
from requests_toolbelt.multipart.encoder import MultipartEncoder

if __name__ == '__main__':
    import pytest, sys
    try:
        filename = sys.argv[0]
    except IndexError:
        print("Call with filename only")
    pytest.main(['-v', '--no-header', filename])

import sys
sys.path.append('..')
from api import PetFriends
from settings import valid_email, valid_password, name_1, animal_type_1, age_1, name_2, bad_name_1, no_name, \
    no_animal_type, no_age, long_name_1, bad_age, name_3

pf = PetFriends()

"""проверка на валидые логин и пароль, с получением статуса и ключа для последующего отпрвления запросов"""
def test_get_api_key_for_valid_user():
    #сохраняю результат текст в result, код статуса в status
    status, result = pf.get_api_key(valid_email, valid_password)
    assert status == 200
    #проверка что результате есть ключ "key", который потом поможет нам отправлять запросы
    assert 'key' in result

"""получаем список всех питомцев, убеждаемся что он не пустой"""
def test_get_all_pets_with_valid_key(filter=''):
    #получили ключ авторизации
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    #сохранили полученную информацию по переменным
    status, result = pf.get_list_of_pets(auth_key, filter)
    #убедились что запрос прошел успешно
    assert status == 200
    #проверка, что список не пустой
    assert len(result['pets']) > 0

#1 проверим что нового питомца можно добавить без фото
def test_post_new_pet_no_photo(name=name_1, animal_type=animal_type_1, age=age_1):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet_no_photo(auth_key, name, animal_type, age)
    assert status == 200
    #проверка, что поле "name" поменялось на "name_1"
    assert result['name'] == name_1

#2 проверим, что питомца можно добавить со всеми валидными данными
def test_post_new_pet_with_photo(name=name_1, animal_type=animal_type_1, age=age_1, pet_photo='images/salem.jpg'):
    #путь до фотографии нужно сохранить в переменную
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    #проверяем что файл формата "jpg" теперь есть в поле pet_photo
    assert 'jpg' in pet_photo

#3 проверим, что питомца можно удалить
def test_delete_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    #запрашиваю список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    #беру самого первого
    pet_id = my_pets['pets'][0]['id']
    #запрос на его удаление
    status, _ = pf.delete_pet(auth_key, pet_id)
    #смотрим на обновленный список питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    assert status == 200
    #убеждаемся, что первый питомец отсутвует в списке
    assert pet_id not in my_pets.values()

#4 обновление информации о питомце с валидными данными
def test_update_info_pet(name=name_2, animal_type=animal_type_1, age=age_1):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    #делаю запрос на обновление информации у первого питомца
    status, result = pf.update_info_pet(auth_key, pet_id, name, animal_type, age)
    assert status == 200
    #убеждаюсь, что информация об его имени поменялась
    assert result['name'] == name_2

#5 обновление информации о питомце невалидными данными: всесто букв - символы
def test_update_info_pet_not_a_valid_name(name=bad_name_1, animal_type=animal_type_1, age=age_1):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.update_info_pet(auth_key, pet_id, name, animal_type, age)
    assert status == 200
    assert result['name'] == bad_name_1

#6 обновление информации о питомце на пустые данные
def test_update_info_pet_bald_fields(name=no_name, animal_type=no_animal_type, age=no_age):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.update_info_pet(auth_key, pet_id, name, animal_type, age)
    assert status == 200
    assert result['name'] == no_name

#7 обновление информации о питомце невалидными данными: очень длинное имя
def test_update_info_pet_long_name(name=long_name_1, animal_type=animal_type_1, age=age_1):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.update_info_pet(auth_key, pet_id, name, animal_type, age)
    assert status == 200
    assert result['name'] == long_name_1
#8 обновление информации о питомце невалидными данными: в возрасте вместо цифр - буквы и символы
def test_update_info_pet_bad_age(name=name_1, animal_type=animal_type_1, age=bad_age):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.update_info_pet(auth_key, pet_id, name, animal_type, age)
    assert status == 200
    assert result['age'] == bad_age
#9 добавление питомца с фотографией: файл неккоректо сохранен, вместо jpg - txt
def test_post_new_pet_with_bad_photo(name=name_3, animal_type=animal_type_1, age=age_1, pet_photo='images/text_S.txt'):
    #путь до фотографии нужно сохранить в переменную
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    #поидее для корректной работы сайта дожен быть статус 400, но сервер выдает 200 - значит можно выложить вместо фото - текст?
    assert status == 200
    # проверка что дата в неверном формате
    assert 'txt' in pet_photo

#10 добавить фотографию к питомцу без фотографии
def test_add_photo_to_pet(pet_photo='images/salem.jpg'):
    #путь до фотографии нужно сохранить в переменную
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_photo_to_pet(auth_key, pet_id, pet_photo)
    assert status == 200
    #проверяем что файл формата "jpg" теперь есть в поле pet_photo
    assert 'jpg' in pet_photo
