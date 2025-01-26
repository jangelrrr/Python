def run(nif: str) -> str:
    lista = 'TRWAGMYFPDXBNJZSQVHLCKE'
    wnif = str(nif) + str(lista[nif%23])

    return wnif

print(run(78654355))
