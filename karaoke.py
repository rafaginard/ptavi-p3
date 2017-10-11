#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from  urllib.request import urlretrieve
import json
import sys
import smallsmilhandler


class KaraokeLocal(object):

    def __init__(self, file):
        parser = make_parser()
        sHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(file)
        self.etiquetas =  sHandler.get_tags()

    def __str__(self):
        for etiquetas in self.etiquetas:
            lista_atributos = []
            for clave, atributo in etiquetas.items():
                if clave != "element" and atributo != "":
                    lista_atributos += ("\t", clave," = ", atributo, " ")
            print(etiquetas["element"], "".join(lista_atributos))

    def to_json(self):
        json.dump([self.etiquetas], open("karaoke.json", "w"))

    def do_local(self):
        for etiquetas in self.etiquetas:
            for clave, atributo in etiquetas.items():
                if clave == "src" and not atributo.find("http://"):
                    urlretrieve(atributo, atributo.split("/")[-1])

if __name__ == "__main__":
    try:
        fichero = KaraokeLocal(sys.argv[1])
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")

    fichero.__str__()
    fichero.to_json()
    fichero.do_local()
