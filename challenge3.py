a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
#for value in a:
#    if value < 5:
#        b.append(value)
#print(b)

number = int(input("Number: "))
print(list(filter(lambda value : value < number, a)))
