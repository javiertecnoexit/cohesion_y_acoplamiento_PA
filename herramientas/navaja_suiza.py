from herramientas import *
from herramientas import herramienta_de_mano_multiherramienta
from abrelata import Abrelata


class Navaja_suiza(herramienta_de_mano_multiherramienta.Herramienta_de_mano_multiherramienta):
    def __init__(self):
        self.lista_de_herramientas=[]
        
        
    def generar_herramienta(self):
        abrelata= Abrelata()
        self.lista_de_herramientas.append(abrelata)
        
        