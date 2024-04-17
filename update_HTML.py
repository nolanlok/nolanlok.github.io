import os

def update_figures(path):
    figures = []
    for folder in os.listdir(path):
        if os.path.isdir(os.path.join(path, folder)):
            images = []
            for file in os.listdir(os.path.join(path, folder)):
                if file.endswith(".png"):
                    images.append(os.path.join(path, folder, file))
            figures.append({"folder": folder, "images": images})
    return figures

def write_to_file(figures, filename):
    with open(filename, 'w') as file:
        file.write("var figures = [\n")
        for figure in figures:
            file.write("    {\n")
            file.write(f"        folder: \"{figure['folder']}\",\n")
            file.write("        images: [\n")
            for image in figure['images']:
                file.write(f"            \"{image}\",\n")
            file.write("        ]\n")
            file.write("    },\n")
        file.write("];\n")

path = "figures"
updated_figures = update_figures(path)
write_to_file(updated_figures, "HTML_Update.txt")
