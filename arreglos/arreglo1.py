vector=[]
vector.append(2)
vector.append(5)
vector.append(6)
print(vector)
print("Tamaño:", len(vector))

#Mostrar el doble de cada elemento
print("Dobles de cada elemento:")
for i in range(len(vector)):
    if i != (len(vector) -1):
        print(vector[i]*2, end=", ")
    else:
        print(f"{vector[i]*2}.")
        
#Añadir en la posicion 1
vector.insert(1,36)
print(vector)

#Añadir en la posicion 0
vector.insert(0,67)
print(vector)