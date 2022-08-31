
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

if __name__ == "__main__":
    #exersize_4_1 = Exersize4_1("FastEthernet")
    #print(exersize_4_1.__doc__)
    #exersize_4_1.getAnswer()

    #exersize_4_2 = Exersize4_2()
    #print(exersize_4_2.__doc__)
    #exersize_4_2.getAnswer()

    exersize_4_3 = Exersize4_3()
    print(exersize_4_3.__doc__)
    exersize_4_3.getAnswer()



