from traceback import print_tb


print(1 < 1)
print(1 <= 1)
print(1 > 1)
print(1 >= 1)
print(1 == 1)
print(1 != 1)


name = input("What's your name? ")
if name == "Jonathan":
    print(f"Hello, nice to see you {name}!")
elif name == "Jack":
    print("Hello, you are a great person!")
elif name == "Adrian":
    print(f"Hi {name}, let's have lunch soon!")
else:
    print("Have a nice day!")