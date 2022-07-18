import json
from .clases import cliente

class Parser():
    def __init__(self,file):
        self.file = file
        self.load()
        if self.data['tipo'] == 'BLACK':
            self.cliente=cliente.ClienteBlack(self.data)
        elif self.data['tipo'] == 'GOLD':
            self.cliente=cliente.ClienteGOLD(self.data)
        else:
            self.data['tipo'] == 'CLASSIC'
            self.cliente=cliente.ClienteClassic(self.data)
        self.eventos=self.data['transacciones']
    
    def load(self):
        f=open(self.file)
        self.data = json.load(f)
        f.close()

     
