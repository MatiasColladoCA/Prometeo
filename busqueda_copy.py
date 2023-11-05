import json
     

# def opciones_input(inp):
#     '''
#     Depende de nuevo_link()
#     Descripción: añade los strings que se indiquen por input, al menos que se escriba "s" para omitir el dato pedido.
    
#     inp = string especificado por el usuario para crear u omitir datos.
#     '''
#     if inp == "s":
#         print("El dato se omitirá")
#         return ""
#     else:
#         return inp
    


# Abre el archivo JSON
with open('datos.json', 'r') as f:
    # Carga el contenido del archivo JSON en una variable
    data = f.read()
data = json.loads(data)

# with open('datos_copy.json', 'r') as f:
#     # Carga el contenido del archivo JSON en una variable
#     data_new = f.read()
# data_new = json.loads(data_new)


new_data = [{"Espanol":{}}, {"Ingles":{}}]

#tomamos los values de categorias por separado
lista_values = []
for i, elem in enumerate(data):
    for key, value in elem.items():
        if key == "categ":
            lista_values.append(value)

#añadimos mas categorias
lista_values = list(set(lista_values))
lista_values.append('Ciencia')
lista_values.append('Documentales')
lista_values.append('Tecnologia')
lista_values.append('Software')

# print(new_data)

#creamos diccionarios con las categorias
for i, elem in enumerate(new_data):
    for value in elem.values():
        for j in lista_values:
            
            value[j] = []


# for i, elem in enumerate(new_data):# cada uno de los 2 elementos (español, ingles)
#     for value in elem.values():#cada diccionario de los idiomas
#         for categ, dict in value.items():#cada item de los idiomas (categorias: {})
#             # print(dict)
#             # print(categ)
#             dict[lista_values]


new_data = json.dumps(new_data, indent=4)
with open('datos_copy.json', 'w') as f:
        # Escribir el objeto Python en formato JSON
        f.write(new_data)


# print(json.dumps(new_data, indent=4))
# newDicc = {"link": link, "idioma": idiomaValue, "categ":categValue, "nombre": nombreValue, "desc": descValue}
# print(newDicc)
# data.append(newDicc)
# for elem in data:
#     print(type(elem))
#     elem["icono"] = ""
# data = json.dumps(data, indent=2)


# # Sobrescribir el archivo JSON
# with open('datos.json', 'w') as f:
#     # Escribir el objeto Python en formato JSON
#     f.write(data)


