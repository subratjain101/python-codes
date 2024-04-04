tup =  (("Alice", 22), ("Bob", 19), ("Charlie", 25))

second_elements = []
for i in range(len(tup)):
    second_elements.append(tup[i][1])

second_elements.sort()

sorted_list = []
for i in second_elements:
   for j in tup:
       if i == j[1]:
           sorted_list.append((j[0], i))
           break

print(sorted_list)
