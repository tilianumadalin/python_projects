import random

letters = ['a','b','c','d','e','f','g','h','i','j','i','j']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*',"(",")"]

print("Welcome to the PyPassword Generator\n")
nr_letters = int(input("How many letters?\n"))
nr_numbers = int(input("How many numbers?\n"))
nr_symbols = int(input("How many symbols?\n"))

password = [letters,numbers,symbols]
new_password = []
for i in range(0,nr_letters):
    new_password.append(letters[random.randint(0,int(len(letters)-1))])
for i in range(0,nr_numbers):
    new_password.append(numbers[random.randint(0,int(len(numbers)-1))])
for i in range(0,nr_symbols):
    new_password.append(symbols[random.randint(0,int(len(symbols)-1))])
    random_password = new_password
    random.shuffle(random_password)
print(f"Your password is: {''.join(random_password)}")
