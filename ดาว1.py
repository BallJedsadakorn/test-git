n = int(input())

line = 0
while line < n:
    
    star = 0
    while star < line:
        print(" ", end = "")
        star += 1
    star = n
    while star > line:
        print("*",end = "")
        star -= 1
    print()
    line += 1