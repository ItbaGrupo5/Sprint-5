class Address():
    def __init__(self, address):
        self.calle= address['calle']
        self.numero= address['numero']
        self.ciudad= address['ciudad']
        self.provincia= address['provincia']
        self.pais= address['pais']