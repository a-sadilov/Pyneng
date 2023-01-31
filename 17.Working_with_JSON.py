import re
import datetime
import csv
import pprint
import json

class Task_17_1:
    __doc__="""
    Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод команды show dhcp snooping binding из разных файлов и записывает обработанные данные в csv файл.
    Аргументы функции:
     filenames - список с именами файлов с выводом show dhcp snooping binding
     output - имя файла в формате csv, в который будет записан результат
    Функция ничего не возвращает.
    Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
    MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
    ------------------  ---------------  ----------  -------------  ----  --------------------
    00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
    00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
    Total number of bindings: 2
    В итоговом csv файле должно быть такое содержимое:
     switch,mac,ip,vlan,interface
     sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
     sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21
    Первый столбец в csv файле имя коммутатора надо получить из имени файла, остальные - из содержимого в файлах.
    Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt."""
    start_time = datetime.datetime.now()
    
    regex = re.compile(r"(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<interface>\S+)")
                       

    def __new__(self, filenames, output ):
        with open(output, "w") as output_file:
            writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(["switch", "mac", "ip", "vlan", "interface"])
            for filename in filenames:
                switch_value = re.search("([^/]+)_dhcp_snooping.txt", filename).group(1)
                with open(filename, "r") as input_file:
                    for line in input_file:
                        match = Task_17_1.regex.search(line)
                        if match:
                            writer.writerow((switch_value,)+ match.groups())



class Task_17_2:
    __doc__="""
    Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает вывод команды show dhcp snooping binding из разных файлов и записывает обработанные данные в csv файл.
    Аргументы функции:
     filenames - список с именами файлов с выводом show dhcp snooping binding
     output - имя файла в формате csv, в который будет записан результат
    Функция ничего не возвращает.
    Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
    MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
    ------------------  ---------------  ----------  -------------  ----  --------------------
    00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
    00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
    Total number of bindings: 2
    В итоговом csv файле должно быть такое содержимое:
     switch,mac,ip,vlan,interface
     sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
     sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21
    Первый столбец в csv файле имя коммутатора надо получить из имени файла, остальные - из содержимого в файлах.
    Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt."""
    start_time = datetime.datetime.now()
    
                       

    def parse_sh_version(self, command_output):
        regex = (
            "Cisco IOS .*? Version (?P<ios>\S+), .*"
            "uptime is (?P<uptime>[\w, ]+)\n.*"
            'image file is "(?P<image>\S+)".*'
        )
        match = re.search(regex, command_output, re.DOTALL,)
        if match:
            return match.group("ios", "image", "uptime")
        

    def write_inventory_to_csv(self, data_filenames, csv_filename):
        headers = ["hostname", "ios", "image", "uptime"]
        with open(csv_filename, "w") as output_file:
            writer = csv.writer(output_file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(headers)
            for data_filename in data_filenames:
                hostname = re.search(r"sh_version_(?P<hostname>\S+).txt", data_filename).group(1)
                with open(data_filename, "r") as f:
                    parsed_data = self.parse_sh_version(f.read())
                    if parsed_data:
                        writer.writerow([hostname] + list(parsed_data))


class Task_17_3:
    __doc__="""
    Задание 17.3
    Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
    вывод команды show cdp neighbors.
    Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
    Функция должна возвращать словарь, который описывает соединения между устройствами.
    Например, если как аргумент был передан такой вывод:
    R4>show cdp neighbors
    Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
    R5           Fa 0/1          122           R S I           2811       Fa 0/1
    R6           Fa 0/2          143           R S I           2811       Fa 0/0
    Функция должна вернуть такой словарь:
    {'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
            'Fa 0/2': {'R6': 'Fa 0/0'}}}
    Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.
    Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt"""
    start_time = datetime.datetime.now()
    
                       

    def parse_sh_cdp_neighbors(self, sh_cdp_file):
        with open(sh_cdp_file, "r") as f:
            file_str = f.read()
            output_dict = {}
            regex = re.compile(
                r"(?P<device_id>\S+)[>#]"
            )
            r_device = regex.search(file_str).group(1)
            output_dict[r_device] = {}
            main_regex = re.compile(
                r"(?P<device_id>\S+) +(?P<loc_intf>\S+ \S+)+ +\d+ +(?:\w )+ +\S+ +(?P<port_id>\S+ \S+)"
            )
            for match in main_regex.finditer( file_str):
                device_id, loc_intf, port_id = match.group("device_id", "loc_intf", "port_id")
                output_dict[r_device][loc_intf] = {device_id: port_id}
            return output_dict
        

class Task_17_3_a:
    __doc__="""
    Задание 17.3
    Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
    вывод команды show cdp neighbors.
    Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
    Функция должна возвращать словарь, который описывает соединения между устройствами.
    Например, если как аргумент был передан такой вывод:
    R4>show cdp neighbors
    Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
    R5           Fa 0/1          122           R S I           2811       Fa 0/1
    R6           Fa 0/2          143           R S I           2811       Fa 0/0
    Функция должна вернуть такой словарь:
    {'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
            'Fa 0/2': {'R6': 'Fa 0/0'}}}
    Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.
    Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt"""
    start_time = datetime.datetime.now()
    
                    
    def parse_sh_cdp_neighbors(self, sh_cdp_files, save_to_filename = None):
        output_dict = {}
        for sh_cdp_file in sh_cdp_files:
            with open(sh_cdp_file, "r") as f:
                file_str = f.read()
                regex = re.compile(
                    r"(?P<device_id>\S+)[>#]"
                )
                r_device = regex.search(file_str).group(1)
                output_dict[r_device] = {}
                main_regex = re.compile(
                    r"(?P<device_id>\S+) +(?P<loc_intf>\S+ \S+)+ +\d+ +(?:\w )+ +\S+ +(?P<port_id>\S+ \S+)"
                )
                for match in main_regex.finditer(file_str):
                    device_id, loc_intf, port_id = match.group("device_id", "loc_intf", "port_id")
                    output_dict[r_device][loc_intf] = {device_id: port_id}
        if save_to_filename:
            with open(save_to_filename, "w") as save_to_file:
                json.dump(output_dict, save_to_file)
        print(__name__ + " Time: ", datetime.datetime.now() - Task_17_3_a.start_time)
        return output_dict

if __name__ == '__main__':
    '''task = Task_17_1(["sw1_dhcp_snooping.txt", "sw2_dhcp_snooping.txt", "sw3_dhcp_snooping.txt"], "write_dhcp_snooping_to_csv.txt")
    task = Task_17_2()
    task.write_inventory_to_csv(["sh_version_r1.txt", "sh_version_r2.txt", "sh_version_r3.txt"], "sh_version_to_csv.txt")
    task = Task_17_3()
    print(task.parse_sh_cdp_neighbors("sh_cdp_n_r2.txt"))'''
    task = Task_17_3_a()
    pprint.pprint(task.parse_sh_cdp_neighbors(["sh_cdp_n_r1.txt", "sh_cdp_n_r2.txt", "sh_cdp_n_r3.txt"], "sh_cdp_n_output.json"))