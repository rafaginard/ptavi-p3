#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.lista_etiquetas = []
        self.etiquetas = ["root-layout", "region", "img", "audio",
                          "textstream"]
        self.attrDict = {"root-layout": ["width", "height",
                                         "background-color"],
                         "region": ["src", "top", "bottom", "left", "right"],
                         "img": ["src", "region", "begin", "dur"],
                         "audio": ["src", "begin", "dur"],
                         "textstream": ["src", "region"]}

    def startElement(self, name, attrs):

        if name in self.etiquetas:
            tempDcit = {}
            tempDcit["element"] = name
            for atribute in self.attrDict[name]:
                tempDcit[atribute] = attrs.get(atribute, "")
            self.lista_etiquetas.append(tempDcit)

    def get_tags(self):
        return self.lista_etiquetas

if __name__ == "__main__":
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open("karaoke.smil"))
    print(sHandler.get_tags())
