class Task_5_1:
    __doc__ = """    В задании создан словарь, с информацией о разных устройствах.
    Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1). И вывести информацию о соответствующем устройстве на стандартный поток вывода (информация будет в виде словаря).

    Пример выполнения скрипта:

    \t$ python task_5_1.py
    \tВведите имя устройства: r1
    \t{'location': '21 New Globe Walk', 'vendor': 'Cisco', 'model': '4451', 'ios': '15.4', 'ip': '10.255.0.1'}

    Ограничение: нельзя изменять словарь london_co.
    Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно решить без использования условия if."""
    london_co = {
        "r1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.1"
        },
        "r2": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.2"
        },
        "sw1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "3850",
            "ios": "3.6.XE",
            "ip": "10.255.0.101",
            "vlans": "10,20,30",
            "routing": True
        }
    }
    def __new__(self):
        user_input = input('Введите имя устройства').strip()
        print(Task_5_1.london_co.get(user_input))

class Task_5_1_a:
    __doc__="""Переделать скрипт из задания 5.1 таким образом, чтобы, кроме имени устройства, запрашивался также параметр устройства, который нужно отобразить.

    Вывести информацию о соответствующем параметре, указанного устройства.

    Пример выполнения скрипта:

    $ python task_5_1a.py
    Введите имя устройства: r1
    Введите имя параметра: ios
    15.4
    Ограничение: нельзя изменять словарь london_co.

    Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно решить без использования условия if."""
    london_co = {
        "r1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.1"
        },
        "r2": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.2"
        },
        "sw1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "3850",
            "ios": "3.6.XE",
            "ip": "10.255.0.101",
            "vlans": "10,20,30",
            "routing": True
        }
    }
    def __new__(self):
        device_name = input('Введите имя устройства').strip()
        parameter_name = input('Введите имя параметра').strip()
        print(Task_5_1.london_co[device_name][parameter_name])

class Task_5_1_b:
    __doc__="""Переделать скрипт из задания 5.1a таким образом, чтобы, при запросе параметра, отображался список возможных параметров. Список параметров надо получить из словаря, а не прописывать вручную.

    Вывести информацию о соответствующем параметре, указанного устройства.

    Пример выполнения скрипта:

    $ python task_5_1b.py
    Введите имя устройства: r1
    Введите имя параметра (location, vendor, model, ios, ip): ip
    10.255.0.1

    $ python task_5_1b.py
    Введите имя устройства: sw1
    Введите имя параметра (location, vendor, model, ios, ip, vlans, routing): ip
    10.255.0.101"""
    london_co = {
        "r1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.1"
        },
        "r2": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.2"
        },
        "sw1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "3850",
            "ios": "3.6.XE",
            "ip": "10.255.0.101",
            "vlans": "10,20,30",
            "routing": True
        }
    }
    def __new__(self):
        device_name = input('Введите имя устройства').strip()
        params = ", ".join(Task_5_1_b.london_co[device_name].keys())
        parameter_name = input(f'Введите имя параметра ({params})').strip()
        print(Task_5_1.london_co[device_name][parameter_name])

class Task_5_2:
    __doc__="""Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:

In [1]: "1" * 28 + "0" * 4
Out[1]: "11111111111111111111111111110000"
Ограничение: Все задания надо выполнять используя только пройденные темы."""
    london_co = {
        "r1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.1"
        },
        "r2": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.2"
        },
        "sw1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "3850",
            "ios": "3.6.XE",
            "ip": "10.255.0.101",
            "vlans": "10,20,30",
            "routing": True
        }
    }
    def __new__(self):
        ip_mask_input = input('Введите IP-сети в формате: 10.1.1.0/24').split("/")
        output = "Network:\n{0:<10} {1:<10} {2:<10} {3:<10} \n{0:<010b} {1:<010b} {2:<010b} {3:<010b}\n".format(int(ip_mask_input[0].split(".")[0]), int(ip_mask_input[0].split(".")[1]), int(ip_mask_input[0].split(".")[2]) , int(ip_mask_input[0].split(".")[3]))
        mask = int(ip_mask_input[1])
        bin_mask = int(ip_mask_input[1])* "1" + "0"*(32-int(ip_mask_input[1]))
        output += "Mask:\n/{0:<10}\n{1:<10} {2:<10} {3:<10} {4:<10}\n{1:<10b} {2:<10b} {3:<10b} {4:<10b}".format(mask, int(bin_mask[:8], 2), int(bin_mask[8:16], 2), int(bin_mask[16:24], 2), int(bin_mask[24:32], 2))
        print(output)

#task = Task_5_1()
#task = Task_5_1_a()
#task = Task_5_1_b()
#task = Task_5_2()