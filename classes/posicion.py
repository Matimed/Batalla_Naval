class Posicion:
    """ Sistema de coordenadas que utiliza la notacion 'x', 'y'
        para representar univocamente una ubicacion particular 
        en cualquier instancia de Tablero. """

    def __init__(self, y, x):
        """ Recibe:
            y:<str> len = 1
            x:<int>"""

        self.verificar_formato(y, x)

        self.x = x
        self.y = y.upper()


    def get_posicion(self):
        return self.y, self.x


    def __eq__(self, other):
        assert (isinstance(other, Posicion) or type(other) == tuple), "No es posible comparar una Posicion con otro objeto"

        if isinstance(other, Posicion):
            self.verificar_formato(self.y, self.x)

            return other.get_posicion() == self.get_posicion()
        elif type(other) == tuple:
            assert len(other) == 2, "La tupla pasada por parametro debe constar de dos elementos"
            self.verificar_formato(other[0], other[1])

            return (other[0].upper(), other[1]) == self.get_posicion()

    def __hash__(self):
        return hash((self.y, self.x))

    def verificar_formato(self, y, x):
        assert type(x) == int, "'x' debe ser int"
        assert type(y) == str, "'y' debe ser str"
        assert len(y) == 1, "'y' debe constar de un solo caracter"


    def __repr__(self):
        return f"({self.y}, {self.x})"