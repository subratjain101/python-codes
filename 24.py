tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)

length = len(tuple1) if len(tuple1) > len(tuple2) else len(tuple2)
long_tup = tuple1 if len(tuple1) > len(tuple2) else tuple2
short_tup = tuple2 if len(tuple1) > len(tuple2) else tuple1
intersection_list = []

for i in range(length):
    if long_tup[i] in short_tup:
        intersection_list.append(long_tup[i])

print(tuple(intersection_list))
    
