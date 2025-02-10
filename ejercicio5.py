# Para agrupar datos en diccionarios
from collections import defaultdict 

data = {
    'Ciudad': ['Nueva York', 'Los Ángeles', 'Nueva York', 'Chicago'],
    'Ventas': [100, 150, 200, 50]
}

def agrupar_por_ciudad(data):
    ventas_por_ciudad = defaultdict(int)
    for ciudad, venta in zip(data["Ciudad"], data["Ventas"]):
        ventas_por_ciudad[ciudad] += venta
    return dict(ventas_por_ciudad)

resultado = agrupar_por_ciudad(data)
print("Ventas por ciudad:", resultado)
