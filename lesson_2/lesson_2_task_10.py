def bank():
    procent = 10
    x = int(input("Колличество денег?" ": "))
    y = int(input("Колличество лет?"": "))

    for i in range(y):
        x = (x+procent*x/100)
    print("По итогу вы получаете", x, "рублей")
bank()
 