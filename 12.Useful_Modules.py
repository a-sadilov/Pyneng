from operator import contains
from sys import argv
import subprocess
import datetime
import ipaddress
from tabulate import tabulate


class Task_12_1:
    __doc__ = '''
    Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса. Функция ожидает как аргумент список IP-адресов.
    Функция должна возвращать кортеж с двумя списками:
    \tсписок доступных IP-адресов
    \tсписок недоступных IP-адресов
    Для проверки доступности IP-адреса, используйте команду ping.'''


    def __new__(self, ip_adresses):
        reachable = []
        unreachable = []

        for ip in ip_adresses:
            result = subprocess.run(['ping',  ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if result.returncode == 0:
                reachable.append(ip)
            else:
                unreachable.append(ip)
        return reachable, unreachable


class Task_12_2:
    __doc__="""
    Функция ping_ip_addresses из задания 12.1 принимает только список адресов, но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.
    В этом задании необходимо создать функцию convert_ranges_to_ip_list, которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.
    Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.
    Элементы списка могут быть в формате:
    \t10.1.1.1
    \t10.1.1.1-10.1.1.10
    \t10.1.1.1-10
    Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона. Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.
    Функция возвращает список IP-адресов.
    Например, если передать функции convert_ranges_to_ip_list такой список:
    \t['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    Функция должна вернуть такой список:
    \t['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
    \t'172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']"""
    start_time = datetime.datetime.now()

    def __new__(self, ip_adresses):
        
        reachable = []
        unreachable = []
        all_ip_adresses = []
        for ip in ip_adresses:
            if ip.isalpha():
                raise ValueError("Not correct IPv4-Adress")
            if '-' in ip:
                start_ip, stop_ip = ip.split('-')
                if '.' not in stop_ip:
                    stop_ip = ".".join(start_ip.split(".")[:-1] + [stop_ip])
                start_ip = ipaddress.ip_address(start_ip)
                stop_ip = ipaddress.ip_address(stop_ip)
                for ip_address in range(int(start_ip), int(stop_ip) + 1):
                    all_ip_adresses.append(str(ipaddress.ip_address(ip_address)))
            else:
                all_ip_adresses.append(ip)
        for listed_ip in all_ip_adresses:
            result = subprocess.run(['ping',  listed_ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if result.returncode == 0:
                reachable.append(listed_ip)
            else:
                unreachable.append(listed_ip)
        print(__name__ + " Time: ", datetime.datetime.now() - Task_12_2.start_time)
        return reachable, unreachable
        

class Task_12_3:
    __doc__="""
    Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.
    Функция ожидает как аргументы два списка:
    \tсписок доступных IP-адресов
    \tсписок недоступных IP-адресов
    Результат работы функции - вывод на стандартный поток вывода таблицы вида:
    Reachable    Unreachable
    -----------  -------------
    10.1.1.1     10.1.1.7
    10.1.1.2     10.1.1.8
                10.1.1.9"""
    start_time = datetime.datetime.now()

    def __new__(self, reachable, unreachable):
        table = {"Reachable": reachable, "Unreachable": unreachable}
        print(tabulate(table, headers="keys"))

if __name__ == '__main__':
    """task = Task_12_1(['192.168.0.0', '192.168.0.1', '8.9.9.9'])
    print(task)
    task = Task_12_2(['192.168.0.0-3', '192.168.0.1-2', '8.8.8.2-8.8.8.8'])
    print(task)"""
    task = Task_12_2(['192.168.0.0-3', '192.168.0.1-2', '8.8.8.2-8.8.8.8'])
    task = Task_12_3(*task)
    