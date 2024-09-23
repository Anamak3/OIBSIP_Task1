import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("welcome to the password genrator!")
nr_letter=int(input("how many letters would you like in your password?\n"))
nr_symbol=int(input(f"how many symbols would you like ?\n"))
nr_number=int(input(f"how many numbers would you like ?\n"))
password_list=[]
for char in range(1,nr_letter+1):
    password_list.append(random.choice(letters))

for char in range(1,nr_symbol+1):
    password_list.append(random.choice(symbols))

for char in range(1,nr_number+1):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)

print(password_list)
password=""
for char in password_list:
    password=password+char
print(f"your password is \n{password}")

