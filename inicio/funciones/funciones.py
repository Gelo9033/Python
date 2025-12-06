



# def message():
#     print("Ingresar valor: ")

# message()
# a = int(input())
# message()
# b = int(input())
# message()
# c = int(input())

# result=a + b + c
# print("El resultado de la suma es: ", result)


# number = float(input ("ingrese el numero: "))
# def message(number):
#     result= number*1.15
#     return result

#n= message(number)
#print("El número ingresdo es: ", message(number))


#ITERAR SOBRE UNA LISTA

nombres=[]
rango= int(input("¿Cuántos nombres desea ingresar? "))
for i in range(rango):
    nombres.append(input("Ingrese el nombre: "))
print("Los nombres ingresados son: ")
for nombre in nombres:
    print(nombre)   
    