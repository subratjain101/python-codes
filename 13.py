num_tuple = (10, 20, 30, 40, 50)

highest = 0

for i in range(len(num_tuple)):
    if num_tuple[highest] < num_tuple[i]:
        highest = i

print(num_tuple[highest])

