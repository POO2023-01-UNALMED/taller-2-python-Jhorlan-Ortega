class Asiento:

    def __init__(self, color, precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro
        
    def cambiarColor(self,color):
        if color=="rojo":
            self.color=color
        elif color=="verde":
            self.color=color
        elif color=="amarillo":
            self.color=color 
        elif color=="negro":
            self.color=color
        elif color=="blanco":
            self.color=color

class Auto:
    cantidadcreados=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
    def cantidadAsientos(self):
        numeroAsientos=0
        
        for asiento in self.asientos:
            if (type(asiento))==Asiento:
                    numeroAsientos=numeroAsientos+1
        return numeroAsientos

    def verificarIntegridad(self):
        mensaje1="Auto original"
        mensaje2="Las piezas no son originales"
        if (self.registro==self.motor.registro):
            for asiento in self.asientos:
                if(type(asiento)==Asiento):
                    if asiento.registro != self.registro:
                        return mensaje2
            return mensaje1
        return mensaje2

class Motor:

    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self, registro):
        self.registro=registro

    def asignarTipo(self,tipo):
        if (tipo=="electrico" or tipo=="gasolina"):
            self.tipo=tipo











