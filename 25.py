nested_tuple = ((1, 2), (3, 4), (5, 6))

flatten_list = []

for i in range(len(nested_tuple)):
    for j in range(len(nested_tuple[i])):
        flatten_list.append(nested_tuple[i][j])

print(tuple(flatten_list))
