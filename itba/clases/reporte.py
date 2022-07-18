import codecs
import webbrowser
class GetHTML():
    def __init__(self,errores,cliente):
        print()
        self.errores = errores
        self.nombre = cliente.nombre
        self.apellido = cliente.apellido
        self.dni = cliente.dni
        self.numero = cliente.numero
        self.tipo = cliente.tipo

        
        html ="<link href="+" https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" +" rel="+"stylesheet" +" integrity="+"sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" +" crossorigin="+"anonymous"+">"
        html+="<div class="+"container"+">"+"<h1>"+ self.apellido +", "+ self.nombre + "</h1> <div> Numero de cliente: "+ str(self.numero) + "</div> <div>DNI: "+str(self.dni)+ "</div><div>Direccion: "+cliente.direccion.calle+" "+str(cliente.direccion.numero)+", "+cliente.direccion.ciudad+", "+cliente.direccion.provincia  + "</div>"+ "</div>"
        html+='<table class="container table table-striped">'

        
        row="<thead><tr><th scope="+"col"+">Fecha</th><th scope="+"col"+">Tipo</th><th scope="+"col"+">Estado</th><th scope="+"col"+">Monto</th><th scope="+"col"+">Razon</th></tr></thead> <tbody>"
        html+=row
        self.html=html
        for x in errores:
            row="<tr><td>"+ str(x['fecha']) + "</td><td>"+ str(x['tipo']) + "</td><td>"+ str(x['estado']) + "</td><td>"+ str(x['monto']) + "</td><td>"+ str(x['razon']) + "</td></tr>"
            html+=row
           
           
        html+=' </tbody></table>'
        self.html=html
   
        with open(cliente.tipo + "_output.html","w") as text_file:
            text_file.write(html)
            webbrowser.open(cliente.tipo + "_output.html")
            text_file.close()        
