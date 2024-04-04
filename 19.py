test_tuple = (1, 2, 3, 4, 1, 2, 1, 4, 5)

unique_check_list = []
frequency_list = []

for i in range(len(test_tuple)):
    if test_tuple[i] not in unique_check_list:
        unique_check_list.append(test_tuple[i])
        count = 0
        for j in range(i, len(test_tuple)):
            if test_tuple[j] == test_tuple[i]:
                count += 1
        frequency_list.append(count)

frequency_list = tuple(frequency_list)
print(frequency_list)
