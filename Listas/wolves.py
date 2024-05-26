#La lista de entrada contiene ovejas y un lobo. Posibles casos:
# a) Si el lobo está cerca de una oveja, habrá que responder con el mensaje:
# "Cuidado oveja X, el lobo te va a comer".
# b) Si el lobo está al final de la lista, habrá que responder con el mensaje:
# "No te quiero ver más por aquí, lobo"
# Las posiciones hay que calcularlas empezando por el final de la lista con índice 1. 
l = ['oveja', 'lobo', 'oveja', 'oveja', 'oveja']
def wolves(a):
	i = l.index('lobo') - len(l)
	if i == (0 - len(l)):
		print('No te quiero ver más por aqui, lobo')
	else:
		print(f'Cuidado oveja {(i+1)}, el lobo te va a comer')
wolves(l)