class Asiento:

    def _init_(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.regristro=registro
    def cambiarColor(self,color):
        if color=="rojo"or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco" :
            self.color=color


class Auto:

    def _init_(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=list(asientos)
        self.marca=marca
        self.motor=motor
        self.registro=registro
    def cantidadAsientos(self):
        numAsientos=0
        if self.asientos !=None:
            for i in self.asientos:
                if i != None:
                    numAsientos+=1
        return numAsientos

    def verificarIntegridad(self):
        mensaje1="Auto original"
        mensaje2="Las piezas no son originales"
        if self.registro==self.asientos[0].registro:
            if self.motor.registro==self.registro:
                return mensaje1
            else:
                return mensaje2
        return mensaje2

class Motor:

    def _init_(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    def cambiarRegistro(self,registro):
        self.registro=registro
    def asignarTipo(self,tipo):
        if (tipo=="electrico"or tipo=="gasolina"):
            self.tipo=tipo











