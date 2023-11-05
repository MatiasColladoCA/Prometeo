import json

'''agregar documentacion'''


def crear_elem(data):
    '''
    Descripción: crea 
    '''
    listaElem = []
    for elem in data:
        for key, value in elem.item():
            if key == "link":
                link = value
                htmlElem = "<li><a href"
    
    '''...'''
            

def opciones_input(inp):
    '''
    Depende de nuevo_link()
    Descripción: añade los strings que se indiquen por input, al menos que se escriba "s" para omitir el dato pedido.
    
    inp = string especificado por el usuario para crear u omitir datos.
    '''
    if inp == "s":
        print("El dato se omitirá")
        return ""
    else:
        return inp
    
#Añade un link con todas las propiedades
def nuevo_link(data, link):
    '''
    Depende de buscar_en_json()
    Descripción: permite la edición del JSON que contiene los links si buscar_en_json() determina que no está almacenado en el JSON.
    Crea nuevos objetos con su respectivo link, idioma, categoria, nombre y descripción.
    
    data = objeto python para el JSON
    link = link para añadir al JSON.
    
    '''
    print("El link no se encontró. Será añadido. Ingrese los datos correspondientes que se pedirán a continuación.")
    #añade el resto de elementos correspondientes para el link
    idiomaValue = opciones_input(input("Ingrese el idioma: "))
    categValue = opciones_input(input("Ingrese la categoría: "))
    nombreValue = opciones_input(input("Ingrese el nombre: "))
    descValue = opciones_input(input("Ingrese la descripción: "))

    newDicc = {"link": link, "idioma": idiomaValue, "categ":categValue, "nombre": nombreValue, "desc": descValue}
    print(newDicc)
    data.append(newDicc)
    for elem in data:
        print(type(elem))
        elem["icono"] = ""
    data = json.dumps(data, indent=2)
    

    # Sobrescribir el archivo JSON
    with open('datos.json', 'w') as f:
        # Escribir el objeto Python en formato JSON
        f.write(data)


def buscar_en_json(data,link):
    '''
    Descripción: busca el link en el JSON data para corroborar su existencia o añadirlo.
    De no encontrarlo, redirige al método nuevo_link
    
    data = JSON
    link = link a buscar o añadir
    '''
    found = False
    for d in data:
    
        if link in d.values():
            found = True
            break
    
    #Si no se encuentra, hay que añadir la link:
    if found == False:
        print("asd")
        nuevo_link(data,link)




'''
Este programa se encarga de la edición del JSON que almacena la información de los links de la web PROMETEO.
El usuario indica si desea añadir un link o crear un elemento HTML
data = donde se carga el JSON.
orden = opción para añadir link o crear

'''
# Abre el archivo JSON
with open('datos.json', 'r') as f:
    # Carga el contenido del archivo JSON en una variable
    data = f.read()
data = json.loads(data)


orden = input("Indique opción: (1)Añadir, (2)Crear elemento html: ")

if orden == "1":
    
    # link que queremos buscar
    link = input("Ingrese el link para buscarlo en la lista: ")

    # Recorre todas las claves y valores del diccionario
    buscar_en_json(data,link)

elif orden == "2":
    crear_elem()

