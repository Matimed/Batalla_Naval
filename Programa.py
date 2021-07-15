from Jugador import Jugador
from Posicion import Posicion
from Tablero import Tablero
import string

class Programa:
    def __init__(self, cant_filas):
        assert cant_filas <= len(string.ascii_uppercase), "cantidad de filas mayor a cantidad de letras"

        self.posiciones = []
        for i in range(cant_filas): # La cantidad de columnas se define a partir de cant_filas
            [self.posiciones.append(Posicion(string.ascii_uppercase[i], x)) for x in range(cant_filas)]

        cant_barcos = 8
        self.tableros = []
        [self.tableros.append(Tablero(self.posiciones, cant_barcos)) for i in range(2)]
        self.jugadores = []
        [self.jugadores.append(Jugador(self.tableros[i], self)) for i in range(2)]

    def validar_posicion(self, y, x):
        return (y, x) in self.posiciones

    def traducir_posicion(self, y, x):
        return self.posiciones[self.posiciones.index((y, x))]

    def juego(self):
        for jugador in self.jugadores:
            jugador.preparar_tablero()
        
        while True:
            self.jugadores[0].disparar
            self.jugadores[1].disparar