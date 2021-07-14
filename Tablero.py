from Barco import *
from Posicion import *
from Celda import *

class Tablero:
    def __init__(self, posiciones, cant_barcos):
        """ Recibe una lista de objetos tipo Posicion a los que asignara
            una celda por cada uno y la cantidad de barcos que se quieren utilizar"""

        assert type(posiciones) == list
        assert type(cant_barcos) == int
        self.celdas = {}
        self.barcos_disponibles = []

        #Crea el diccionario de celdas a partir de las posiciones
        for posicion in posiciones: 
            self.celdas[posicion] = [Celda()]

        #Crea la lista de barcos de la cantidad pedida
        for i in range(cant_barcos):
            self.barcos_disponibles.append(Barco())


    def _buscar_celda(self, posicion):
            """Dada una posicion devuelve la celda correspondiente"""

            assert isinstance(posicion, Posicion), "La posicion debe ser un objeto tipo Posicion"
            if posicion in self.celdas:
                return self.celdas.get(posicion)
            else:
                raise ValueError("La posicion no esta en la lista")


    def agregar_barco(self, posicion):
        celda = self._buscar_celda(posicion)
        celda.agregar_barco(self.barcos_disponibles.pop())


    def quitar_barco(self, posicion):
            celda = self._buscar_celda(posicion)
            self.barcos_disponibles.append(celda.quitar_barco())


    def estado_celda(self, posicion):
        """ Dada una posicion de una celda devuelve su estado
            Argumentos:
                posicion: Posicion
            Devuelve: 
                bool: si contiene un barco
                bool: si esta marcada.
        """

        celda = self._buscar_celda(posicion)
        return celda.haber_barco(), celda.get_marca()


    def barcos_disponibles(self):
        """Devuelve la cantidad de barcos disponibles"""

        return len(self.barcos_disponibles)
    