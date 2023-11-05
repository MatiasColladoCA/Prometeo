import json

# LO USÉ PARA CONVERTIR LINKS EN COLUMNAS, A ELEMENTOS EN JSON
lista = []
with open("texttt.txt", "r") as f:
    for line in f:
        dicc = {"link": line, "nombre": "", "desc": ""}
        lista.append(dicc)


print(lista)
  
with open("datos.json", "w") as f:
    for i in lista:
        json.dump(i, f)
        f.write("\n")
