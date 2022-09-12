from src.models import Addressbook


def insert_adressbook(name, phone, birthday, emails, address):
    ab = Addressbook(name=name, phone=phone, birthday=birthday, emails=emails, address=address)
    ab.save()
    print(f'Successful add user')


def change_contact(name, old, new):
    r = Addressbook.objects
    for i in r:
        if i.name == name and i.phone == old:
            i.update(phone=new)
    print('Successful change phone number')


def show_phone(name):
    r = Addressbook.objects
    for i in r:
        if i.name == name:
            print(f"{name}'s phone: {i.phone}")


def del_phone(name):
    r = Addressbook.objects
    for i in r:
        if i.name == name:
            i.update(phone='')
    print(f'Successful delete phone')


def show_all():
    r = Addressbook.objects
    if not r:
        print('AddressBook is empty')
    for i in r:
        if i.birthday is not None:
            print(f"User: {i.name}, phone: {i.phone}, birthday: {i.birthday.date()}, email: {i.emails}, address: {i.address}")
        elif i.birthday is None:
            print(f"User: {i.name}, phone: {i.phone}, birthday: {i.birthday}, email: {i.emails}, address: {i.address}")


def add_birthday(name, birthday):
    r = Addressbook.objects
    for i in r:
        if i.name == name and i.birthday is not None:
            print(f'User already has birthday: {i.birthday}')
        if i.name == name and i.birthday is None:
            i.update(birthday=birthday)
    print(f'Successful add birthday to user {name}')


def days_to_user_birthday(name):
    r = Addressbook.objects
    for i in r:
        if i.name == name and i.birthday is not None:
            return i.birthday.date()
        elif i.name == name and i.birthday is None:
            return i.birthday


def find_something(som):
    r = Addressbook.objects
    j_som = ' '.join(som)
    for i in r:
        if j_som in i.name or j_som in i.phone or j_som in i.emails or j_som in i.address:
            print(f"User: {i.name}, phone: {i.phone}, birthday: {i.birthday.date()}, email: {i.emails}, address: {i.address}")


def del_user(name):
    r = Addressbook.objects
    for i in r:
        if i.name == name:
            i.delete()
    print(f'Successful delete user: {name}')


def clear_all():
    r = Addressbook.objects
    for i in r:
        i.delete()
    print('Successful delete all users')


def add_email(name, email):
    r = Addressbook.objects
    for i in r:
        if i.name == name and i.emails != '':
            print('Email already exists')
        if i.name == name and i.emails == '':
            i.update(emails=email)
            print(f'Successful add email to user {name}')


def del_email(name):
    r = Addressbook.objects
    for i in r:
        if i.name == name and i.emails != '':
            i.update(emails='')
            print(f'Successful delete email from user {name}')
        if i.name == name and i.emails == '':
            print('Email does not exist')


def add_address(name, address):
    r = Addressbook.objects
    for i in r:
        if i.name == name and i.address != '':
            print('Email already exists')
        if i.name == name and i.address == '':
            i.update(address=address)
            print(f'Successful add address to user {name}')


if __name__ == "__main__":
    pass
