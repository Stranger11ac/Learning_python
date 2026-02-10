# 🐍 Guía de Python para principiantes

## Introducción rápida (antes de programar)

**Objetivo**: que entiendan qué es Python y cómo se ejecuta.

- ¿Qué es Python?
- ¿Para qué se usa? (web, automatización, IA, data, apps)
- Diferencia entre:
  - Lenguaje interpretado (Python)
  - Lenguaje compilado
- Qué es un script (.py)
- Qué es la terminal / consola
- Cómo correr Python:
  - python archivo.py
  - o usar un editor como VS Code

## 1) Primeros pasos: imprimir y comentarios

**Objetivo**: empezar con lo más simple.

- print("Hola mundo")
- Comentarios:
  - \# comentario de una línea
  - """ comentario multilínea """

## 2) Variables

**Objetivo**: que entiendan que una variable es una etiqueta para guardar valores.

- Crear variables:

  ```python
  nombre = "Salvador"
  edad = 25
  ```

- Reglas de nombres:
  - no empezar con números
  - no usar espacios
  - evitar palabras reservadas (class, for, if, etc.)
- Convención recomendada:
  - snake_case → mi_variable

## 3) Tipos de valores

En Python las variables no “tienen tipo fijo”, el tipo lo tiene el valor.
**Tipos básicos**:

- int → enteros: 10
- float → decimales: 10.5
- str → texto: "hola"
- bool → True / False
- NoneType → None (nada / vacío)

Ver tipo:

```python
type(edad)
```

## 4) Operadores (matemáticos y lógicos)

**Objetivo**: que puedan hacer cálculos y lógica.

**Matemáticos**:

- \+ - * /
- // -> división entera
- % -> módulo
- ** -> potencia

**Comparación**:

== != > < >= <=

**Lógicos**:

- and
- or
- not

## 5) Entrada de usuario

input() siempre devuelve string:

```python
edad = int(input("Dame tu edad: "))
```

## 6) Condicionales (if / elif / else)

**Objetivo**: tomar decisiones.

```python
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres niño")
```

Tema clave: indentación

- Python usa indentación en vez de {}

## 7) Ciclos (loops)

### Ciclowhile

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### Ciclo for

```python
for i in range(5):
    print(i)
```

---

**Extras súper básicos**:

- break (romper ciclo)
- continue (saltar vuelta)

## 8) Estructuras de datos

**Listas (list)**:

```python
numeros = [1, 2, 3]
numeros.append(4)
```

**Tuplas (tuple)**:

```python
coords = (10, 20)
```

**Diccionarios (dict)**:

```python
persona = {"nombre": "Ana", "edad": 20}
print(persona["nombre"])
```

**Conjuntos (set)**:

```python
items = {1, 2, 3}
```

## 9) Acceso, slicing y métodos comunes

**Objetivo**: que puedan manipular strings y listas.

- Index:
  - lista[0]
  - texto[1]
- Slicing:
  - lista[0:3]
  - texto[::-1] (invertir)

Métodos comunes:

- len()
- .upper() .lower(), .strip()
- .append(), .pop(), .remove()
- .keys(), .values(), .items()

## 10) Anidación (lo que pediste)

**Objetivo**: entender estructuras dentro de estructuras.

Condicional dentro de ciclo:

```python
for n in range(10):
    if n % 2 == 0:
        print(n, "es par")
```

Lista de diccionarios:

```python
usuarios = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 30}
]
```

## 11) Funciones (fundamental)

**Objetivo**: evitar repetir código.

```python
def saludar(nombre):
    return f"Hola {nombre}"
```

Parámetros y retorno

- return
- funciones sin return → regresan None

Valores por defecto

```python
def saludar(nombre="Invitado"):
    print("Hola", nombre)
```

## 12) Scope

**Objetivo**: que entiendan variables locales y globales.

- Variables dentro de **funciones** = locales
- Variables **fuera** = globales

## 13) Manejo de errores (try/except)

**Objetivo**: que no se rompan al primer error.

```python
try:
    x = int(input("Número: "))
except ValueError:
    print("Eso no es un número")
```

## 14) Archivos (básico real de la vida)

Leer y escribir archivos.

```python
with open("archivo.txt", "w", encoding="utf-8") as f:
    f.write("Hola")
```

```python
with open("archivo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
```

## 15) Módulos e imports

**Objetivo**: que sepan reutilizar código y usar librerías.

```python
import math
print(math.sqrt(16))
```

- import x
- from x import y
- as para alias

## 16) Programación Orientada a Objetos (POO)

Aquí entran clases, objetos, herencia, etc.

Clase y objeto

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, soy", self.nombre)
```

```python
p1 = Persona("Ana", 20)
p1.saludar()
```

Conceptos clave:

- \_\_init__ = constructor
- self = referencia al objeto actual
- atributos
- métodos
