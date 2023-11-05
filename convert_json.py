import json

def add_nid(json_data, parent_nid="", depth=0):
    if isinstance(json_data, list):
        for i, item in enumerate(json_data):
            child_nid = f"{parent_nid}o{i + 1}"
            item["nid"] = child_nid
            add_nid(item, child_nid, depth + 1)
    elif isinstance(json_data, dict):
        for key, value in json_data.items():
            if isinstance(value, (list, dict)):
                add_nid(value, parent_nid, depth)



# Cargar el JSON desde "./datosArbol.json"
with open("./datosArbol.json", "r") as json_file:
    input_json = json.load(json_file)

# Copia del JSON de entrada y agregando "nid"
output_json = input_json.copy()
add_nid(output_json)

# Guardar el nuevo JSON en "./copy_datosArbol.json"
with open("./copy_datosArbol.json", "w") as output_file:
    json.dump(output_json, output_file, indent=4)

print("Se ha creado y guardado el nuevo JSON en './copy_datosArbol.json'.")      