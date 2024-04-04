test_tuple = (1, 2, 3, 4, 5)
num = int(input("Enter a number: "))
if num in test_tuple:
    print(f"{num} exists in the tuple")
else:
    print(f"{num} does not exist in the tuple")
