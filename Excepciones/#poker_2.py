#poker_2
class Card:
	CLUBS = '♣'
	DIAMONDS = '◆'
	HEARTS = '❤'
	SPADES = '♠'
	PALOS = {'CLUBS': CLUBS, 'DIAMONDS': DIAMONDS, 'HEARTS': HEARTS, 'SPADES': SPADES}
	VALORES = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

	def __init__(self, valor: int | str, palo: str):
		self.valor = valor
		self.palo = palo
		if self.palo not in self.PALOS.keys():
			raise InvalidCardError(f'{self.palo} no es un palo soportado')
		elif isinstance(self.valor, int):
			if self.valor < 1 or self.valor > 13:
				raise InvalidCardError(f'{self.valor} no es un número soportado')
		elif isinstance(self.valor, str):
			if self.valor not in self.VALORES:
				raise InvalidCardError(f'{self.valor} no es un símbolo soportado')
            
	@property
	def cmp_valor(self) -> int:
		'''Devuelve el valor (numérico) de la carta para comparar con otras.
        Tener en cuenta el AS.'''
		if isinstance(self.valor, int):
			value = self.valor
		else:
			value = self.VALORES.index(self.valor)+1
		if value == 1:
			value = 14
		return value
    
	def __repr__(self):
		'''Devuelve el glifo de la carta'''
		if isinstance(self.valor, int):
			numero = self.VALORES[self.valor-1]
		else:
			numero = self.valor
		return f'El {numero} del palo {self.PALOS[self.palo]}'
	
	def __eq__(self, other):
		if isinstance(self.valor, int):
			numero1 = self.VALORES[self.valor-1]
		else:
			numero1 = self.valor
		if isinstance(other.valor, int):
			numero2 = self.VALORES[other.valor-1]
		else:
			numero2 = other.valor
		if numero1 == numero2 and self.palo == other.palo:
			return True
		return False
	
	def __lt__(self, other):
		return self.cmp_valor < other.cmp_valor
	
	def __gt__(self, other):
		return self.cmp_valor > other.cmp_valor

	def __add__(self, other):
		if self.cmp_valor > other.cmp_valor:
			self.palo = self.palo
		else:
			self.palo = other.palo
		numero = self.cmp_valor + other.cmp_valor
		if numero > 13:
			self.valor = 1
		else:
			self.valor = numero
		return self.__repr__()
	def es_as(self):
		if self.valor == 'A' or self.valor == 1:
			return True
		return False
	@classmethod
	def get_palos(self):
		lista_palos = list(self.PALOS.keys())
		return ','.join(lista_palos)

class InvalidCardError(Exception):
	def __init__(self, message = None, default = 'Carta no valida. '):
		mensaje = default + message
		super().__init__(mensaje)


uno = Card('4', 'DIAMONDS')
dos = Card('3', 'CLUBS')
print(uno.get_palos())