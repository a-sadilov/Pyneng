import datetime
import pprint
import time
import telnetlib
import yaml


class Task_22_1:
    __doc__ = """
    Задание 22_1
    Создать класс Topology, который представляет топологию сети.

    При создании экземпляра класса, как аргумент передается словарь, который описывает топологию. Словарь может содержать «дублирующиеся» соединения. Тут «дублирующиеся» соединения, это ситуация когда в словаре есть два соединения:

    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")
    Задача оставить только один из этих линков в итоговом словаре, не важно какой.

    В каждом экземпляре должна быть создана переменная topology, в которой содержится словарь топологии, но уже без «дублей». Переменная topology должна содержать словарь без «дублей» сразу после создания экземпляра.

    Пример создания экземпляра класса:

    In [2]: top = Topology(topology_example)
    """
    start_time = datetime.datetime.now()
    
    def __init__(self, connections_dict):
        self.topology = {}
        for local, remote in connections_dict.items():
            if not (self.topology.get(remote) == local):
                self.topology[local] = remote


class Task_22_1_a:
    __doc__ ='''Скопировать класс Topology из задания 22.1 и изменить его.
    Перенести функциональность удаления «дублей» в метод _normalize.
    При этом метод __init__ должен выглядеть таким образом:

    class Topology:
        def __init__(self, topology_dict):
            self.topology = self._normalize(topology_dict)
    '''
    def _normalize(self, topology_dict):
        self.unique_topologue_dict = {}
        for local, remote in topology_dict.items():
            if not(self.unique_topologue_dict.get(remote) == local):
                self.unique_topologue_dict[local] = remote
        return self.unique_topologue_dict

    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)


class Task_22_1_b:
    __doc__ ='''Изменить класс Topology из задания 22.1a или 22.1.
    Добавить метод delete_link, который удаляет указанное соединение.
    Метод должен удалять и «обратное» соединение, если оно есть (ниже пример).
    Если такого соединения нет, выводится сообщение «Такого соединения нет».
    '''
    def _normalize(self, topology):
        self.topology_dict = {}
        for local, remote in topology.items():
            if not(self.topology_dict.get(remote) == local):
                self.topology_dict[local] = remote
        return self.topology_dict
    
    def _delete_link(self, from_port, to_port):
        if self.topology_dict.get(from_port) == to_port:
            del self.topology[from_port]
        elif self.topology.get(to_port) == from_port:
            del self.topology[to_port]
        else:
            print("Такого соединения нет")


    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)


class Task_22_1_c:
    __doc__ ='''Изменить класс Topology из задания 22.1b.
    Добавить метод delete_node, который удаляет все соединения с указаным устройством.
    Если такого устройства нет, выводится сообщение «Такого устройства нет».
    '''
    def _normalize(self, topology):
        self.topology_dict = {}
        for local, remote in topology.items():
            if not(self.topology_dict.get(remote) == local):
                self.topology_dict[local] = remote
        return self.topology_dict
    
    def _delete_link(self, from_port, to_port):
        if self.topology_dict.get(from_port) == to_port:
            del self.topology[from_port]
        elif self.topology.get(to_port) == from_port:
            del self.topology[to_port]
        else:
            print("Такого соединения нет")
    

    def delete_node(self, node_name):
        original_size = len(self.topology)
        for src, dest in list(self.topology.items()):
            if node_name in src or node_name in dest:
                del self.topology[src]
        if original_size == len(self.topology):
            print("Такого устройства нет")


    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)


class Task_22_1_d:
    __doc__ ='''Изменить класс Topology из задания 22.1c
    Добавить метод add_link, который добавляет указанное соединение, если его еще нет в топологии.
    Если соединение существует, вывести сообщение «Такое соединение существует».
    Если одна из сторон есть в топологии, вывести сообщение «Cоединение с одним из портов существует».
    '''
    def _normalize(self, topology):
        self.topology_dict = {}
        for local, remote in topology.items():
            if not(self.topology_dict.get(remote) == local):
                self.topology_dict[local] = remote
        return self.topology_dict
    
    def delete_link(self, from_port, to_port):
        if self.topology_dict.get(from_port) == to_port:
            del self.topology[from_port]
        elif self.topology.get(to_port) == from_port:
            del self.topology[to_port]
        else:
            print("Такого соединения нет")
    

    def add_link(self, from_port, to_port):
        if (self.topology_dict.get(from_port) == to_port) or (self.topology.get(to_port) == from_port):
            print("Такое соединение существует")
        else:
            self.topology[from_port] = to_port

    def delete_node(self, node_name):
        original_size = len(self.topology)
        for src, dest in list(self.topology.items()):
            if node_name in src or node_name in dest:
                del self.topology[src]
        if original_size == len(self.topology):
            print("Такого устройства нет")


    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

class Task_22_2:
    __doc__ = """
        Создать класс CiscoTelnet, который подключается по Telnet к оборудованию Cisco.
    При создании экземпляра класса, должно создаваться подключение Telnet, а также
    переход в режим enable.
    Класс должен использовать модуль telnetlib для подключения по Telnet.
    У класса CiscoTelnet, кроме __init__, должно быть, как минимум, два метода:
    * _write_line - принимает как аргумент строку и отправляет на оборудование строку
    преобразованную в байты и добавляет перевод строки в конце. Метод _write_line должен
    использоваться внутри класса.
    * send_show_command - принимает как аргумент команду show и возвращает вывод
    полученный с обрудования
    Параметры метода __init__:
    * ip - IP-адрес
    * username - имя пользователя
    * password - пароль
    * secret - пароль enable
    """
    def __init__(self, ip, username, password, secret):
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b"Username:")
        self._write_line(username)
        self.telnet.read_until(b"Password:")
        self._write_line(password)
        self._write_line("enable")
        self.telnet.read_until(b"Password:")
        self._write_line(secret)
        self._write_line("terminal length 0")
        time.sleep(1)
        self.telnet.read_very_eager()

    def _write_line(self, line):
        self.telnet.write(line.encode("utf-8") + b"\n")

    def send_show_command(self, command):
        self._write_line(command)
        command_output = self.telnet.read_until(b"#").decode("utf-8")
        return command_output



if __name__ == "__main__":
    topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}
    '''top = Task_22_1(topology_example)
    pprint.pprint(top.topology)
    top = Task_22_1_a(topology_example)
    pprint.pprint(top.topology)
    top = Task_22_1_b(topology_example)
    pprint.pprint(top.topology)
    top._delete_link(('R3', 'Eth0/1'),('R4', 'Eth0/0'))
    pprint.pprint(top.topology)
    top = Task_22_1_c(topology_example)
    pprint.pprint(top.topology)
    top.delete_node('R3')
    pprint.pprint("After changing \n" + str(top.topology)
    top = Task_22_1_d(topology_example)
    pprint.pprint(top.topology)
    top.add_link(('SW5', 'Eth0/8'), ('R9', 'Eth0/5'))
    top.add_link(('SW5', 'Eth0/8'), ('R9', 'Eth0/5'))
    pprint.pprint(top.topology))'''

    r1 = telnetlib.CiscoTelnet(**{
        "ip": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    })
    print(r1.send_show_command("sh ip int br"))

