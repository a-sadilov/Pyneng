from datetime import datetime


class Task_9_1:
    __doc__="""
    Cоздать функцию, которая генерирует конфигурацию для access-портов.
    Функция ожидает такие аргументы:

    \t*словарь с соответствием интерфейс-VLAN такого вида:

    {"FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17}

    \t*шаблон конфигурации access-портов в виде списка команд (список access_mode_template)
    
    Функция должна возвращать список всех портов в режиме access с конфигурацией на основе шаблона access_mode_template. В конце строк в списке не должно быть символа перевода строки.
    В этом задании заготовка для функции уже сделана и надо только продолжить писать само тело функции."""
    start_time = datetime.now()

    access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable"]

    access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

    access_config_2 = {
        "FastEthernet0/03": 100,
        "FastEthernet0/07": 101,
        "FastEthernet0/09": 107,
    }
    def __new__(self, interface_vlan = access_config_2, access_mode_template = access_mode_template):
        access_config = []
        for intf, vlan in interface_vlan.items():
            access_config.append(f"interface {intf}")
            for cmd in access_mode_template:
                if cmd.endswith("access vlan"):
                    access_config.append(f"{cmd} {vlan}")
                else:
                    access_config.append(f"{cmd}")
        print("Task_7_2_a Time: ", datetime.now() - Task_9_1.start_time)
        return access_config


class Task_9_1_a:
    __doc__="""
    Сделать копию скрипта задания 7.2.
    Дополнить скрипт: Скрипт не должен выводить команды, в которых содержатся слова, которые указаны в списке ignore.
    При этом скрипт также не должен выводить строки, которые начинаются на !.
    Проверить работу скрипта на конфигурационном файле config_sw1.txt. Имя файла передается как аргумент скрипту."""
    start_time = datetime.now()

    access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
    ]

    port_security_template = [
        "switchport port-security maximum 2",
        "switchport port-security violation restrict",
        "switchport port-security"
    ]

    access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

    def __new__(self,*, interface_vlan = access_config, access_mode_template = access_mode_template, psecurity = None):
        access_config = []
        for intf, vlan in interface_vlan.items():
            access_config.append(f"interface {intf}")
            for command in access_mode_template:
                if command.endswith("access vlan"):
                    access_config.append(f"{command} {vlan}")
                else:
                    access_config.append(command)
            if psecurity:
                access_config.extend(psecurity)
        print("Task_7_2_a Time: ", datetime.now() - Task_9_1.start_time)
        return access_config


class Task_9_2:
    __doc__="""
    Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов.

    У функции должны быть такие параметры:

    intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы такого вида:

    {"FastEthernet0/1": [10, 20],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]}
    trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде списка команд (список trunk_mode_template)

    Функция должна возвращать список команд с конфигурацией на основе указанных портов и шаблона trunk_mode_template. В конце строк в списке не должно быть символа перевода строки.

    Проверить работу функции на примере словаря trunk_config и списка команд trunk_mode_template. Если эта проверка прошла успешно, проверить работу функции еще раз на словаре trunk_config_2 и убедится, что в итоговом списке правильные номера интерфейсов и вланов.

    Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):

    [
    "interface FastEthernet0/1",
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan 10,20,30",
    "interface FastEthernet0/2",
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan 11,30",
    ...]"""
    start_time = datetime.now()

    trunk_mode_template = [
        "switchport mode trunk", "switchport trunk native vlan 999",
        "switchport trunk allowed vlan"
    ]

    trunk_config = {
        "FastEthernet0/1": [10, 20, 30],
        "FastEthernet0/2": [11, 30],
        "FastEthernet0/4": [17]
    }

    def __new__(self, *, interface_vlan = trunk_config, access_mode_template = trunk_mode_template):
        access_config = {(intf): [(cmd +" "+ str(vlan).strip("[]")) if cmd.endswith("allowed vlan") else cmd for cmd in Task_9_2_a.trunk_mode_template] for intf, vlan in Task_9_2_a.trunk_config.items()}
        print("Task_7_2_a Time: ", datetime.now() - Task_9_1.start_time)
        
        return access_config


class Task_9_2_a:
    __doc__="""
    Сделать копию функции generate_trunk_config из задания 9.2

    Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:

    ключи: имена интерфейсов, вида «FastEthernet0/1»

    значения: список команд, который надо выполнить на этом интерфейсе

    Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template."""
    start_time = datetime.now()

    trunk_mode_template = [
        "switchport mode trunk", "switchport trunk native vlan 999",
        "switchport trunk allowed vlan"
    ]

    trunk_config = {
        "FastEthernet0/1": [10, 20, 30],
        "FastEthernet0/2": [11, 30],
        "FastEthernet0/4": [17]
    }

    def __new__(self):
        access_config = {(intf): [(cmd +" "+ str(vlan).strip("[]")) if cmd.endswith("allowed vlan") else cmd for cmd in Task_9_2_a.trunk_mode_template] for intf, vlan in Task_9_2_a.trunk_config.items()}
        return access_config

if __name__ == "__main__":
    '''task = Task_9_1()
    for line in task:
        print(line)
    task = Task_9_2()
    for line in task:
        print(line)
    task = Task_9_2_a()
    print(task.keys())
    for line in Task_9_2_a.trunk_config.keys():
        print(task[line])'''
    task = Task_9_1_a()
    for line in task:
        print(line)

    
    