class Buscador():
    def __init__(self,eventos):
        
        self.evento = [x for x in eventos]
        
        """ print(self.errores)

        for x in self.errores:
           print(x['estado']) """
    pass

    def razon(self):
                
        for x in self.evento:
            print(x)
            x.update(razon= '')
            if x['tipo'] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                if x['monto']>x['saldoEnCuenta']:
                    x.update(razon= "El retiro de $"+ str(x['monto'])+" exede el saldo en cuenta de $" + str(x['saldoEnCuenta']))
                    x['tipo'] ="RETIRO EFECTIVO CAJERO AUTOMATICO"
                    continue

                if x['monto']>x['cupoDiarioRestante']:
                    x.update(razon= "El retiro de  $" + str(x['monto']) + " exede el cupo diario restante de $" + str(x['cupoDiarioRestante']))
                    x['tipo'] ="RETIRO EFECTIVO CAJERO AUTOMATICO"
