
from operator import index


class Task_6_1:
    __doc__="""Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX. Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.
    Написать код, который преобразует MAC-адреса в формат cisco и добавляет их в новый список result.
    Полученный список result вывести на стандартный поток вывода (stdout) с помощью print."""
    macs = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
    def __new__(self):
        for mac in Task_6_1.macs:
            i = Task_6_1.macs.index(mac)
            Task_6_1.macs[i] = mac.replace(":", ".") 
        print(Task_6_1.macs)


class Task_6_2:
    __doc__="""
Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
    «unicast» - если первый байт в диапазоне 1-223
    «multicast» - если первый байт в диапазоне 224-239
    «local broadcast» - если IP-адрес равен 255.255.255.255
    «unassigned» - если IP-адрес равен 0.0.0.0
    «unused» - во всех остальных случаях"""
    def __new__(self):
        ip_address = input('Введите IP-адрес в формате 10.0.1.1: ')
        if int(ip_address.split('.')[0]) >= 1 and int(ip_address.split('.')[0]) <= 223:
            print("unicast")
        elif int(ip_address.split('.')[0]) >= 224 and int(ip_address.split('.')[0]) <= 239:
            print("multicast")
        elif ip_address == "255.255.255.255":
            print("local broadcast")
        elif ip_address == "0.0.0.0":
            print("unassigned")
        else: print("unused")


class Task_6_2_a:
    __doc__="""
Сделать копию скрипта задания 6.2.
Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:

    состоит из 4 чисел (а не букв или других символов)
    числа разделенны точкой
    каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: «Неправильный IP-адрес».
Сообщение «Неправильный IP-адрес» должно выводиться только один раз, даже если несколько пунктов выше не выполнены."""
    def __new__(self):
        ip = input("Введите IP-адрес в формате x.x.x.x: ")
        octets = ip.split(".")
        valid_ip = len(octets) == 4

        for i in octets:
            valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip

        if valid_ip:
            if 1 <= int(octets[0]) <= 223:
                print("unicast")
            elif 224 <= int(octets[0]) <= 239:
                print("multicast")
            elif ip == "255.255.255.255":
                print("local broadcast")
            elif ip == "0.0.0.0":
                print("unassigned")
            else:
                print("unused")
        else:
            print("Неправильный IP-адрес")


class Task_6_2_b:
    __doc__="""
Сделать копию скрипта задания 6.2a.
Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова."""
    ip_correct = False
    def __new__(self):
        while not Task_6_2_b.ip_correct:
            ip = input("Введите IP-адрес в формате x.x.x.x: ")
            octets = ip.split(".")
            valid_ip = len(octets) == 4

            for i in octets:
                valid_ip = i.isdigit() and 0 <= int(i) <= 255 and valid_ip

            if valid_ip:
                if 1 <= int(octets[0]) <= 223:
                    print("unicast")
                elif 224 <= int(octets[0]) <= 239:
                    print("multicast")
                elif ip == "255.255.255.255":
                    print("local broadcast")
                elif ip == "0.0.0.0":
                    print("unassigned")
                else:
                    print("unused")
                Task_6_2_b.ip_correct = True
            else:
                print("Неправильный IP-адрес")

if __name__ == "__main__":
    #task = Task_6_1()
    #task = Task_6_2()
    #task = Task_6_2_a()
    task = Task_6_2_b()