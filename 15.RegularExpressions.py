import datetime
import re
import pprint

class Task_15_1:
    __doc__="""
    Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла, в котором находится конфигурация устройства.

    Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски, которые настроены на интерфейсах, в виде списка кортежей:

    первый элемент кортежа - IP-адрес

    второй элемент кортежа - маска

    Например (взяты произвольные адреса):

    [("10.0.1.1", "255.255.255.0"), ("10.0.2.1", "255.255.255.0")]
    Для получения такого результата, используйте регулярные выражения.

    Проверить работу функции на примере файла config_r1.txt."""
    start_time = datetime.datetime.now()
    regex = r"ip address (\S+) (\S+)"
    

    def __new__(self, file_name):
        result = []
        with open(file_name, 'r+') as f:
            result = [m.groups() for m in re.finditer(Task_15_1.regex, f.read())]
        return result


class Task_15_1_a:
    __doc__="""
    Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
    \tключ: имя интерфейса
    \tзначение: кортеж с двумя строками:
    \t\tIP-адрес
    \t\tмаска
    В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.
    Например (взяты произвольные адреса):
    {"FastEthernet0/1": ("10.0.1.1", "255.255.255.0"),
    "FastEthernet0/2": ("10.0.2.1", "255.255.255.0")}
    Для получения такого результата, используйте регулярные выражения.
    Проверить работу функции на примере файла config_r1.txt."""
    start_time = datetime.datetime.now()
    
    regex = re.compile(
        r"interface (?P<interface>\S+)\n"
        r"( .*\n)*"
        r" ip address (?P<ip_addres>\S+) (?P<mask>\S+)")

    def __new__(self, file_name):
        with open(file_name, 'r+') as f:
            result = {m.group('interface') : m.group('ip_addres','mask') for m in Task_15_1_a.regex.finditer(f.read())}
        print(__name__ + " Time: ", datetime.datetime.now() - Task_15_1_a.start_time)
        return result


class Task_15_1_b:
    __doc__="""
    Проверить работу функции get_ip_from_cfg из задания 15.1a на конфигурации config_r2.txt.
    Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
    \tinterface Ethernet0/1
    \tip address 10.255.2.2 255.255.255.0
    \tip address 10.254.2.2 255.255.255.0 secondary
    А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1 соответствует только один из них (второй).
    Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким образом, чтобы она возвращала список кортежей для каждого интерфейса. Если на интерфейсе назначен только один адрес, в списке будет один кортеж. Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.
    Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу Ethernet0/1 соответствует список из двух кортежей.
    Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя."""
    start_time = datetime.datetime.now()
    
    regex = re.compile(
        r"interface (?P<interface>\S+)\n"
        r"(?: .*\n)*"
        r"( ip address (?P<ip>\S+) (?P<msk>\S+))+")

    def __new__(self, file_name):
        result = {}
        with open(file_name) as f:
        # сначала отбираем нужные куски конфигурации
            match = re.finditer(
                "interface (\S+)\n"
                "(?: .*\n)*"
                " ip address \S+ \S+\n"
                "( ip address \S+ \S+ secondary\n)*",
                f.read(),
            )
        # потом в этих частях находим все IP-адреса
        for m in match:
            result[m.group(1)] = re.findall("ip address (\S+) (\S+)", m.group())
        print(__name__ + " Time: ", datetime.datetime.now() - Task_15_1_b.start_time)
        return result


