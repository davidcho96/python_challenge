
x = list(range(1, 100))

number = int(input("Número: "))

newX = list(filter(lambda i : number % i == 0, x))

print(newX)


