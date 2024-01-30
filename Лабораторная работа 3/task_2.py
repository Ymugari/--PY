# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separate=","):
    first_group = first_group.split(separate)
    second_group = second_group.split(separate)
    intersection_ = list(set(first_group).intersection(second_group))
    intersection_.sort()

    return intersection_


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))
