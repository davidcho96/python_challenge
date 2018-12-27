import random

random_number = random.randint(1, 9)

cont = 0

state = True

print("Puede finalizar el juego con la palabra 'exit'")

while state:
	cont += 1
	res = str(input("Qué número es?: "))
	if res.lower() == "exit":
		state = False
		print("Número de intentos {}".format(cont))
	elif int(res) == int(random_number):
		++cont
		state = False
		print("Correcto. Número de intentos {}".format(cont))
	elif int(res) < int(random_number):
		print("Demasiado bajo")
	elif int(res) > int(random_number):
		print("Demasiado alto")
