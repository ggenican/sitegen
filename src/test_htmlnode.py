import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_html_eq(self):
        node = HTMLNode(
            tag="This is a tag",
            value="This is a value",
            children=["This is a child"],
            props={"This is a prop"}
        )
        
        node2 = HTMLNode(
            tag="This is a tag",
            value="This is a value",
            children=["This is a child"],
            props={"This is a prop"}
        )
        self.assertEqual(node, node2)

    def test_html_not_equal_tag(self):
        node = HTMLNode(tag="p")
        node2 = HTMLNode(tag="b")
        self.assertNotEqual(node, node2)

    def test_html_not_equal_value(self):
        node = HTMLNode(value="This is a value")
        node2 = HTMLNode(value="This is a different value")
        self.assertNotEqual(node, node2)

    def test_html_not_equal_child(self):
        node = HTMLNode(children="This is a child")
        node2 = HTMLNode(children="This is a different child")
        self.assertNotEqual(node, node2)

    def test_html_props_to_html(self):
        # Create an HTMLNode with some props
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        
        # Check if the props_to_html method returns the expected string
        expected = ' href="https://example.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)
        
    def test_html_props_to_html_empty(self):
        # Test with empty props
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), 'empty props given')
        
    def test_html_props_to_html_none(self):
        # Test with props=None (the default)
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), 'no props given')

    
    #------------------------------------------------------------------------------------#


    def test_leaf_eq(self):
        node = LeafNode(
            tag="p",
            value="This is a value",
            props={"This is a prop"}
        )
        
        node2 = LeafNode(
            tag="p",
            value="This is a value",
            props={"This is a prop"}
        )        
        self.assertEqual(node, node2)

    def test_leaf_not_equal_tag(self):
        node = LeafNode("", "p")
        node2 = LeafNode("", "b")
        self.assertNotEqual(node, node2)

    def test_leaf_not_equal_value(self):
        node = LeafNode("p", "This is a value")
        node2 = LeafNode("p", "This is a different value")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()