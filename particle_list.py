import json
from particle import Particle
from algorithms import *

class Particle_List:
    def __init__(self):
        self.__Particles = []

    def __len__(self):
        return len(self.__Particles) 

    def __str__(self):
        return "".join(
            str(particle) for particle in self.__Particles
        )

    def __iter__(self):
        self.cont = 0
        return self
    
    def __next__(self):
        if(self.cont < len(self.__Particles)):
            Particle = self.__Particles[self.cont]
            self.cont += 1
            return Particle
        else:
            raise StopIteration

    def addToEnd(self, part:Particle):
        self.__Particles.append(part)

    def addFirst(self, part:Particle):
        self.__Particles.insert(0, part)

    def showAll(self):
        for part in self.__Particles:
            print(part)
    
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particle.to_dict() for particle in self.__Particles]
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__Particles =[Particle(**part) for part in lista]
                
            return 1
        except:
            return 0
    
    def sort_byId(self):
        self.__Particles.sort(key=lambda Particle: float(Particle.id))
    
    def sort_byDistance(self):
        self.__Particles.sort(key=lambda Particle : Particle.distancia, reverse=True)
    
    def sort_bySpeed(self):
        self.__Particles.sort(key=lambda Particle : Particle.velocidad)
    


