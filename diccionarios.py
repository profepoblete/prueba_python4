#declarar diccionario
diccionario_alumno = {
    "id":1
    ,"nombre":"Policarpo Avendaño"
    ,"edad":45
    ,"notas":[2.2,3.3,4.4]
}

#vemos el diccionario
print(diccionario_alumno)

#mostrar elemento específico
print(f"Nombre: {diccionario_alumno.get("nombre")}")

#listar elementos
print("_____DATOS ALUMNO______")
print(f"nombre: {diccionario_alumno.get("nombre")}")
print(f"edad: {diccionario_alumno.get("edad")}")
print("NOTAS: ")
for n in diccionario_alumno.get("notas"):
    print(f"{n}")

#mostrar una nota
print(diccionario_alumno.get("notas")[1])

#agregar un elemento al diccionario

diccionario_alumno["asistencia"] = 72.5

print("datos con asistencia")
print(diccionario_alumno)

#modificar elemento

diccionario_alumno["edad"] = 38

print("datos modificados")
print(diccionario_alumno)

#eliminar elemento
diccionario_alumno.pop("asistencia")


print("datos eliminados")
print(diccionario_alumno)

#listar items diccionario
print("----- ITEMS DICCIONARIO----")
for llave, valor in diccionario_alumno.items():
    print(f"{llave} : {valor}")

lista_alumnos = [
    {
        "id":1
        ,"nombre":"Policarpo Avendaño"
        ,"edad":45
        ,"notas":[2.2,3.3,4.4]
    }
    ,{
        "id":2
        ,"nombre":"Juan Nieve"
        ,"edad":22
        ,"notas":[2,1.8,2.5]
    }
]

print("LISTADO DE ALUMNOS")
for alum in lista_alumnos:
    print("DATOS ALUMNO")
    for llave, valor in alum.items():
        print(f"{llave}: {valor}")