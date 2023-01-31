import re
import datetime
import pprint
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
from netmiko.exceptions import SSHException
import yaml


class Task_18_1_a:
    __doc__ = """
    Задание 18.1_a
    Создать функцию send_show_command.
    Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству
    и выполняет указанную команду.
    Параметры функции:
    * device - словарь с параметрами подключения к устройству
    * command - команда, которую надо выполнить
    Функция возвращает строку с выводом команды.
    Скрипт должен отправлять команду command на все устройства из файла devices.yaml
    с помощью функции send_show_command (эта часть кода написана).
    Скопировать функцию send_show_command из задания 18.1 и переделать ее таким образом, чтобы обрабатывалось исключение, которое генерируется при ошибке аутентификации на устройстве.
    При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.
    Для проверки измените пароль на устройстве или в файле devices.yaml.
    """
    start_time = datetime.datetime.now()
    
    @staticmethod
    def send_show_command(device, commands):
        result = {}
        try:
            with ConnectHandler(**device) as ssh:
                ssh.enable()
                for command in commands:
                    output = ssh.send_command(command)
                    result[command] = output
            print(__name__ + " Time: ", datetime.datetime.now() - Task_18_1_a.start_time)
            return result
        except NetmikoAuthenticationException as auth_err:
            print("Authettifiaction problem \n", auth_err)
        except SSHException as error:
            print(error)
        except (NetmikoTimeoutException) as error:
            print(error)


class Task_18_1_b:
    __doc__ = """
    Задание 18.1_a
    Создать функцию send_show_command.
    Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству
    и выполняет указанную команду.
    Параметры функции:
    * device - словарь с параметрами подключения к устройству
    * command - команда, которую надо выполнить
    Функция возвращает строку с выводом команды.
    Скрипт должен отправлять команду command на все устройства из файла devices.yaml
    с помощью функции send_show_command (эта часть кода написана).
    Скопировать функцию send_show_command из задания 18.1a и переделать ее таким образом, чтобы обрабатывалось не только исключение, которое генерируется при ошибке аутентификации на устройстве, но и исключение, которое генерируется, когда IP-адрес устройства недоступен.
    При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.
    Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
    """
    start_time = datetime.datetime.now()
    
    @staticmethod
    def send_show_command(device, commands):
        result = {}
        try:
            with ConnectHandler(**device) as ssh:
                ssh.enable()
                for command in commands:
                    output = ssh.send_command(command)
                    result[command] = output
            print(__name__ + " Time: ", datetime.datetime.now() - Task_18_1_a.start_time)
            return result
        except NetmikoAuthenticationException as auth_err:
            print("Authettifiaction problem \n", auth_err)
        except (NetmikoTimeoutException) as error:
            print(error)
    

class Task_18_2:
    __doc__ = """
    Задание 18.1_a
    Создать функцию send_show_command.
    Функция подключается по SSH (с помощью netmiko) к ОДНОМУ устройству
    и выполняет указанную команду.
    Параметры функции:
    * device - словарь с параметрами подключения к устройству
    * command - команда, которую надо выполнить
    Функция возвращает строку с выводом команды.
    Скрипт должен отправлять команду command на все устройства из файла devices.yaml
    с помощью функции send_show_command (эта часть кода написана).
    Скопировать функцию send_show_command из задания 18.1a и переделать ее таким образом, чтобы обрабатывалось не только исключение, которое генерируется при ошибке аутентификации на устройстве, но и исключение, которое генерируется, когда IP-адрес устройства недоступен.
    При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.
    Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
    """
    start_time = datetime.datetime.now()
    
    @staticmethod
    def send_show_command(device, commands):
        result = {}
        try:
            with ConnectHandler(**device) as ssh:
                ssh.enable()
                for command in commands:
                    output = ssh.send_command(command)
                    result[command] = output
            print(__name__ + " Time: ", datetime.datetime.now() - Task_18_2.start_time)
            return result
        except NetmikoAuthenticationException as auth_err:
            print("Authettifiaction problem \n", auth_err)
        except (NetmikoTimeoutException) as error:
            print(error)

if __name__ == '__main__':
    '''with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for device in devices:
        result = Task_18_1_a.send_show_command(device, ["sh clock", "sh ip int br"])
        pprint.pprint(result, width=120)'''