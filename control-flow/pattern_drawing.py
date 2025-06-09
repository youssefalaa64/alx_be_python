integer = int(input("Enter the size of the pattern: "))
current_row = 0
while integer > current_row :
    for i in range(1,integer+1) :
        print("*" , end="")
    print()
    current_row += 1

