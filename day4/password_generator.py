#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")



nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

parola = []

for i in range(1,nr_letters+1):
  for letter in range (0,len(letters)):
    a = random.randint(0, len(letters)-1)
    b = letters[a]
  parola.append(b)

for i in range(1,nr_symbols+1):
  for letter in range (0,len(symbols)):
    a = random.randint(0, len(symbols)-1)
    b = symbols[a]
  parola.append(b)

for i in range(1,nr_numbers+1):
  for number in range (0,len(numbers)):
    a = random.randint(0, len(numbers)-1)
  parola.append(a)

print(parola)

random.shuffle(parola)
print(parola)

parola2 = ""
for i in parola:
  a =str(i)
  parola2 += a
print(f"{parola2}")


  

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P