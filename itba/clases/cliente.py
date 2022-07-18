from ..clases import direcciones
class Cliente:
    def __init__(self,data):
        self.tipo=data['tipo']
        self.dni=data['dni']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.numero=data['numero']

        self.getAddress(data)
        self.direccion= direcciones.Address(self.direccion)

    def getAddress(self, data):
        self.direccion= data['direccion']


    #   """   #print("se creo cliente: "+ self.dni) """

    def puede_comprar_dolar(self):
        return True
    pass



class ClienteGOLD(Cliente):
    def __init__(self, data):
        print("Se creo GOLD")
        super().__init__(data)
    pass


class ClienteClassic(Cliente):
    def __init__(self, data):
        print("Se creo Classic")
        super().__init__(data)

    def puede_comprar_dolar(self):
        return False

class ClienteBlack(Cliente):
    def __init__(self, data):
        print("Se creo BLACK")
        super().__init__(data)
    pass