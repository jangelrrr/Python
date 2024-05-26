#crear clase SnakesLadders, la prueba llamará el metodo play(die1, die2), son los dos dados (entre 1 y 6) y el jugador moverá la suma de los dos
#tablero de 0 a 100, hay que llegar al 100 si no es justo rebota hacia atras
#escaleras: 2-38, 7-14, 8-31, 15-26, 21-42, 28-84, 36-44, 51-67, 71-91, 78-98, 87-94
#serpientes: 16-6, 46-25, 49-11, 62-19, 64-60, 74-53, 89-68, 92-88, 95-75, 99-80
#2 jugadores, empieza el primero. si el valor de los dos dados es el mismo, volverá a jugar
#return Player n Wins: si consigue ganar el juego algún jugador
#return Game Over!: si un jugador ha ganado y otro jugador intenta jugar
#return Player n is on square x: si nadie gana, retorna donde está el jugador más cercano a 100
from random import randint
class SnakesLadders:
	escaleras = {2:38, 7:14, 8:31, 15:26, 21:42, 28:84, 36:44, 51:67, 71:91, 78:98, 87:94}
	serpientes = {16:6, 46:25, 49:11, 62:19, 64:60, 74:53, 89:68, 92:88, 95:75, 99:80}
	def __init__(self, name, puntos=0):
		self.name = name
		self.puntos = puntos
	
	@staticmethod
	def jugar(sel):
			die1 = randint(1,6)
			die2 = randint(1,6)
			sel.puntos += (die1 + die2)
			if sel.puntos > 100:
				sel.puntos = 100 - (sel.puntos - 100)
			elif sel.puntos in sel.escaleras.keys():
				sel.puntos = sel.escaleras[sel.puntos]
			elif sel.puntos in sel.serpientes.keys():
				sel.puntos = sel.serpientes[sel.puntos]
			while die1 == die2:
				die1 = randint(1,6)
				die2 = randint(1,6)
				sel.puntos += (die1 + die2)
				if sel.puntos > 100:
					sel.puntos = 100 - (sel.puntos - 100)
				elif sel.puntos in sel.escaleras.keys():
					sel.puntos = sel.escaleras[sel.puntos]
				elif sel.puntos in sel.serpientes.keys():
					sel.puntos = sel.serpientes[sel.puntos]
			return sel.puntos
		
	@classmethod
	def juego(cls, self, other):
		i = 0
		while True:
			cls.jugar(self)
			if self.puntos == 100:
				return f'{self.name} gana con {self.puntos}'
			cls.jugar(other)
			if other.puntos == 100:
				return f'{other.name} gana con {other.puntos}'
			i += 1
			if i == 8:
				if self.puntos > other.puntos:
					return f'{self.name} gana con {self.puntos}'
				elif self.puntos == other.puntos:
					return f'Empatan con {self.puntos}'
				else:
					return f'{other.name} gana con {other.puntos}'

uno = SnakesLadders('Jose')
dos = SnakesLadders('Antonio')
print(SnakesLadders.juego(uno, dos))
