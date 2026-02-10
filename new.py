print("hola mundo")

fistname = "Salvador" #string
year = 2026 # numero / enter / int
lastYear = 2025
# *nextyear = 2027
# "nextyear = 2027
# 6nextyear = 2027

varFloat = 10.53434 # float / decimal
varboolTrue = True
varboolFalse = False

n1 = 2
n2 = 6

# print("5 + 2") # "5 + 2"
# print(5 + 2) # 7
# print(n1 * n2)
# print(n1 % n2)
# print(fistname)

Age = 15
# Age = int(input("Dame tu edad: "))

if Age >= 18:
    print("Eres mayor de edad")
# elif Age >= 13 and fistname == "Alvador":
#     print("Eres adolescente Alvador")
# elif Age >= 13 or fistname == "Alvador":
#     print("Eres adolescente Alvador")
# elif Age >= 13 and not fistname == "Alvador":
#     print("Eres adolescente Alvador")
# elif Age >= 13 and fistname != "Alvador":
#     print("Eres adolescente Alvador")
elif Age >= 13:
    print("Eres adolescente y no eres Alvador")
else:
    print("Eres niño")

# print()
# print("----")
# print()

i = 0
while i < 5:
    print(i)
    i += 1
    # break

# password = ""
# while password != "1234":
#     password = input("Contraseña: ")


print()

for numeroEnElRango in range(2):
    print(numeroEnElRango) # 0 - 99


alumnos = ["Ana", "Luis", "Carlos"]

for item in alumnos:
    print("Hola", item)

listObjects = ["texto", 12, 123.78, True]
print(listObjects)
listObjects.append("Otra cosa")
listObjects[0] = "Este texto"
print(listObjects)
