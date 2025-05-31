minimum_length = 7

password = input("enter password:")
while len(password) < minimum_length:
    print("password must be at least 7 characters")
    password = input("enter password:")

for i in range (len(password)):
    print("*", end="")