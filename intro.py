from myFunctions import operAritmetic
from myFunctions import calcIva
from myFunctions import fibonacci
print("Hola Mundo en Python")

#Definición de variables
firstName = "Carlos"
lastName = "Sánchez"
age = 44
gender = False
salaryEmployee = 5000000
print(type(gender) )
#Lista
numbers=[1, 2, 3, 4, 5]
#Tupla
pair=(2,4,6,8)
#Diccionario
person={
    "cc": "1234567",
    "name": "John",
    "phone": "311258741",
    "gender": False,
    "salary": 3200000
}
#Arreglo de objetos
persons=[
    {
        "id":2,
        "firstName":"Carolina",
        "address":"calle 5 #3-2"
    },
    {
        "id":3,
        "firstName":"Juan",
        "address":"diagonal 1 #2-1"
    },
    {
        "id":4,
        "firstName":"Pedro",
        "address":"carrera 3 #1-3"
    }
    
]


#CONDICIONALES
'''
if not gender :
    print("El empleado es hombre")
else :
    print("El empleado es mujer")
'''    
    
    
#Operador ternario o condicional
print("Es mujer" if gender else "Es hombre")

comission = salaryEmployee * 10/100 if gender and salaryEmployee > 4000000 else salaryEmployee * 2/100
print(f"Comisión: {comission}")

category = "A"
valuePay = 0
if category == "A" :
    valuePay = 5000
elif category == "B" :
    valuePay = 100000
elif category == "C":
    valuePay = 20000
elif category == "D":
    valuePay = 30000
else:
    valuePay = 1000
print(f"Valor a pagar: {valuePay}")

#CICLOS

#Ciclo for
for i in range(1,6):
    print(f"Número: {i}")

for i in range(1,6,2):
#     if i < 6 -1:
#         print(i, end=",")
#     else:
#         print(i)
    print(i, end=", " if i < 6-1 else "")
    
    
for i in range(0,22,2):
    print(i)
    
#Ciclos para recorrer objetos iterables
print("Iteraccion en listas, tuplas, diccionarios, etc.")
for nro in numbers:
    print(nro)
    
print("--------------------")
for i in range(0, len(numbers)):
    print(numbers[i])

print("-------Cantidad de números pares e impares-------------")
countEven = 0
countOdd = 0
for num in numbers:
    if num % 2 == 0:
        countEven += 1
    else:
        countOdd += 1
print(f"cantidad de números pares {countEven}")
print(f"cantidad de números impares {countOdd}")

print("Recorrer una tupla")
todd=(1,3,5,7)
for n in todd:
    print(n)
    
print("Recorrer un set")
tpair={40,10,20,30}
for num in tpair:
    print(num)

print("Recorrer un Diccionario")
for key, value in person.items():
    print(f"{key}: {value}")
for item in person:
    print(f"{item}: {person[item]}")
    
print(person["cc"])

print("Mostrando los datos de la lista de diccionarios")
for person in persons:
    print(f"ID: {person['id']}, Nombre: {person['firstName']}, Dirección: {person['address']}")

print("Buscando el id de la lista persons")
idSearch = int(input('Ingrese el id de la persona:'))
flag = False #variable bandera
for person in persons:
    if person['id'] == idSearch:
        print(f"ID: {person['id']}, Nombre: {person['firstName']}, Dirección: {person['address']}")
        flag= True
        break
if not flag:
    print("No se encontró el id de la persona")
    
    
#FUNCIONES
def sumar(a,b):
    return a + b

def message(text):
    print(text)
    
#Llamando a las funciones
message("Hola mundo desde Python con métodos")
print(sumar(5,2))

num1 = int(input("Ingrese al valor 1: "))
num2 = int(input("Ingrese al valor 2: "))
resultado = sumar(num1, num2)
if sumar(num1, num2) > 20:
    message(f"El resultado es mayor a 20 es: {resultado}")
    

print("Funciones ")    
print(operAritmetic(34, 55, "+")) 
valIva=calcIva(100000)
print(f"El valor del iva de 100000 es {valIva}")


print(fibonacci(n))

#Prueba de cambio para este archivo
print("Haciendo prueba con el sistema de control de versiones")
