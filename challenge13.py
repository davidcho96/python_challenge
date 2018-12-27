fibonnaci_list = []

number = int(input("Ingresa un valor numérico: "))

for n in range(1, number+1):
	if len(fibonnaci_list) == 0:
		fibonnaci_list.append(n)
	elif len(fibonnaci_list) == 1:
		fibonnaci_list.append(1)
	else:
		fibonnaci_list.append(fibonnaci_list[n-2] + fibonnaci_list[n-3])

print(fibonnaci_list)
