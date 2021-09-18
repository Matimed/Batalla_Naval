import pygame
from pygame.sprite import AbstractGroup
from view.tools.caja_entrada import SpriteCajaEntrada
from view.tools.boton_flecha import SpriteBotonFlecha


class SelectorNumerico(AbstractGroup):
    """ Herramienta para seleccionar en un determinado rango de numeros."""

    def __init__(self, maximo, minimo, tamaño_caja=(60,60), color_texto=(255,255,255), color_caja=(0,0,0)):
        assert maximo > minimo, (
            'El valor maximo no puede ser menor o igual que el minimo.'
        )

        self.maximo = maximo
        self.minimo = minimo
        self.numero = minimo
        self.boton_arriba = SpriteBotonFlecha(tamaño_caja[0], 90)
        self.boton_abajo = SpriteBotonFlecha(tamaño_caja[0], 270)
        self.caja = SpriteCajaEntrada(str(minimo), (10, int(tamaño_caja[1] * 1/3)), tamaño_caja, color_texto, color_caja, True)


    def update(self):
        if self.boton_arriba.update():
            if self.numero < self.maximo:
                self.numero += 1
        
        if self.boton_abajo.update():
            if self.numero > self.minimo:
                self.numero -= 1

        self.caja.set_texto(str(self.numero))
        self.caja.generar_texto_sprite()
    

    def draw(self, superficie):
        self.caja.get_rect().center = (100, 100)
        self.boton_arriba.get_rect().midbottom = (self.caja.get_rect().midtop[0], self.caja.get_rect().midtop[1] - 5)
        self.boton_abajo.get_rect().midtop = (self.caja.get_rect().midbottom[0], self.caja.get_rect().midbottom[1] + 5)

        self.caja.draw(superficie)
        self.boton_arriba.draw(superficie)
        self.boton_abajo.draw(superficie)


    def get_numero(self):
        return self.numero