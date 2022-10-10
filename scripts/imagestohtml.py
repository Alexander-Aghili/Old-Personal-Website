#imports
from os import listdir
from PIL import Image
#inits
input_folder = "../images/cool/"  #Ensure all files in folder are .jpg
output_file = "./htmlgen.html"
to_src_folder = "./images/cool/"

file_list = listdir(input_folder)
final_html = ""


def get_names_for_file(file):
    id = file[:file.index("."):]
    modal_id = id + "Modal"
    modal_content_id = modal_id + "Content"
    return id, modal_id, modal_content_id

def get_image_orientation(file_src):
    with Image.open(file_src) as img:
        width, height = img.size
    if (width > height):
        return "horizontal image"
    else:
        return "vertical image"

def generate_html(file):
    id, modal_id, modal_content_id = get_names_for_file(file)
    file_src = input_folder + file
    file_src_name = to_src_folder + file
    image_orientation = get_image_orientation(file_src)
    html = "<div class=\"image-container\">\n"
    html += "\t<img class=\"" + image_orientation + "\" src=\"" + file_src_name + "\"\n"
    html += "\t\tid=\"" + id + "\" onclick=\"enlargeImg(\n"
    html += "\t\t\tdocument.getElementById(\'" + id + "\'),\n"
    html += "\t\t\tdocument.getElementById(\'" + modal_id + "\'),\n"
    html += "\t\t\tdocument.getElementById(\'" + modal_content_id + "\'))\";>\n"
    html += "\t</img>\n"
    html += "\t<div id=\"" + modal_id + "\" class=\"modal\">\n"
    html += "\t\t<span class=\"close\" onclick=\"closeImg(document.getElementById(\'" + modal_id + "\'))\">&times;</span>\n"
    html += "\t\t<img class=\"modal-content\" id=\"" + modal_content_id + "\">\n"
    html += "\t</div>\n"
    html += "</div>\n"

    return html
    

for file in file_list:
    final_html += generate_html(file)

def load_html_to_output_file():
    f = open(output_file, "a")
    f.write(final_html)
    f.close()

load_html_to_output_file()