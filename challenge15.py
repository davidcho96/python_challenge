def backwards(text:str):
	text_arr = text.split(" ")
	reverse = text_arr[::-1]
	return " ".join(reverse)

print(backwards(str(input("Texto: "))))
