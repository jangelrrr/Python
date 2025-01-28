from datetime import datetime
trato = ('0', 'agua', 'qd', 'agua', 'qd')
clientes= {
    'Quique Castelo' : 1,
    'Ovidio Focus' : 1,
    'Mia Rodabell' : 9,
    'Asturiano Passat' : 9, 
	'Carolina Seronero' : 9,
	'M Mar' : 8,
    'Maria Roda' : 9,
    'Ivan Lieiro Toyota' : 4,
    'Ivan Lieiro Bmw' : 4,
    'Marisa Manel' : 8,
    'Castelo GLA' : 8,
    'Yoli Bermudez Touran' : 2,
    'Yoli Bermudez C4' : 9,
    'Nacho Vertical' : 8,
    'Dani Puche' : 9,
    'Lucia Vequez' : 4,
    'Fredy Quelle' : 2,
    'Maestra Insti' : 2,
    'Eden' : 3,
    'Fran Home Soledad' : 8,
    'Mary Kia Sportage' : 3,
    'Marta Lage' : 3,
    'Marcos frigomar' : 3,
    'Albano Passat' : 7,
    'Alicia Risitas Mercedes' : 6,
    'Bussy Avensis' : 7,
    'Ivan Ganados Lieiro' : 6,
    'Javi Bidueiros SQ5' : 0,
    'Juanma' : 6,
    'Francisco Lieiro' : 0,
    'Madrileños Conchi' : 6,
    'Mon' : 7,
    'David Joticar Hilux' : 4,
    'Sofia Farmacia': 4,
    'Araceli' : 7,
    'Javi Bidueiros A8' : 7,
    'Sofia Farmacia' : 8,
    'Bango T7' : 8,
    'Manolo Villalba' : 8,
    'Oscar bmw' : 8,
    'Bango Cupra' : 8,
    'Castelo GLC' : 9
}

def buscar_nombre():
	letras = input()
	def buscar_por_letras(dici, letters=letras):
		nombres = tuple(dici.keys())
		opciones = []
		for i in nombres:
			if letters in i.lower():
				opciones.append(i)
		if opciones ==[]:
			print('No encontrado')
			return buscar_nombre()
		dici_opciones = {}
		for i, opcion in enumerate(opciones):
			dici_opciones[i] = opcion
			print(f'{i}: {opcion}')
		option = int(input())
		nombre_opcion = dici_opciones[option]
		return nombre_opcion
	def buscar_por_nombre(dici, word=letras):
		try:
			dici[word]
		except KeyError:
			print('No encontrado')
			return buscar_nombre()
		else:
			nombre_complete = word
			return nombre_complete
	if letras[0].isupper():
		name = buscar_por_nombre(clientes)
		return name
	else:
		name = buscar_por_letras(clientes)
		return name

def tratar(dici, name, trato, position, mes=datetime.now().month):
	hace_meses = mes - dici[name]
	if hace_meses < 0:
		meses_antes = 12 - abs(hace_meses)
		hace_meses = meses_antes
	if hace_meses > 4:
	    tratamiento = 'acondicionar'
	    return f'Linea {position} \nTratamiento {tratamiento}'
	else:
	    tratamiento = trato[hace_meses]
	return f'Tratamiento {tratamiento}'


nombre = buscar_nombre()
n = tuple(clientes.keys())
posicion = (n.index(nombre)) + 4
if clientes[nombre] == 0:
	print('Linea',  posicion, '\n',  'No hay valores')
else:
	resultado = tratar(clientes, nombre, trato, posicion)
	print(resultado)