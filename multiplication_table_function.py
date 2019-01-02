def multiplication_table(x = 1):
    x = int(x)
    for i in range(1,11,1):
        print(x,"X",i,'=',x*i)

y = input("Write an Integer and Press Enter")

multiplication_table(y)
multiplication_table()