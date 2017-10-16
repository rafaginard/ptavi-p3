#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from  urllib.request import urlretrieve
import json
import sys
import smallsmilhandler


class KaraokeLocal(object):

    def __init__(self, fichero):
        parser = make_parser()
        sHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(fichero)
        self.etiquetas =  sHandler.get_tags()

    def __str__(self):
        for etiquetas in self.etiquetas:
            lista_atributos = []
            for etiqueta in etiquetas:
                if etiqueta != "element" and etiquetas[etiqueta] != "":
                    lista_atributos += ("\t", etiqueta,'="',
                                        etiquetas[etiqueta],'"')
            print(etiquetas["element"], "".join(lista_atributos))

    def to_json(self, fichero, jfichero = ""):
        if jfichero == "":
            jfichero = fichero.split(".")[0] + ".json"
        json.dump([self.etiquetas], open(jfichero, "w"))

    def do_local(self):
        for etiquetas in self.etiquetas:
            for etiqueta in etiquetas:
                if etiqueta == "src" and not etiquetas[etiqueta].find("http://"):
                    urlretrieve(etiquetas[etiqueta],
                                etiquetas[etiqueta].split("/")[-1])
                    etiquetas[etiqueta] = etiquetas[etiqueta].split("/")[-1]

if __name__ == "__main__":
    try:
        fichero = KaraokeLocal(sys.argv[1])
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")

    fichero.__str__()
    fichero.to_json(sys.argv[1])
    fichero.do_local()
    fichero.__str__()
