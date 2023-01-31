import time
import telnetlib
import yaml
import pprint


class Task_23_1:
    __doc__ = """
        Задание 23.1
    В этом задании необходимо создать класс IPAddress.
    При создании экземпляра класса, как аргумент передается IP-адрес и маска,
    а также должна выполняться проверка корректности адреса и маски:
    * Адрес считается корректно заданным, если он:
    - состоит из 4 чисел разделенных точкой
    - каждое число в диапазоне от 0 до 255
    * маска считается корректной, если это число в диапазоне от 8 до 32 включительно
    Если маска или адрес не прошли проверку, необходимо сгенерировать
    исключение ValueError с соответствующим текстом (вывод ниже).
    Также, при создании класса, должны быть созданы два атрибута экземпляра:
    ip и mask, в которых содержатся адрес и маска, соответственно.
    Пример создания экземпляра класса:
    In [1]: ip = IPAddress('10.1.1.1/24')
    Атрибуты ip и mask
    In [2]: ip1 = IPAddress('10.1.1.1/24')
    In [3]: ip1.ip
    Out[3]: '10.1.1.1'
    In [4]: ip1.mask
    Out[4]: 24
    Проверка корректности адреса (traceback сокращен)
    In [5]: ip1 = IPAddress('10.1.1/24')
    ---------------------------------------------------------------------------
    ...
    ValueError: Incorrect IPv4 address
    Проверка корректности маски (traceback сокращен)
    In [6]: ip1 = IPAddress('10.1.1.1/240')
    ---------------------------------------------------------------------------
    ...
    ValueError: Incorrect mask
    """
    def __init__(self, ip_addres):
        ip, mask = ip_addres.split("/")
        self._check_ip(ip)
        self._check_mask(mask)
        self.ip, self.mask = ip, int(mask)

    def _check_ip(self, ip):
        octets = ip.split(".")
        correct_octets = [octet for octet in octets if octet.isdigit() and 0 <= int(octet) <= 255]
        if len(octets) == 4 and len(correct_octets) == 4:
            return True
        else:
            raise ValueError("Incorrect IPv4 address")

    def _check_mask(self, mask):
        if mask.isdigit() and 8 <= int(mask) <=32:
            return True
        else:
            raise ValueError("Incorrect Mask-value")


class Task_23_2:
    __doc__ = """
                Задание 23.2
        Скопировать класс CiscoTelnet из любого задания 22.2x и добавить классу поддержку
        работы в менеджере контекста.
        При выходе из блока менеджера контекста должно закрываться соединение.
        Пример работы:
        In [14]: r1_params = {
            ...:     'ip': '192.168.100.1',
            ...:     'username': 'cisco',
            ...:     'password': 'cisco',
            ...:     'secret': 'cisco'}
        In [15]: from task_23_2 import CiscoTelnet
        In [16]: with CiscoTelnet(**r1_params) as r1:
            ...:     print(r1.send_show_command('sh clock'))
            ...:
        sh clock
        *19:17:20.244 UTC Sat Apr 6 2019
        R1#
        In [17]: with CiscoTelnet(**r1_params) as r1:
            ...:     print(r1.send_show_command('sh clock'))
            ...:     raise ValueError('Возникла ошибка')
            ...:
        sh clock
        *19:17:38.828 UTC Sat Apr 6 2019
        R1#
        ---------------------------------------------------------------------------
        ValueError                                Traceback (most recent call last)
        <ipython-input-17-f3141be7c129> in <module>
            1 with CiscoTelnet(**r1_params) as r1:
            2     print(r1.send_show_command('sh clock'))
        ----> 3     raise ValueError('Возникла ошибка')
            4
        ValueError: Возникла ошибка"""

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
        self.telnet.write(line.encode("ascii") + b"\n")

    def send_show_command(self, command):
        self._write_line(command)
        time.sleep(1)
        command_output = self.telnet.read_very_eager().decode("ascii")
        return command_output

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.telnet.close()


class Task_23_3:
    __doc__ = """
        Задание 23.3
    Скопировать и изменить класс Topology из задания 22.1x.
    Добавить метод, который позволит выполнять сложение двух экземпляров класса Topology.
    В результате сложения должен возвращаться новый экземпляр класса Topology.
    Создание двух топологий:
    In [1]: t1 = Topology(topology_example)
    In [2]: t1.topology
    Out[2]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
    ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}
    In [3]: topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                                ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}
    In [4]: t2 = Topology(topology_example2)
    In [5]: t2.topology
    Out[5]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}
    Суммирование топологий:
    In [6]: t3 = t1+t2
    In [7]: t3.topology
    Out[7]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
    ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
    ('R1', 'Eth0/6'): ('R9', 'Eth0/0'),
    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
    ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}
    Проверка, что исходные топологии не изменились:
    In [9]: t1.topology
    Out[9]:
    {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
    ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}
    In [10]: t2.topology
    Out[10]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}
    """
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

    def __add__(self, other):
        return Task_23_3({**self.topology, **other.topology})
        
if __name__ == "__main__":
    """p1 = Task_23_1('10.1.1.1/24')
    print(p1.ip, p1.mask)
    r1_params = {
        "ip": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    with Task_23_2(**r1_params) as r1:
        print(r1.send_show_command("sh clock"))"""
    topology_example = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    }
    topology_example2 = {
        ("R1", "Eth0/4"): ("R7", "Eth0/0"),
        ("R1", "Eth0/6"): ("R9", "Eth0/0"),
    }
    t1 = Task_23_3(topology_example)
    t2 = Task_23_3(topology_example2)
    t3 = t2 + t1
    pprint.pprint(t1.topology)