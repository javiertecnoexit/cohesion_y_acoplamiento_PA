from pickle import FALSE, TRUE


class Navaja_Suiza:
    def __init__(self):
        pass
    
        

    def navaja(sef):
        print("desplegar navaja")

    def pinza(self):
        print("desplegar pinza")

    def tijera(self):
        print("desplegar tijera")

    def __destornillador_plano(self):
        print("desplegar destornillador plano")

    def destornillador_phillips(self):
        print("desplegar destornillador phillips")

    def sacacorcho(self):
        print("desplegar sacacorcho")

    def abrelata(self):
        print("desplegar abrelata")

    def destapador(self, usa_destornillador=FALSE):
        print("desplegar destapador")
        if usa_destornillador==TRUE:
            self.__destornillador_plano()

    def serrucho(self, usa_lima=FALSE):
        print("desplegar serrucho")
        if usa_lima == TRUE:
            self.__lima()

    def __lima(self):
        print("desplegar lima")

    def pinza_de_depilar(self):
        print("desplegar pinza de depilar")

    def escarbadiente(self):
        print("desplegar escarbadiente")

    def lupa(self):
        print("desplegar navaja")

    def linterna(self):
        print("desplegar linterna")
        print("encender linterna")
        
    def boligrafo(self):
        print("desplegar boligrafo")
    
    def saca_escamas(self, usa_regla=FALSE):
        print("desplegar saca escamas")
        if usa_regla == TRUE:
            self.__regla()
    
    def __regla(self):
        print("desplegar regla")

victorinox= Navaja_Suiza()

victorinox.destapador(TRUE)