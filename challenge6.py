s = str(input("Palabra: "))

reverse_s = "".join(reversed(s.replace(" ", "")))

if reverse_s.lower() == s.replace(" ", "").lower() :
    print("Palindromo")
else:
    print("No es palindromo")
