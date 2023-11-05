import json
import svgwrite

def load_tree_data(json_file):
    with open(json_file, 'r') as file:
        tree_data = json.load(file)
    return tree_data


def draw_node(dwg, node, x, y):
    # Dibuja un círculo blanco en las coordenadas (x, y)
    dwg.add(dwg.circle(center=(x, y), r=3, fill="white"))
    
    # # Agrega el nombre del nodo como etiqueta
    # dwg.add(dwg.text(node["concept"], insert=(x - 5, y + 10), fill="white", font_size="10"))
    
    # Agrega el nombre del nodo como etiqueta centrado horizontalmente
    text = dwg.text(node["concept"], insert=(x, y + 20), fill="white", font_size="20")
    text['text-anchor'] = 'middle'  # Establece el anclaje del texto en el medio
    dwg.add(text)


def draw_lines(dwg, parent, children, spacing_x, spacing_y):
    x1 = parent["x"]
    y1 = parent["y"]

    for child in children:
        x2 = child["x"]
        y2 = child["y"]

        dwg.add(dwg.line((x1, y1), (x2, y2), stroke=svgwrite.rgb(255,255,255, '%'), stroke_width="3px"))




def draw_tree(dwg, data, x, y, spacing_x, spacing_y, level=0):
    data["x"] = x
    data["y"] = y

    draw_node(dwg, data, x, y)

    if "children" in data:
        children = data["children"]
        num_children = len(children)

        if num_children > 0:
            total_height = num_children * spacing_y
            start_x = x + spacing_x
            start_y = y - total_height / 2
            
            for child_data in children:
                child_height = draw_tree(dwg, child_data, start_x, start_y + spacing_y / 2, spacing_x, spacing_y, level + 1)
                draw_lines(dwg, data, [child_data], spacing_x, spacing_y)
                start_y += spacing_y

            return total_height

    return spacing_x




def create_tree_svg(data, output_file, position_father):
    # Crea un lienzo SVG con un ancho y alto suficientes para el árbol
    width = 800
    height = 600
    dwg = svgwrite.Drawing(output_file, profile='tiny', size=(width, height))

    # Agregar un atributo id al elemento <svg>
    dwg.attribs['id'] = 'svg'
    
    # Llama a la función para dibujar el árbol
    draw_tree(dwg, data, 100, position_father, 100, 30)

    # Guarda el archivo SVG
    dwg.save()

if __name__ == "__main__":
    
    listJSON = ["treePhilosophy.json", "treeRight.json"]
    # Carga los datos del archivo JSON
    
    for elem in range(len(listJSON)):
        tree_data = load_tree_data(elem)
    
    
        # json_file = "philosophyTree.json"
        # tree_data = load_tree_data(json_file)

        # Nombre del archivo de salida
        output_file = "allSVG.svg"

        # Crea el árbol SVG y guárdalo en un archivo
        create_tree_svg(tree_data, output_file)
    
    print("Ejecución terminada")