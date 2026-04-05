def find_common_participants(group1, group2, separator=","):
    first = group1.split(separator)
    second = group2.split(separator)
    set1 = set(first)
    set2 = set(second)
    common = set1.intersection(set2)
    result = list(common)
    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, "|")
print(common_participants)
