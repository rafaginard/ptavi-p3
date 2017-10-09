#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from  urllib.request import urlretrieve
import json
import sys
import smallsmilhandler


if __name__ == "__main__":
    parser = make_parser()
    sHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(sHandler)
    url = ""
    try:
        parser.parse(open(sys.argv[1]))
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")

    for etiquetas in sHandler.lista_etiquetas:
        lista_atributos = []

        for clave, atributo in etiquetas.items():
            if clave != "element":
                lista_atributos += ("\t", clave," = ", atributo, " ")
            if clave == "src" and not atributo.find("http://"):
                print("HASTA AQUI: " + atributo)
                urlretrieve(atributo, "local_file.rt")
        print(etiquetas["element"], "".join(lista_atributos))

    json.dump([sHandler.lista_etiquetas], open("karaoke.json", "w"))
