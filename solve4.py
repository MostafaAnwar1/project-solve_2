x = int(input("Enter the frist number:"))
y = int(input("Enter the second number:"))
if y == 0:
    print("You can't divide by zero please enter another number")
else:
    print("The numbers are:")
    for i in range(0,x+1):    
        if i % y == 0:
            print(i)
        
