# Main file

# Mi primera impresion en terminal
# print("Hola mundo")

""" Comentario multilinea
    Es decir que puede tener varias lineas
    a la vez y cuantas mas queramos """

year = 2026
name = "Salvador"
Age = 80

# Valor entero
intValue = 10
# Valor decimal / flotante
floatValue = 10.5
# valor de texto / sctring
strValue = "Valor de texto"
# Valor de booleano -> verdadero o falso
boolValueTrue = True
# print(boolValueTrue)

boolValueFalse = False
boolValueTrue = "False"

# print(year)
# print(name)
# print(Age)

# print()
# print("---------")
# print()

# print(intValue)
# print(floatValue)
# print(strValue)
# print(boolValueFalse)
# print(boolValueTrue)

# Ver el tipo de variable
# typeValue = type(boolValueTrue)
# print(typeValue)


# Operaciones matematicas
# 5 + 2
# print(5 + 2)
# print(10 / 3)
# print(10 // 3)

# print(10 % 3)
# print(10 % 5)

# 3 ** 2 -> 3^2

# print(3 ** 2)

# print(1 == 1) # 1 es igual a 1
# print(1 != 1) # 1 es diferente a 1?
# print(1 > 1) # 1 es Mayor a 1?
# print(1 < 1) # 1 es Menor a 1?
# print(1 >= 1) # 1 es Mayor o igual a 1?
# print(1 <= 1) # 1 es Menor o igual a 1?

# age = int(input("Dame tu edad: "))
# age = 6

# if age >= 50:
#     print("Usted ya es un señor")
# elif age == 20 and name == "alvador":
#     print("Tienes 20 salvador")
# elif age == 20:
#     print("Tienes 20")
# elif age >= 18:
#     print("Eres mayor de edad")
# elif age >= 13:
#     print("Eres adolescente")
# elif age == 7:
#     print("Eres nene")
# else:
#     print("Eres niño")


# i = 0
# while i < 5:
#     print(i)
#     i += 1

# password = ""
# while password != "1234":
#     password = input("Contraseña: ")
"""
Se utiliza para dar un numero n de vueltas en el ciclo
hasta que se cumpla una condicion.
Funciona por condiciones
"""

# for i in range(5):
#     print(i)

"""
Se utiliza con listas, textos, diccionarios o rangos.
funciona por iteracion.
for, en python, significa "para cada elemento en esta coleccion... haz esto..."
"""

students = ["Anna", "Gabriel", "Cristian"]
# for item in students:
#     print("Hola", item)

numbers = [1, 2, 3]
numbers.append(4)
numbers.append(5)
# print(numbers)

coords = (10, 20)
# coords.append(30) # No se puede ejecutar en una tupla

people = {"nombre": "Ana", "edad": 20}
# print(people["nombre"])
# print(people["edad"])

items = {1, 2, 3, 3, 3}
# print(set(items))

print(students)
print(students[0])
print(students[2])
print(students[0:2])
print(students[0:3])
print(students[2][::-1])