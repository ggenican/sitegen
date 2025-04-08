from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    first_node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    second_node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
    
    print(second_node.props_to_html())

main()