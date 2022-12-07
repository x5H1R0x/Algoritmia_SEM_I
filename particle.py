from algorithms import euclidean_distance

class Point:
    def __init__(self, x=0, y=0):
        self.point_X = x
        self.point_Y = y
    
class Particle:
    def __init__(self, id="", origen_x=0, origen_y=0, destino_x=0, destino_y=0, velocidad=0, red=0, green=0, blue=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = euclidean_distance(origen_x, origen_y, destino_x, destino_y)
    
    def __str__(self) -> str:
        return(
            '\nID: ' + str(self.__id) +
            '\nOrigen X: ' + str(self.__origen_x) +
            '\nOrigen Y: ' + str(self.__origen_y) + 
            '\nDestino X: ' + str(self.__destino_x) +
            '\nDestino Y: ' + str(self.__destino_y) +
            '\nVelocidad: ' + str(self.__velocidad) +
            '\nRojo: ' + str(self.__red) +
            '\nVerde: ' + str(self.__green) +
            '\nAzul: ' + str(self.__blue) +
            '\nDistancia: ' + str(self.__distancia) +
            '\n'
        )

    def __lt__(self, other):
        return self.id < other.id

    def to_dict(self):
        return{
            
            "id": self.__id,
            "origen_x": self.__origen_x,
            "origen_y": self.__origen_y,
            "destino_x": self.__destino_x,
            "destino_y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue

        }

    @property
    def id(self):
        return self.__id
    
    @property
    def origen_x(self):
        return self.__origen_x

    @property
    def origen_y(self):
        return self.__origen_y

    @property
    def destino_x(self):
        return self.__destino_x
    
    @property
    def destino_y(self):
        return self.__destino_y

    @property
    def velocidad(self):
        return self.__velocidad
    
    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green
    
    @property
    def blue(self):
        return self.__blue

    @property
    def distancia(self):
        return self.__distancia