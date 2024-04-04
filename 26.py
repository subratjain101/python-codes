range_tuple = (10, 20, 30, 40, 50)
num = int(input("Enter your number: "))

is_in_range = False

for i in range(len(range_tuple)-1):
    if num >= range_tuple[i] and num <= range_tuple[i+1]:
        print(f"The number {num} falls within the range of the {range_tuple[i]} and its next {range_tuple[i+1]} values of the tuple")
        is_in_range = True
        break

if not is_in_range:
    print(f"The value {num} does not fall between any 2 consecutive values of the tuple")
