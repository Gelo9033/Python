# break - ejemplo

#print("La instrucción break:")
#for i in range(1, 6):
#    if i == 3:
#        break
#    print("Dentro del bucle.", i)
#print("Fuera del bucle.")


# continue - ejemplo

# print("\nLa instrucción continue:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Dentro del bucle.", i)
# print("Fuera del bucle.")



frase=str(input("\nIntroduce una palabra o frase: "))
comFrase="todos estamos aprendiendo Python"
while True:
    if frase.lower() in comFrase:
        print("¡Encontrado!")
        break
    else:
        print("No encontrado, intenta de nuevo.")
        frase=str(input("Introduce una palabra o frase: "))
print("¡Gracias por participar!")