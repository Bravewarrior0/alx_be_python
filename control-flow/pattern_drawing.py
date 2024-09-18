size = int(input("Enter the size of the pattern: "))
i = 0
while i < size:
    i+=1
    for j in range(0, size):
        print("*", end="")
    print("")