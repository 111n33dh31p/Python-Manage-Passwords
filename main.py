import index
import time
import os

print("Вас приветствует программа Python-Manage-Passwords")
time.sleep(1)
print("Для полноценной работы была реализована кривая система хранения ")
time.sleep(1)
print("паролей и также всех необходимых данных для входа на желающую для вас платформу ")
time.sleep(1)
print("==============================================================================")
data = ""
while data !="1" or data !="2" or data !="3":
    data = input("Создать новую учётную запись или использовать существующую?"
                 "\n1. Создать новую"
                 "\n2. Использовать текущую \n")

    if data == '1':
        print("Сейчас невозможно создать новую учётную запись, возможно проблемы на сервере, или же программист - придурок")

    if data == '2':
        print("Пожалуйста, введите пароль для входа в систему менеджера")
        login_admin_try = input("Ваш логин: ")
        password_admin_try = input("Ваш пароль: ")
        if login_admin_try == (index.login_admin):
            if password_admin_try == (index.password_admin):
                print("Здравствуйте, " + login_admin_try)
                menu = ""
                while menu != '1' or menu != '2':
                     menu = input("Вы хотите создать новую таблицу или же посмотреть текущие?"
                        "\n1. Создать новый пароль"
                        "\n2. Просмотреть текущие пароли"
                        "\n3. Удалить текущий список паролей"
                        "\n4. Выход \n")

                     if menu == '1':
                         software = input("Введите название платформы: ")
                         username = input("Введите ник от этой платформы: ")
                         password = input("Введите пароль от этой платформы: ")
                         file = open("password.txt", "a")
                         file.write(software + "; " + username + "; " + password + ";" + "\n")
                         time.sleep(1.5)
                         print("Всё успешно!")
                         print("_______________________________________________")
                         file.close()

                     if menu == '2':
                         time.sleep(1)
                         print("Показываю существующие пароли.")
                         time.sleep(1)
                         print("Показываю существующие пароли..")
                         time.sleep(1)
                         print("Показываю существующие пароли...")
                         time.sleep(1)
                         print("Готово!")
                         file = open("password.txt", "r")
                         print("_______________________________________________")
                         print("Software\tUsername\tPassword")
                         print("_______________________________________________")
                         for i in file:
                            data = i.split(";")
                            print(data[0] + "\t\t", data[1] + "\t\t", data[2] + "\t\t")

                     if menu == '3':
                         print("Удаление паролей.")
                         time.sleep(1)
                         print("Удаление паролей..")
                         time.sleep(1)
                         print("Удаление паролей...")
                         time.sleep(1)
                         agree = input("Точно вы хотите отчистить пароли (y/n) \n")
                         if agree == "y":
                             file = open("password.txt", "w")
                             file.write("")
                             file.close()
                             print("_______________________________________________")
                             print("Пароли удалены!")
                             break

                         if agree == "n":
                             break

                     if menu == '4':
                        exit()
                if password_admin_try != (index.password_admin) or login_admin_try != (index.login_admin):
                    print("Данные не совпадают. Пожалуйста попробуйте ещё раз :)))))")

