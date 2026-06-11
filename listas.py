#declarar listas
listaIds = [1,2,3]
listaNombres = ["Juan Nieve","Antonio Estarko","María Sue"]
listaEdades = [21,40,22]


#listar
for nombre in listaNombres:
    print(f"{nombre}")

#listar con funcion zip
print("LISTADO DE PERSONAS")
for id, nombre, edad in zip(listaIds,listaNombres,listaEdades):
 
    print(f"id: {id}, nombre: {nombre}, edad: {edad}")

#listar por indice o posición
print("LISTADO DE PERSONAS POR INDICE")
for i in range(len(listaNombres)):
 
    print(f"id: {listaIds[i]}, nombre: {listaNombres[i]}, edad: {listaEdades[i]}")

#agregar
id = max(listaIds)+1
nombre = input("Ingrese nombre: ")
edad = int(input("Ingrse edad: "))
listaIds.append(id)
listaNombres.append(nombre)
listaEdades.append(edad)

print("LISTADO DE PERSONAS POR INDICE 2")
for i in range(len(listaNombres)):
 
     print(f"id: {listaIds[i]}, nombre: {listaNombres[i]}, edad: {listaEdades[i]}")


#buscar elemento
idBuscar = int(input("Ingrese id de la persona: "))

if idBuscar in listaIds:
    indice = listaIds.index(idBuscar) #index retorna el indice el elemento enviado
    print(f"id: {listaIds[indice]}, nombre: {listaNombres[indice]}, edad: {listaEdades[indice]}")
else:
    print("No existe la persona")

#Modificar elemento
idBuscar = int(input("Ingrese id de la persona a modificar: "))

if idBuscar in listaIds:
    indice = listaIds.index(idBuscar) #index retorna el indice el elemento enviado
    nombre = input("Ingrese nuevo nombre: ")
    edad = int(input("Ingrese nueva edad: "))
    listaNombres[indice] = nombre
    listaEdades[indice] = edad
    print("Datos modificados")

    print(f"id: {listaIds[indice]}, nombre: {listaNombres[indice]}, edad: {listaEdades[indice]}")
else:
    print("No existe la persona")

#Eliminar elemento
idBuscar = int(input("Ingrese id de la persona a eliminar: "))

if idBuscar in listaIds:
    indice = listaIds.index(idBuscar) #index retorna el indice el elemento enviado
    listaIds.pop(indice)
    listaNombres.pop(indice)
    listaEdades.pop(indice)
    print("Datos eliminados")
else:
    print("No existe la persona")


print("LISTADO DE PERSONAS POR INDICE 3")
for i in range(len(listaNombres)):
 
     print(f"id: {listaIds[i]}, nombre: {listaNombres[i]}, edad: {listaEdades[i]}")
