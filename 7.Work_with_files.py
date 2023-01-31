from sys import argv
from datetime import datetime

class Task_7_1:
    __doc__="""
    Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде на стандартный поток вывода:

    Prefix                10.0.24.0/24
    AD/Metric             110/41
    Next-Hop              10.0.13.3
    Last update           3d18h
    Outbound Interface    FastEthernet0/0"""
    cfg_lines = ['Prefix                10.0.24.0/24',
    'AD/Metric             110/41',
    'Next-Hop              10.0.13.3',
    'Last update           3d18h',
    'Outbound Interface    FastEthernet0/0']
    def __new__(self):
          with open('ospf.txt', 'w+') as f:
            f.write("\n".join(Task_7_1.cfg_lines))
            for line in f:
                print(line)


class Task_7_2:
    __doc__="""
    Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt. Имя файла передается как аргумент скрипту.
    Скрипт должен возвращать на стандартный поток вывода команды из переданного конфигурационного файла, исключая строки, которые начинаются с !.
    Вывод должен быть без пустых строк."""
    start_time = datetime.now()

    input_filename = argv[1]
    def __new__(self):
        with open(Task_7_2.input_filename) as f:
            for line in f:
                if line[0] != "!":
                    print(line.strip())
        print("Task_7_2 Time: ", datetime.now() - Task_7_2.start_time)
    



class Task_7_2_a:
    __doc__="""
    Сделать копию скрипта задания 7.2.
    Дополнить скрипт: Скрипт не должен выводить команды, в которых содержатся слова, которые указаны в списке ignore.
    При этом скрипт также не должен выводить строки, которые начинаются на !.
    Проверить работу скрипта на конфигурационном файле config_sw1.txt. Имя файла передается как аргумент скрипту."""
    start_time = datetime.now()
    input_filename = argv[1]
    ignore = ["duplex", "alias", "configuration"]
    ignore.append("!")
    def __new__(self):
        with open(Task_7_2_a.input_filename) as f:
            for line in f:
                line_words = line.split()
                words_intersect  = set(line_words) & set(Task_7_2_a.ignore)
                if not words_intersect:
                    print(line.strip())
        print("Task_7_2_a Time: ", datetime.now() - Task_7_2_a.start_time)


class Task_7_3:
    __doc__="""
    Сделать копию скрипта задания 7.2.
    Дополнить скрипт: Скрипт не должен выводить команды, в которых содержатся слова, которые указаны в списке ignore.
    При этом скрипт также не должен выводить строки, которые начинаются на !.
    Проверить работу скрипта на конфигурационном файле config_sw1.txt. Имя файла передается как аргумент скрипту."""
    start_time = datetime.now()
    input_filename = argv[1]
    def __new__(self):
        with open(Task_7_3.input_filename) as f:
            for line in f:
                line_words = line.split()
                if line_words and line_words[0].isdigit():
                    vlan, mac_address, _,port = line_words
                    print(f"{vlan:9}{mac_address:20}{port:6}")
        print("Task_7_2_a Time: ", datetime.now() - Task_7_3.start_time)   

if __name__ == "__main__":
    #task = Task_7_1()
    #task = Task_7_2()
    #task = Task_7_2_a()
    task = Task_7_3()
