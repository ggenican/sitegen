import os
import shutil
from htmlnode import HTMLNode, ParentNode
from markdown_blocks import (
    markdown_to_html_node,
    extract_title
)

def copySourceFiles(base, items):
    source = items
    for item in os.listdir(base):
        if os.path.isdir(f"{base}/{item}/"):
            source[os.path.join(base, item)] = "folder"
            copySourceFiles(f"{base}/{item}/", source)
        else:
            source[os.path.join(base, item)] = "file"

    return source


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}\n")
    markdown_file = open(from_path).read()
    template_file = open(template_path).read()

    html = markdown_to_html_node(markdown_file).to_html()
    title = extract_title(markdown_file)

    page = template_file.replace("{{ Title }}", title).replace("{{ Content }}", html)
    
    output = open(dest_path, "x")
    output.write(page)
    output.close()


def system_crawler(base, items):
    source = items
    for item in os.listdir(base):
        print(f"{base}/{item}")
        if os.path.isdir(f"{base}/{item}"):
            system_crawler(f"{base}/{item}", source)
        else:
            source.append(os.path.join(base, item))

    return source


def generate_page_recursive(from_path_dir, template_path, dest_path_dir):
    return 0


def main():
    sourceFolder = os.getcwd()
    destFolder = os.getcwd() + "/public"

    if os.path.exists(destFolder):
        shutil.rmtree(destFolder)
    os.mkdir(destFolder)
    source = copySourceFiles(sourceFolder + "/static", {})

    # first create the folder structure
    for key in source.keys():
        if source[key] == "folder":
            os.mkdir(key.replace("static", "public"))

    # then copy all the files into the corresponding folder
    for key in source.keys():
        if source[key] == "file":
            shutil.copy(key, key.replace("static", "public"))

    markdown_list = system_crawler(os.getcwd() + "/content", [])
    for md in markdown_list:
        generate_page(md, sourceFolder + "/template.html", md.replace("content", "public").replace(".md", ".html"))

main()
