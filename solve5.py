x = int(input("Enter the frist number:"))
y = int(input("Enter the second number:"))

print("The numbers are:")
for i in range(101):
    if i % x == 0 and i % y == 0:
        print(i)
