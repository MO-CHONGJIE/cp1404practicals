# Q1
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# Q2
in_file = open("name.txt", "r")
name = in_file.read().strip()  # strip to remove any extra newline
in_file.close()
print(f"Hi {name}!")

# Q3
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number
    print(result)  # Should print 59 if numbers.txt contains 17, 42, 400

# Q4
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)  # Should print 459 if file has 17, 42, 400