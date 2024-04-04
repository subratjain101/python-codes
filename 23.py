mixed_tuple = (1, 2, 3, 4, 5, 1, 2, 3)
unique_list = []

for i in mixed_tuple:
    if i not in unique_list:
        unique_list.append(i)

unique_list = tuple(unique_list)
print(unique_list)
