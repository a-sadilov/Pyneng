from datetime import datetime
import time

start_time = datetime.now()

#print(datetime.now() - start_time)


class Exersize4_1:
    __doc__ = """Используя подготовленную строку nat, получить новую строку, в которой в имени интерфейса вместо FastEthernet написано GigabitEthernet. Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print."""

    nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
    def __init__(self, words):
        self._changing_word = words

    def getAnswer(self):
        index = Exersize4_1.nat.index(self._changing_word)
        new_string = Exersize4_1.nat[:index] + "GigabitEthernet" + Exersize4_1.nat[(index + len(self._changing_word)):]
        print(new_string)

    def getAnswer_2(self):
        new_string = Exersize4_1.nat.replace("Fast", "Gigabit")
        print(new_string)

class Exersize4_2:
    __doc__ = """Преобразовать строку в переменной mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print."""

    mac = "AAAA:BBBB:CCCC"

    def getAnswer(self):
        new_string = Exersize4_2.mac.replace(":", ".")
        print(new_string)


class Exersize4_3:
    __doc__ = """Записать итоговый список в переменную result. (именно эта переменная будет проверяться в тесте)\nПолученный список result вывести на стандартный поток вывода (stdout) с помощью print. Тут очень важный момент, что надо получить именно список (тип данных), а не, например, строку, которая похожа на показанный список."""

    config = "switchport trunk allowed vlan 1,3,10,20,30,100"

    def getAnswer(self):
        result = Exersize4_3.config.split(' ')[-1].split(',')
        print(result)


class Exersize4_4:
    __doc__ = """Список vlans это список VLANов, собранных со всех устройств сети, поэтому в списке есть повторяющиеся номера VLAN.

    Из списка vlans нужно получить новый список уникальных номеров VLANов, отсортированный по возрастанию номеров. Для получения итогового списка нельзя удалять конкретные vlanы вручную.

    Записать итоговый список уникальных номеров VLANов в переменную result. (именно эта переменная будет проверяться в тесте)Полученный список result вывести на стандартный поток вывода (stdout) с помощью print."""

    vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]

    def getAnswer(self):
        result = sorted(set(Exersize4_4.vlans))
        print(result)
        print(type(result))


class Exersize4_5:
    __doc__ = """Из строк command1 и command2 получить список VLANов, которые есть и в команде command1 и в команде command2 (пересечение).
    В данном случае, результатом должен быть такой список: ['1', '3', '8']
    Записать итоговый список в переменную result. (именно эта переменная будет проверяться в тесте)
    Полученный список result вывести на стандартный поток вывода (stdout) с помощью print."""
    command1 = "switchport trunk allowed vlan 1,2,3,5,8"
    command2 = "switchport trunk allowed vlan 1,3,8,9"

    def getAnswer(self):
        vlan_1 = Exersize4_5.command1.split()[-1].split(",")
        vlan_2 = Exersize4_5.command2.split()[-1].split(",")
        result = sorted(set(vlan_1) & set(vlan_2))
        print(result)
        print(type(result))


class Exersize4_6:
    __doc__ = """Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
    Prefix                10.0.24.0/24
    AD/Metric             110/41
    Next-Hop              10.0.13.3
    Last update           3d18h
    Outbound Interface    FastEthernet0/0"""
    
    ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

    def better_solution(self):
        output = "\n{:25} {}" * 5

        route = Exersize4_6.ospf_route.replace(",", "").replace("[", "").replace("]", "")
        print(output.format(
                "Prefix", route[0],
                "AD/Metric", route[1],
                "Next-Hop", route[3],
                "Last update", route[4],
                "Outbound Interface", route[5],
        ))
        print(datetime.now() - start_time)

    def getAnswer(self):
        output = "\n{:25} {}" * 5

        route = Exersize4_6.ospf_route.split()
        """for a in route:
            index = route.index(a)
            route[index] = a.strip("],[")"""

        for i in range(0, len(route)):
            route[i] = route[i].strip("],[")
            i = i + 1

        print(output.format(
                "Prefix", route[0],
                "AD/Metric", route[1],
                "Next-Hop", route[3],
                "Last update", route[4],
                "Outbound Interface", route[5],
        ))
        print(datetime.now() - start_time)


class Exersize4_7:
    __doc__ = """Преобразовать MAC-адрес в строке mac в двоичную строку такого вида: „101010101010101010111011101110111100110011001100“

    Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print."""
    mac = "AAAA:BBBB:CCCC"

    def getAnswer(self):
        result = "{:b}".format(int(Exersize4_7.mac.replace(":", ""), 16))
        print(result)


class Exersize4_8:
    __doc__ = """Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:

    *первой строкой должны идти десятичные значения байтов
    *второй строкой двоичные значения

    Вывод должен быть упорядочен также, как в примере:

    *столбцами
    *ширина столбца 10 символов (в двоичном формате надо добавить два пробела между столбцами для разделения октетов между собой)

    Пример вывода для адреса 10.1.1.1:

    10        1         1         1
    00001010  00000001  00000001  00000001
    Ограничение: Все задания надо выполнять используя только пройденные темы."""
    ip = "192.168.3.1"

    def getAnswer(self):
        ip_parts = Exersize4_8.ip.split(".")
        """start_time = datetime.now()
        for element in ip_parts:
            result = "\n{:<10}".format(int(element, 10))
            result += "\n{:<10b}".format(int(element, 10))
            print(result)
        print(datetime.now() - start_time)"""

        start_time = datetime.now()
        output = """
        {0:<10}{1:<10}{2:<10}{3:<10}
        {0:<08b}  {1:<08b}  {2:<08b}  {3:<08b}"""

        print(output.format(int(ip_parts[0]), int(ip_parts[1]), int(ip_parts[2]), int(ip_parts[3])))
        print(datetime.now() - start_time)

if __name__ == "__main__":
    #exersize_4_1 = Exersize4_1("FastEthernet")
    #print(exersize_4_1.__doc__)
    #exersize_4_1.getAnswer()

    #exersize_4_2 = Exersize4_2()
    #print(exersize_4_2.__doc__)
    #exersize_4_2.getAnswer()

    #exersize_4_3 = Exersize4_3()
    #print(exersize_4_3.__doc__)
    #exersize_4_3.getAnswer()

    #exersize_4_4 = Exersize4_4()
    #print(exersize_4_4.__doc__)
    #exersize_4_4.getAnswer()

    #exersize_4_5 = Exersize4_5()
    #print(exersize_4_5.__doc__)
    #exersize_4_5.getAnswer()

    #exersize_4_6 = Exersize4_6()
    #print(exersize_4_6.__doc__)
    #exersize_4_6.getAnswer()
    #exersize_4_6.better_solution()

    #exersize_4_7 = Exersize4_7()
    #print(exersize_4_7.__doc__)
    #exersize_4_7.getAnswer()
    
    exersize_4_8 = Exersize4_8()
    print(exersize_4_8.__doc__)
    exersize_4_8.getAnswer()

