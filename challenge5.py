a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 3, 3, 3]

x = list(filter(lambda item : item in b, list(set(a))))

print(x)
