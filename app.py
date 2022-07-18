from itba import parseador
from itba import errores
from itba.clases import reporte
from itba.clases import cliente


classic = parseador.Parser("eventos_classic.json")
gold = parseador.Parser("eventos_gold.json")
black = parseador.Parser("eventos_black.json")

clienteclassic = classic.cliente
eventosclassic = classic.eventos

clientegold = gold.cliente
eventosgold = gold.eventos

clienteblack = black.cliente
eventosblack = black.eventos


buscadorA = errores.Buscador(eventosclassic)
buscadorB = errores.Buscador(eventosgold)
buscadorC = errores.Buscador(eventosblack)

razonesClassic = buscadorA.razon()
razonesGold = buscadorB.razon()
razonesBlack = buscadorC.razon()

html = reporte.GetHTML(razonesClassic, clienteclassic)
html = reporte.GetHTML(razonesGold, clientegold)
html = reporte.GetHTML(razonesBlack, clienteblack)

