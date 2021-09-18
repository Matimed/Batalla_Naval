import pygame
from view.referencias import FUENTE
from events import EventoGlobal as ev
from view.tools import SpriteCajaTexto

class SpriteCajaEntrada(pygame.sprite.Sprite):
    """ Rectángulo en el cual se puede digitar texto y acceder a este."""

    def __init__(self, texto_inicial = '', margen=(5,20), tamaño=(350,50), color_texto=(255,255,255), color_caja=(0,0,0), solo_lectura=False):
        super().__init__()
        self.solo_lectura = solo_lectura

        self.caja_sur = pygame.Surface(tamaño)
        self.caja_sur.fill(color_caja)

        self.margen = margen
        self.alto_texto = tamaño[1] - margen[1]
        self.color_texto = color_texto
        self.texto = texto_inicial
        self.texto_sprite  = None
        self.generar_texto_sprite()
        
        self.rect = self.caja_sur.get_rect()

        self._presionado = False


    def update(self):
        focus = self.rect.collidepoint(pygame.mouse.get_pos())

        if focus:
            if pygame.mouse.get_pressed()[0] and not self._presionado:
                self._presionado = True
        else:
            if pygame.mouse.get_pressed()[0] and self._presionado: 
                self._presionado = False

        return self._presionado


    def escribir(self, eventos):
        if not self.solo_lectura:
            for evento in eventos:
                if evento.type == ev.TECLA_PRESIONADA:
                    if evento.key == pygame.K_BACKSPACE:
                        self.texto = self.texto[:-1]

                        self.generar_texto_sprite()

                    elif evento.key == pygame.K_SPACE:
                        return

                    else:
                        self.texto += evento.unicode

                        self.generar_texto_sprite()


    def draw(self, surface):
        """ Recibe una superficie y dibuja  la superficie de la caja y del texto en ella."""

        surface.blit(self.caja_sur, self.rect)
        
        self.texto_sprite.get_rect().center = self.get_rect().center

        surface.blit(self.texto_sprite.get_surface(), self.texto_sprite.get_rect())


    def set_texto(self, texto):
        self.texto = texto


    def get_texto(self):
        return self.texto


    def get_rect(self):
        return self.rect


    def _verificar_largo_texto(self, texto_sprite):
        """ Verifica que la longitud de la superficie de un texto sea 
            adecuada para la superfice del fondo rectangular.
        """

        return texto_sprite.get_tamaño()[0] > self.caja_sur.get_size()[0] - self.margen[0]


    def generar_texto_sprite(self):
        """ Genera una instancia de SpriteCajaTexto según
            el texto en su atributo homonimo.
        """

        texto_sprite = SpriteCajaTexto(self.texto, self.color_texto, self.alto_texto)

        if  not self._verificar_largo_texto(texto_sprite):
            self.texto_sprite = texto_sprite

        else:
            self.texto = self.texto[:-1]
            self.generar_texto_sprite()