from aenum import auto
from events import Evento

class EventoBatalla(Evento):
    AGUA = auto()
    BARCO_DAÑADO = auto()
    DISPARAR = auto(), 'posicion (Posicion)'