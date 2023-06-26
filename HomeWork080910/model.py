phone_book = []
path = 'phones.txt'


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        user_id, name, phone, comment, *_ = contact.strip().split(':')
        phone_book.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})


def check_id():
    uid_list = []
    for contact in phone_book:
        uid_list.append(int(contact.get('id')))
    return {'id': max(uid_list) + 1}


def add_contact(new: dict):
    new.update(check_id())
    phone_book.append(new)


def search(word: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in value.lower():
                result.append(contact)
                break
    return result


def change(index: int, new: dict[str, str]):
    for key, field in new.items():
        if field != '':
            phone_book[index - 1][key] = field

def delete_contact(index: int): # Функция удаления контакта
    if index >= 1 and index <= len(phone_book): # Проверка index, диапазон (больше или равен 1) и (меньше или равен колву контактов)
        phone_book.pop(index - 1) # Удалить контакт с index из списка пхоне_бук
        for i, contact in enumerate(phone_book): #Запуск цикла оставшихся контактов (ай - индекс, контакт, очевидно, контакт)
            contact['id'] = i + 1 # обновляет индексы контактов в списке пхоне_бук (ставится ай+1)


