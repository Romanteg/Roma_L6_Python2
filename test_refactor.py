from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=20)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    if current_time.hour >= 22 or current_time.hour < 6:
        is_dark_theme = True  
    else:
        is_dark_theme = False
    assert is_dark_theme is True
        

def test_dark_theme_by_time_and_user_choice():
    current_time = time(hour=15)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную
    if dark_theme_enabled_by_user == True: # Включил ночной режим 
        is_dark_theme = dark_theme_enabled_by_user
        assert is_dark_theme is True
        print('Выбор пользователя')
    elif dark_theme_enabled_by_user is None: # Не включил, но проверяется интервал с 23-6 ночь 
        if current_time.hour >= 22 or current_time.hour < 6: 
            is_dark_theme = True 
            print(is_dark_theme, "Включена темная тема")
        else:
            is_dark_theme = False 
            print(is_dark_theme, "Выключена темная тема")
    else:
        is_dark_theme = False  # Темная тема выключена  
        print(False, "Значение из else")
    assert is_dark_theme is True 

def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = None
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = None
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]




def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")
def print_function_name_and_args(func, *args):  # функция принимает имя функции и значения аргументов
    func_name = func.__name__.replace('_', ' ').title() # получаем имя функции и преобразуем его в читаемый вид (заменяем символ подчеркивания на пробел, делаем первую букву заглавной)
    args_name = ", ".join([*args])  # преобразуем значения аргументов в строку
    print(f"{func_name} [{args_name}]")  # печатаем имя функции и значения аргументов
    return f"{func_name} [{args_name}]"  # возвращаем строку с именем функции и значениями аргументов
def open_browser(browser_name):
    print_function_name_and_args(open_browser, browser_name)
def go_to_companyname_homepage(page_url):
    print_function_name_and_args(go_to_companyname_homepage, page_url)

def find_registration_button_on_login_page(page_url, button_text):
    print_function_name_and_args(find_registration_button_on_login_page, page_url, button_text)


def open_browser(browser_name):
    actual_result = print_function_name_and_args(open_browser, browser_name)
    print_function_name_and_args(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = print_function_name_and_args(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = print_function_name_and_args(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"