class Task_15_2:
    __doc__="""
    Проверить работу функции get_ip_from_cfg из задания 15.1a на конфигурации config_r2.txt.
    Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
    \tinterface Ethernet0/1
    \tip address 10.255.2.2 255.255.255.0
    \tip address 10.254.2.2 255.255.255.0 secondary
    А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1 соответствует только один из них (второй).
    Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким образом, чтобы она возвращала список кортежей для каждого интерфейса. Если на интерфейсе назначен только один адрес, в списке будет один кортеж. Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.
    Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу Ethernet0/1 соответствует список из двух кортежей.
    Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса, диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя."""
    start_time = datetime.datetime.now()
    
    regex = re.compile(r'(\S+)\s+ +(\S+) +\s+ +\S+ +\S+ +(\S+ \S*) +(\S+)')

    def __new__(self, file_name):
        with open(file_name) as f:
            result = Task_15_2.regex.findall(f.read())
        print(__name__ + " Time: ", datetime.datetime.now() - Task_15_2.start_time)
        return result


class Task_15_3:
    __doc__="""
    Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.
    Функция ожидает такие аргументы:
    \t * имя файла, в котором находится правила NAT Cisco IOS
    \t * имя файла, в который надо записать полученные правила NAT для ASA
    Функция ничего не возвращает.
    Проверить функцию на файле cisco_nat_config.txt.
    Пример правил NAT cisco IOS
    \t ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
    \t ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023
    И соответствующие правила NAT для ASA:
    \t object network LOCAL_10.1.2.84
    \t host 10.1.2.84
    \t nat (inside,outside) static interface service tcp 22 20022
    \t object network LOCAL_10.1.9.5
    \t host 10.1.9.5
    \t nat (inside,outside) static interface service tcp 22 20023
    В файле с правилами для ASA:
    \t - не должно быть пустых строк между правилами
    \t - перед строками «object network» не должны быть пробелы
    \t - перед остальными строками должен быть один пробел
    Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside)."""
    start_time = datetime.datetime.now()
    
    regex = re.compile(r'ip nat inside source static (?P<con_type>\S+) +(?P<ip>\S+) +(?P<conn_number>\S+) +.* +(?P<port>\d+)')
    output = 'object network LOCAL_{ip}\n host {ip}\n nat (inside,outside) static interface service {con_type} {conn_number} {port}\n'
    def __new__(self, rules_file_name, output_file_name):
        with open(rules_file_name) as f, open(output_file_name, 'w') as output_config :
            matches = Task_15_3.regex.finditer(f.read())
            for m in matches:
                output_config.write(Task_15_3.output.format(**m.groupdict()))
        print(__name__ + " Time: ", datetime.datetime.now() - Task_15_3.start_time)
        

class Task_15_4:
    __doc__="""
    Создать функцию get_ints_without_description, которая ожидает как аргумент имя файла, в котором находится конфигурация устройства.
    Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов, на которых нет описания (команды description).
    Пример интерфейса с описанием:
    interface Ethernet0/2
     description To P_r9 Ethernet0/2
     ip address 10.0.19.1 255.255.255.0
     mpls traffic-eng tunnels
     ip rsvp bandwidth
    Интерфейс без описания:
    interface Loopback0
     ip address 10.1.1.1 255.255.255.255
    Проверить работу функции на примере файла config_r1.txt."""
    start_time = datetime.datetime.now()
    
    regex = re.compile(r"!\ninterface (?P<intf>\S+)\n"
                       r"(?P<descr> description \S+)?")

    def __new__(self, config):
        result = []
        with open(config) as src:
            match = Task_15_4.regex.finditer(src.read())
            result = [m.group('intf') for m in match if m.lastgroup == 'intf']
        print(__name__ + " Time: ", datetime.datetime.now() - Task_15_4.start_time)
        return result

if __name__ == '__main__':
    '''task = Task_15_1("config_r1.txt")
    print(task)
    task = Task_15_1_a("config_r1.txt")
    pprint.pprint(task)
    task = Task_15_1_b("config_r2.txt")
    pprint.pprint(task)
    task = Task_15_2("sh_ip_int_br.txt")
    pprint.pprint(task)
    print(Task_15_3.__doc__)
    task = Task_15_3("cisco_nat_config.txt", "cisco_asa_config.txt")'''
    task = Task_15_4("config_r1.txt")
    pprint.pprint(task)
    