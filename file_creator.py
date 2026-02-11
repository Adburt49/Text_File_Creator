name = input("What's your name? \April Burton\n")
color = input("What's your favorite color? \Purple\n")
with open('example.txt', 'w') as file:

 file.write(f"{name} created this file and their favorite color is {color}")