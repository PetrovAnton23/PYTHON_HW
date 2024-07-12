def fizz_buzz(n):
    for x in range(1, n+1):
        if x % 3 == 0 and x % 5 == 0:
            print("fizz_buzz")
        if x % 3 == 0:
            print("fizz")
        if x % 5 == 0:
            print("buzz")
        else: 
            print(x)
n= int(input("Введите число: "))
fizz_buzz(n) 