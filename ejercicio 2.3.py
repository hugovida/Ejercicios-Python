#ejercicio 2.3
class Articulo:
    codigo
    cantidad
    precio

def __init__(self,codigo,cantidad,precio):
    self.codigo=codigo
    self.cantidad=cantidad
    self.precio=precio

def getCodigo():
    return self.codigo

def getCantidad():
    return self.codigo

def mostrarCodigo(codigo):
    print("codigo: ",codigo)

def mostrarCantidad(cantidad):
    print("cantidad: "cantidad)

def vender(num):
    cantidad=cantidad-num

def comprar(num):
    cantidad=cantidad+num

class ArticuloVip(Articulo):
    def __init__(self, codigo, cantidad, precio):
        super().__init__(codigo, cantidad, precio)
        super().precio=precio-precio*0.10

    def imprimir(cantidad,precio):
        print("cantidad: ",cantidad," precio: ",precio)    

    def pagarImpuestos(precio):
        if precio>=1000:
            print("PAGA IMPUESTOS")
        elif precio<1000:
            print("NO PAGA IMPUESTOS")


articulo_normal = Articulo(codigo="A001", cantidad=5, precio=800)
print("Artículo Normal:")
articulo_normal.imprimir()
articulo_normal.paga_impuestos()

# Crear un artículo VIP y probar los métodos
articulo_vip = ArticuloVIP(codigo="V001", cantidad=3, precio=1200)
print("\nArtículo VIP:")
articulo_vip.imprimir()
articulo_vip.paga_impuestos()