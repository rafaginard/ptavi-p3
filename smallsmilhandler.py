#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.etiquetas = []


    def startElement(self, name, attrs):
        atributos = {}
        if name == "root-layout":
            self.etiquetas = ["root-layout"]                                                         ]
            atributos["width"] = attrs.get("width", "")
            atributos["height"] = attrs.get("height", "")
            atributos["background-color"] = attrs.get("background-color", "")

            print(self.etiquetas[0])


if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open("karaoke.smil"))
