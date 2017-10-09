#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import collections

class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.etiquetas = []

    def startElement(self, name, attrs):
        if name == "root-layout":
            root_layout = collections.OrderedDict()
            root_layout["element"] = "root-layout"
            root_layout["width"] = attrs.get("width", "empty")
            root_layout["height"] = attrs.get("height", "empty")
            root_layout["background-color"] = attrs.get("background-color",
                                                        "empty")
            self.etiquetas.append(root_layout)
        elif name == "region":
            region = collections.OrderedDict()
            region["element"] = "region"
            region["id"] = attrs.get("id", "empty")
            region["top"] = attrs.get("top", "empty")
            region["bottom"] = attrs.get("bottom", "empty")
            region["left"] = attrs.get("left", "empty")
            region["right"] = attrs.get("right", "empty")
            self.etiquetas.append(region)
        elif name == "img":
            img = collections.OrderedDict()
            img["element"] = "img"
            img["src"] = attrs.get("src", "empty")
            img["region"] = attrs.get("region", "empty")
            img["begin"] = attrs.get("begin", "empty")
            img["dur"] = attrs.get("dur", "empty")
            self.etiquetas.append(img)
        elif name == "audio":
            audio = collections.OrderedDict()
            audio["element"] = "audio"
            audio["src"] = attrs.get("src", "empty")
            audio["begin"] = attrs.get("begin", "empty")
            audio["dur"] = attrs.get("dur", "empty")
            self.etiquetas.append(audio)
        elif name == "textstream":
            textstream = collections.OrderedDict()
            textstream["element"] = "textstream"
            textstream["src"] = attrs.get("src", "empty")
            textstream["region"] = attrs.get("region", "empty")
            self.etiquetas.append(textstream)
    def get_tags(self):
            for etiqueta in self.etiquetas:
                for clave, atributo in etiqueta.items():
                    print(clave + "---> " + atributo)
if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open("karaoke.smil"))
    sHandler.get_tags()
