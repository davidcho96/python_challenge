def f():
    number = int(input("Número: "))
    verify = int(input("Verificador: "))
    if number % verify == 0:
        print("El número {} es divisor de {}".format(number, verify))
    elif number % 4 == 0:
        print("El número {} es divisor de 4".format(number))
    elif number % 2 == 0 :
        print("El número {} es par".format(number))
    else: 
        print("El número {} es impar".format(number))

if __name__ == "__main__":
    f()

