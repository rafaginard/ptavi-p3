#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler

if __name__ == "__main__":
    parser = make_parser()
    sHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(sHandler)
    try:
        parser.parse(open(sys.argv[1]))
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")


#    for etiqueta in self.etiquetas:
#        for clave, atributo in etiqueta.items():
#            print(clave + "---> " + atributo)


    for etiquetas in sHandler.etiquetas:
        lista_atributos = []
        lista = ""
        for clave, atributo in etiquetas.items():
            if clave != "element":
                lista_atributos += ("\t", clave," = ", atributo, " ")
        print(etiquetas["element"], lista.join(lista_atributos))
