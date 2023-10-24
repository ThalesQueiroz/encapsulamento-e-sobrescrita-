class Moto:
    def __init__(self, marca, modelo):
        self.__marca=marca
        self.__modelo=modelo
    
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca= marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo=modelo

moto1=moto('Honda', 'CB1000')

print(moto1.marca)
print(moto1.modelo)

moto1.marca='Honda'
moto1.modelo='CB1000'
print(f'\n{moto1.marca}')
print(moto1.modelo)
