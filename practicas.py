numero = [1, 2, 6, 2, -5]

def obtener_mayor(numeros):
    mayor = 0
    for i in numeros:
        if i > mayor:
            mayor = i
    return mayor

print(obtener_mayor(numero))

def invertir_lista(elementos):
    return elementos.reverse()
    
invertir_lista(numero)
    
print(numero)
    
def eliminar_duplicados(numeros):
    return set(numeros)

print(eliminar_duplicados(numero))

def filtrar_positivos(numeros):
    return list(filter( lambda n: n > 0, numeros))

print(filtrar_positivos(numero))

producto = [1, 2, 3, 4, 5, 6, 7, 8, 9]
buscar = 7

def buscar_elemento(productos, buscado):
    for i in productos:
        if buscado == productos[i]:
            return print("Producto encontrado")
    
buscar_elemento(producto, buscar)

words = ["sal", "mangos", "ir", "cocer"]

def filtrar_palabras_largas(palabras):
    return [elem for elem in palabras if  len(elem) > 5]


print(filtrar_palabras_largas(words))

def contar_palabras_largas(palabras):
    contador = 0
    for elemento in palabras:
        if len(elemento) > 5:
            contador += 1
    return contador

print(contar_palabras_largas(words))

notas = [47, 76, 86]

def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones) 

print(f"{calcular_promedio(notas):.2f}")

def sumar_lista(numeros):
    print(numeros)
    return sum(numeros)

print(sumar_lista(numero))

def contar_pares(numeros):
    contador = 0
    for i in numeros:
        if i % 2 == 0:
            contador +=1
    return contador

print(contar_pares(numero))

def clasificar_notas(notas):
    clasificacion = []
    for i in notas:
        if i > 59:
            clasificacion.append("Aprobado")
        else:
            clasificacion.append("Reprobado")
    return clasificacion

print(clasificar_notas(notas))