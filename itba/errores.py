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


            elif x['tipo']== "ALTA_TARJETA_CREDITO":
                if x['totalTarjetasDeCreditoActualmente'] >= 5:
                    x.update(razon= "Actualmente tiene el maximo de tarjetas de credito ("+str(x['totalTarjetasDeCreditoActualmente'])+")")
                    x['tipo'] ="ALTA TARJETA CREDITO"

            elif x['tipo']== "ALTA_CHEQUERA":
                if x['totalChequerasActualmente'] >=2:
                    x.update(razon= "Actualmente tiene el maximo de chequeras ("+str(x['totalChequerasActualmente'])+")")
                    x['tipo'] = "ALTA CHEQUERA"

            elif x['tipo']== "COMPRA_DOLAR":
                if x['monto']>x['saldoEnCuenta']:
                    x.update(razon= "El monto de compra (" +str(x['monto']) + ") exede el saldo en cuenta (" +str(x['saldoEnCuenta'])+")")
                    x['tipo'] = "COMPRA DOLAR"

            elif x['tipo']== "TRANSFERENCIA_ENVIADA":
                if x['monto']> x['saldoEnCuenta']:
                    x.update(razon= "El monto de la transferencia exede el saldo en cuenta")
                    x['tipo'] = "TRANSFERENCIA ENVIADA"
       
            if  x['estado']=="ACEPTADA":
                if x['tipo'] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                    x['tipo'] ="RETIRO EFECTIVO CAJERO AUTOMATICO"
                    x['razon'] =""                    
                if x['tipo']== "TRANSFERENCIA_RECIBIDA":
                    x['tipo'] ="TRANSFERENCIA RECIBIDA"
            


        
        return self.evento