class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == {}:
            return 'empty props given'
        elif self.props == None:
            return 'no props given'
        
        return f' href="{self.props["href"]}" target="{self.props["target"]}"'
    
    def __eq__(self, htmlnode):
        if self.tag == htmlnode.tag and self.value == htmlnode.value and self.children == htmlnode.children and self.props == htmlnode.props:
            return True
        return False
    
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value == "":
            raise ValueError()

        if self.tag == "":
            return self.value
        
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __eq__(self, htmlnode):
        if self.tag == htmlnode.tag and self.value == htmlnode.value and self.props == htmlnode.props:
            return True
        return False
    
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, props: {self.props}"