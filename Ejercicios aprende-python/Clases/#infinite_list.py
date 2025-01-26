#crear clase que permita utilizar una lista sin limites, evitando indexerror. si la lista tiene 10 elementos, y asignamos un valor
#al elemento 20 que no de error, sino que amplie la lista hasta el indice 20 rellenando el resto de valores con None

class InfiniteList:
    def __init__(self, *args, fill_value=None):
        self.lista = [i for i in args]
        self.fill_value = fill_value

    def __getitem__(self, index: int):
        valor = self.lista[index]
        return valor

    def __len__(self):
        largo = len(self.lista)
        return largo

    def __setitem__(self, index: int, item) -> None:
        hasta = len(self.lista)
        if index <= hasta:
        	self.lista.insert(index, item)
        else:
        	i = hasta
        	while index > i:
        		self.lista.append(self.fill_value)
        		i += 1
        	self.lista.insert(index, item)

    def __str__(self):
        return f'{self.lista}'
     
prueba = InfiniteList(3, 4, 5)
prueba.__setitem__(5, 10)
print(prueba)
