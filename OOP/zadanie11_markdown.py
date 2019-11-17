

class Document:
    def __init__(self):
        self.elements = []

    def add_element(self, item):
        self.elements.append(item)

    def render(self):
        output = ""
        for el in self.elements:
            output += el.render()
        return output

class Element:
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text + "\n"


class HeaderElement(Element):

    def render(self):
        text = super().render()
        text += "\n"+"="*(len(text)-1) + "\n\n"
        return text


class LinkElement(Element):
    def __init__(self, text, url):
        self.text = text
        self.url = url

    def render(self):
        return f"[{self.text}](http://{self.url})\n\n"








def test_render():
    dokument = Document()
    dokument.add_element(HeaderElement ("Header"))
    dokument.add_element(LinkElement("ABC", "wp.pl"))
    dokument.add_element(Element("simple text"))

    expected = """Header

======

[ABC](http://wp.pl)

simple text
"""
    assert dokument.render() == expected
